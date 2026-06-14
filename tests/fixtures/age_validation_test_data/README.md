# Test data for `validation_age_structure.py`

This folder contains data-only validation cases for `age_structure_validation(parsed_age)`.

The validator expects an `AgeTimeData` object with these fields:

- `name`
- `start`
- `end`
- `rest_time`

Use `age_structure_validation_cases.json` as source data when writing tests later. Each case has:

- `input` - values to pass into `AgeTimeData`
- `expected` - expected `AgeStructureResult.ok` and `AgeStructureResult.errors`

## Important notes

The strings intentionally use the same mojibake text currently present in the validator regex patterns:

- `vÄ›k`
- `VÄ›k`
- `dnĂ­`

That means these fixtures match the validator exactly as it exists now, without changing the validation file.

The `invalid_rest_time_singular_hour_not_supported` case documents current behavior: `hodina` and `minuta` are not accepted by the current regex, while `hodiny`, `hodin`, `minuty`, and `minut` are accepted.
