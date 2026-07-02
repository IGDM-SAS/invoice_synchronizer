# Changelog

All notable changes to this project are documented in this file.

The format follows "Keep a Changelog" (https://keepachangelog.com/) and the
project follows Semantic Versioning (https://semver.org/).

This changelog was reconstructed from the repository git history and grouped by release tags.

## [Unreleased]

- No unreleased changes recorded.

## Releases


### [3.1.2] - 2026-07-02

#### Added

- Add `equals_soft` to `Invoice` for percentage-based tolerance comparison of totals and taxes. (68422f2)
- Added a fallback method to get a client if it is not present when parsing loggro invoices. (289d197)

#### Changed

- Subtract 5 hours when parsing `createdOn`/`modifiedOn` from Pirpos to align with UTC-5. (68422f2)
- Format invoice summaries as a table and display totals with dot thousands and comma decimals. (c2a3811)


### [3.1.1] - 2026-05-08

- Merge pull request #22 from IGDM-SAS/fix/update_version (6947932)
- updated: lib version (30e38f3)
- Merge pull request #21 from IGDM-SAS/release/3.1.1 (ff84a90)
- Merge pull request #20 from IGDM-SAS/fix/pirpos_batch_size (0fcd2f9)
- fixed: pirpos batch size (9c718ae)

### [3.1.0] - 2026-04-03

- Merge pull request #19 from jueshebe/develop (c736b54)
- Fix/fixing lambda (#18) (5038c88)
- Fix/fix invoices and iterations (#16) (0cbd18f)
- Fix/fix invoices and iterations (#15) (86b242b)
- fixed: bad reported payments into siigo api (#14) (274bd86)

### [3.0.0] - 2026-01-25

- updated: application description (#13) (d4570c3)
- Feature/update version (#12) (8005455)
- Feature/clean arch (#11) (c4d56ab)
- Feature/clean arch (#9) (640f1ec)

### [2.0.1] - 2023-05-01

- fix UTC time on pirpos, lost invoices on siigo, bad users on siigo (api user) and comparison of invoices (a5c4e24)
- upload configuration (339f43f)
- fix clients comparison and download invoices request (2c44075)
- working on CRU invoices and related changes (262cbd0, 0be208e, b7de723, 03fc81e, 00a4d02, e18598d)
- finish getters for siigo and pirpos clients, start clients/work (708c717, b7ec83d, cdee630, dae2b36, 220fd74, 67d2289)

### [2.0.0] - 2022-09-04

- fix missing search, automatic download and automatic clients download (f792edd, ef653f1, 2a30e43, 5f82ceb)
- working on refactorings, metrics and dependency updates (744f201, 101e493, dd490cc, 7e20c4f, 355b351)

### [1.0.0] - 2022-06-17

- Initial release (2fccf00)

Notes

- This changelog was generated from git tags and commit history. For more granular details, check the commit history between tags.
