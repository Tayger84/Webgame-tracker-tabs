# Alliance overview parser fixtures

Parser is intentionally left unchanged. These fixtures target the exact input shape expected by `load_alliance_overview_data`.

| File | What it tests | Expected parser behavior | Type |
| --- | --- | --- | --- |
| `overview_valid_minimal.html` | Minimal valid alliance page with two country rows. | `ok=True`, two countries in `data`, no errors. | Common case |
| `overview_missing_bonus_header.html` | Missing `h2` containing the exact text `Alianční bonusy`. | `ok=False`, error `Incorrect page for parsing, Alliance Overview is necessary`. | Edge case |
| `overview_missing_h1.html` | Bonus header exists, but alliance name `<h1>` is absent. | `ok=False`, error `The Alliance name header was not able to find on the page`. | Edge case |
| `overview_missing_alliance_table.html` | Alliance name exists, but there is no following table. | `ok=False`, error `No find an Alliance table on the page`. | Edge case |
| `overview_corrupted_short_row.html` | Country row has an `<a>` but too few text tokens after splitting. | `ok=False`, error starting `Invalid row structure`. | Edge case |
| `overview_missing_values_empty_strings.html` | Required positions exist, but player, area, prestige and regime are placeholder/empty-like values. | Current parser accepts the row: `ok=True`; fields contain empty string or `-`. | RISK |
| `overview_bad_country_number_format.html` | Country text has non-numeric `#ABC` and another row without the `(#` marker. | `ok=False`, errors starting `Invalid country name/number format`; no valid countries. | Edge case | result: ['Invalid country name/number format: Alpha land(#ABC)', 'Invalid country name/number format: Beta land #102']
| `overview_empty_data_no_country_rows.html` | Alliance table contains no rows with `<a>`. | Current parser returns `ok=True`, empty `data`, no errors. | RISK |
| `overview_duplicate_country_numbers.html` | Two rows resolve to the same country number. | `ok=False`, first country is kept, duplicate row adds `Duplicate country number in the countries: 101`. | Edge case |
| `overview_extra_data_ignored.html` | Valid row contains extra columns and another later table with links. | Current parser returns `ok=True`; extra fields and later table are ignored. | Common case |
| `overview_risk_wrong_table_after_h1.html` | First table after `<h1>` is a layout/menu table, while real data is in the next table. | Current parser reads the wrong table, returns `ok=False` with `Invalid row structure`; real table is ignored. | RISK |
| `overview_risk_unexpected_link_text_in_country_cell.html` | Country cell has a text-producing mail link before the country link. | Current parser treats `Mail` as `country_text[2]`, returns `ok=False` with invalid country name/number format. | RISK |
