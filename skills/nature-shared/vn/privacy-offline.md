# Privacy and Offline Rules for Clinical Research Material

Shared by every `exa-*` skill. Load before reading any dataset, case report, image, or
unpublished manuscript.

## 1. What never leaves the machine

- Unpublished manuscript text, figures, tables, and supplementary files
- Raw or processed research data
- Ethics applications, approval letters, consent forms
- Reviewer and editor correspondence
- Any patient-level information

Remote services may receive only public identifiers (DOI, PMID, arXiv ID) and search terms.
Never paste manuscript passages into a search query.

## 2. Identifier screen (run before analysis)

Check every dataset, table, image, and case description for:

| Identifier | Examples |
|---|---|
| Name or initials with other details | patient name, "BN Nguyễn V. A." |
| Exact dates tied to a person | date of birth, admission, discharge, death |
| Government or hospital numbers | national ID (CCCD), health-insurance number (BHYT), medical record number (mã hồ sơ bệnh án) |
| Contact or location | phone, email, street address, commune-level residence |
| Images | full-face photos, identifiable tattoos, DICOM headers with patient fields |
| Free text | clinical notes that name relatives, workplaces, or rare events |

If any identifier is present:

1. Stop and tell the user which columns or passages contain identifiers.
2. Offer to work only with aggregated values, or ask the user to supply a de-identified file.
3. Never copy identifiers into generated files, logs, or examples.

Age in years, sex, province, and year-level dates are usually acceptable for analysis, but
small cells (fewer than 5 individuals) in a table can still re-identify patients: flag them.

## 3. Case reports and images

Case reports and clinical images need documented patient consent for publication. Ask whether
consent exists before drafting; if not, mark `[CẦN BỔ SUNG: giấy đồng ý công bố của bệnh nhân]`.

## 4. Generated files

Save outputs only inside the user's project folder or a path the user names. Do not write to
cloud-synced folders unless the user chooses them.
