from datetime import datetime
from unittest.mock import Mock, patch

import pytest

from invoice_synchronizer.domain import (
    CityDetail,
    DocumentType,
    Invoice,
    InvoiceId,
    InvoiceStatus,
    Responsibilities,
    User,
)
from invoice_synchronizer.infrastructure.repositories.pirpos.pirpos import PirposConnector
from invoice_synchronizer.infrastructure.repositories.siigo.siigo import SiigoConnector


def make_invoice(number: int, created_on: datetime) -> Invoice:
    client = User(
        name="Client",
        document_type=DocumentType.CEDULA_CIUDADANIA,
        document_number=123,
        check_digit=None,
        city_detail=CityDetail(
            city_name="Bogota",
            city_state="Bogota",
            city_code="11001",
            country_code="CO",
            state_code="11",
        ),
        responsibilities=Responsibilities.R_99_PN,
        email="client@example.com",
        phone="3000000000",
        address="Calle 1",
    )
    return Invoice(
        client=client,
        created_on=created_on,
        invoice_id=InvoiceId(prefix="FV", number=number),
        payments=[],
        order_items=[],
        total=100,
        taxes_values={},
    )


def make_pirpos_connector() -> PirposConnector:
    connector = object.__new__(PirposConnector)
    connector.get_clients = Mock(return_value=[])  # type: ignore[method-assign]
    connector._PirposConnector__get_invoices_by_status = Mock(  # type: ignore[attr-defined]
        side_effect=lambda _start, _end, status, _clients, _pbar: [status]
    )
    return connector


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        (None, [InvoiceStatus.PAID, InvoiceStatus.ANULATED]),
        (InvoiceStatus.PAID, [InvoiceStatus.PAID]),
        (InvoiceStatus.ANULATED, [InvoiceStatus.ANULATED]),
    ],
)
def test_pirpos_get_invoices_selects_requested_status(status, expected):
    connector = make_pirpos_connector()

    invoices = connector.get_invoices(
        datetime(2026, 8, 1), datetime(2026, 8, 31), status
    )

    assert invoices == expected


def test_pirpos_get_invoices_rejects_unsupported_status():
    connector = make_pirpos_connector()

    with pytest.raises(ValueError, match="not supported"):
        connector.get_invoices(
            datetime(2026, 8, 1), datetime(2026, 8, 31), InvoiceStatus.PENDING
        )


def make_siigo_connector() -> SiigoConnector:
    connector = object.__new__(SiigoConnector)
    connector._SiigoConnector__invoice_id_to_credit_note_acentry_id = {}  # type: ignore[attr-defined]
    connector.invoice_id_to_credit_note_name = {}
    connector._SiigoConnector__invoice_number_to_siigo_id = {}  # type: ignore[attr-defined]
    return connector


def test_siigo_anulated_invoices_filters_all_credit_note_invoices_by_invoice_date():
    connector = make_siigo_connector()
    in_range_invoice = make_invoice(1, datetime(2026, 8, 15))
    out_of_range_invoice = make_invoice(2, datetime(2026, 7, 31))
    connector._get_invoice_by_id = Mock(  # type: ignore[method-assign]
        side_effect=lambda invoice_id, _clients: {
            "invoice-in-range": in_range_invoice,
            "invoice-out-of-range": out_of_range_invoice,
        }[invoice_id]
    )
    credit_notes = [
        {
            "name": "NC-1",
            "date": "2026-10-01",
            "invoice": {"id": "invoice-in-range"},
        },
        {
            "name": "NC-2",
            "date": "2026-10-01",
            "invoice": {"id": "invoice-out-of-range"},
        },
    ]

    invoices = connector._get_anulated_invoices(
        datetime(2026, 8, 1),
        datetime(2026, 8, 31),
        [],
        credit_notes,
        {"NC-1": "acentry-1", "NC-2": "acentry-2"},
    )

    assert invoices == [in_range_invoice]
    assert in_range_invoice.status == InvoiceStatus.ANULATED
    assert in_range_invoice.anulated_on == datetime(2026, 10, 1)
    assert connector._get_invoice_by_id.call_args_list == [  # type: ignore[union-attr]
        (("invoice-in-range", []), {}),
        (("invoice-out-of-range", []), {}),
    ]


def test_siigo_anulated_status_loads_all_credit_notes_before_filtering_invoices():
    connector = make_siigo_connector()
    connector.get_clients = Mock(return_value=[])  # type: ignore[method-assign]
    connector._get_credit_note = Mock(return_value=[])  # type: ignore[method-assign]
    connector._get_anulated_invoices = Mock(return_value=[])  # type: ignore[method-assign]

    invoices = connector.get_invoices(
        datetime(2026, 8, 1), datetime(2026, 8, 31), InvoiceStatus.ANULATED
    )

    assert invoices == []
    connector._get_credit_note.assert_called_once_with()  # type: ignore[union-attr]
    connector._get_anulated_invoices.assert_called_once_with(  # type: ignore[union-attr]
        datetime(2026, 8, 1),
        datetime(2026, 8, 31),
        [],
        [],
        {},
    )


def test_siigo_paid_filter_excludes_credit_note_invoices():
    connector = make_siigo_connector()
    connector._SiigoConnector__configuration = Mock()  # type: ignore[attr-defined]
    connector._SiigoConnector__siigo_access_token = "token"  # type: ignore[attr-defined]
    connector._SiigoConnector__timeout = 1  # type: ignore[attr-defined]
    connector._SiigoConnector__page_size = 200  # type: ignore[attr-defined]
    connector.credit_note_forward_days = 60
    connector._rate_limiter = Mock()
    connector.get_clients = Mock(return_value=[])  # type: ignore[method-assign]
    connector._get_credit_note = Mock(  # type: ignore[method-assign]
        return_value=[
            {
                "name": "NC-1",
                "date": "2026-08-02",
                "invoice": {"id": "annulled"},
            }
        ]
    )
    connector.get_credit_note_acentryid = Mock(  # type: ignore[method-assign]
        return_value={"NC-1": "acentry-1"}
    )
    paid_invoice = make_invoice(1, datetime(2026, 8, 1))
    annulled_invoice = make_invoice(2, datetime(2026, 8, 1))
    response = Mock(ok=True)
    response.json.return_value = {"results": [{}], "_links": {}}

    with patch(
        "invoice_synchronizer.infrastructure.repositories.siigo.siigo.requests.request",
        return_value=response,
    ), patch(
        "invoice_synchronizer.infrastructure.repositories.siigo.siigo.define_siigo_invoice",
        return_value={"paid": paid_invoice, "annulled": annulled_invoice},
    ):
        invoices = connector.get_invoices(
            datetime(2026, 8, 1), datetime(2026, 8, 31), InvoiceStatus.PAID
        )

    assert invoices == [paid_invoice]
