# Changelog

All notable changes to this project are documented in this file.

The format follows "Keep a Changelog" (https://keepachangelog.com/) and the
project follows Semantic Versioning (https://semver.org/).

This changelog was reconstructed from the repository git history.

## [Unreleased]

- No unreleased changes recorded.

## History (reconstructed from git)

### 2026

- 2026-05-08 — 30e38f3 — updated: lib version
- 2026-05-08 — 9c718ae — fixed: pirpos batch size
- 2026-04-03 — 5038c88 — Fix/fixing lambda (#18)
- 2026-02-01 — 0cbd18f — Fix/fix invoices and iterations (#16)
- 2026-01-30 — 86b242b — Fix/fix invoices and iterations (#15)
- 2026-01-28 — 274bd86 — fixed: bad reported payments into siigo api (#14)
- 2026-01-25 — d4570c3 — updated: application description (#13)
- 2026-01-25 — 8005455 — Feature/update version (#12)
- 2026-01-25 — c4d56ab — Feature/clean arch (#11)
- 2026-01-25 — 640f1ec — Feature/clean arch (#9)

### 2025

- 2025-11-08 — 422dbb9 — uncomment lines
- 2025-09-21 — 40b2997 — updating payment methods
- 2025-08-07 — 4dee718 — updaring retentions
- 2025-05-09 — 5ace5fe — updating toml
- 2025-04-07 — 7a27577 — fix error when the invoice has a credit note
- 2025-03-18 — 540d2c7 — adding credit notes
- 2025-03-04 — 062a004 — taking into account deleted invoices

### 2024

- 2024-11-06 — 8b922e7 — updating Transferencia payment method
- 2024-11-06 — cdd085c — fix load taxes
- 2024-09-10 — 4ceb3d8 — update invoice payload when there is a product with 0 price
- 2024-08-07 — a2fa149 — update non tax products
- 2024-08-07 — 446ff4c — updating sigo and pirpos api
- 2024-05-06 — 8d5d807 — fix invoice update after error
- 2024-04-09 — b438865 — update api changes
- 2024-02-07 — 72ca2ba — updating new api parameters
- 2024-02-06 — cbfd4dd — updating new api parameters
- 2024-01-09 — b1abe03 — fix invoice values

### 2023

- 2023-12-07 — d314073 — new rent and boost invoice sending
- 2023-11-27 — 5d99be7 — add must_be_deleted invoices
- 2023-10-18 — aaeb96c — fix invoices without taxes
- 2023-05-01 — a5c4e24 — fix UTC time on pirpos, lost invoices on siigo, bad users on siigo (api user) and comparison of invoices
- 2023-04-30 — 339f43f — upload configuration
- 2023-01-17 — 2c44075 — fix clients comparison and download invoices request
- 2023-01-15 — 262cbd0 — working on CRU invoices
- 2023-01-15 — 0be208e — wokring con CRU
- 2023-01-15 — b7de723 — working on CRU invoices
- 2023-01-14 — 03fc81e — finish products CRU
- 2023-01-14 — 00a4d02 — working on products CUR
- 2023-01-10 — e18598d — finish clients CRU
- 2023-01-09 — 708c717 — finish getters for siigo and pirpos clients.
- 2023-01-09 — b7ec83d — refactory of models and configuration file.
- 2023-01-07 — cdee630 — starting siigo client
- 2023-01-07 — dae2b36 — finish pirpos client
- 2023-01-04 — 220fd74 — working pirpos poducts
- 2023-01-03 — 67d2289 — download pirpos clients

### 2022 and earlier

- 2022-12-29 — dc44de8 — refactory
- 2022-10-17 — 5165c9c — change version
- 2022-10-17 — fb5cd8e — get quantity and total per product in a range of periods
- 2022-10-02 — 3f6a919 — change versions
- 2022-10-02 — 9634fe0 — change versions
- 2022-10-02 — 355b351 — update library versions
- 2022-10-02 — 72b346a — fix none payment and delete prints
- 2022-09-27 — 25750f1 — fix none error quantity
- 2022-09-27 — 307d16d — adding pivot products-sellers
- 2022-09-27 — 024341a — working on metrics
- 2022-09-25 — c06c050 — fix import errors
- 2022-09-25 — 6e621ca — adding mypy fix
- 2022-09-04 — f792edd — fix missing search
- 2022-09-04 — ef653f1 — automatic download
- 2022-09-03 — 2a30e43 — working on automatic download
- 2022-09-01 — 5f82ceb — automatic clients download
- 2022-08-20 — 744f201 — working on refactory
- 2022-08-19 — 101e493 — adding prube.py to test code
- 2022-08-08 — dd490cc — black formatting
- 2022-08-08 — 7e20c4f — adding poetry dependencies
- 2022-07-03 — 17930ed — fixing sending invoices from a start_at invoice
- 2022-07-03 — 402e41a — saving invoice errors as .json, adding feature sending invoices from a list and sending invoices from a start_at invoice
- 2022-06-17 — 2fccf00 — fix invoice time and due_date for rappi
- 2022-06-16 — 15ac87e — dependencies
- 2022-06-16 — fa247cf — se arregla union de tablas, facturas ahora quedan ordenadas tempralemnte
- 2022-06-16 — 5caf7f2 — se mejora la preparacion de documentos y revision de documentos. Se permite cargar varios archivos para un mismo dataframe
- 2022-06-15 — 95cf32a — refactory, adding poetry
- 2022-06-15 — 48a82e6 — trabajando en excepciones, verificar archivos antes de enviar facturas
- 2022-06-15 — 309d22e — Initial commit
- 2022-05-29 — 8bde433 — se mejora la lectura de documentos usuarios antes de enviar las facturas a Siigo
- 2022-05-13 — b8e5e30 — Se crean funciones en utils.py para reducir el codigo en el archivo principal. Se crean funciones para preparar los .xls leidos, verificar la numeracion y el prefijo y los valores facturados de las facturas.
- 2022-05-03 — 3ab4f3f — creacion del repositorio
