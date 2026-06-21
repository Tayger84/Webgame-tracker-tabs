# Test data for `services/age_pipeline.py`

This folder contains data only. It does not contain tests and does not modify the pipeline.

`pipeline_cases.json` describes scenarios for `process_age_time()` with mocked pipeline steps:

- `get_data_from_webpage`
- `load_age_time_data`
- `age_structure_validation`

Each case contains:

- `description` - what the scenario covers
- `mocked_steps` - values that can be returned by mocked dependencies later
- `expected_pipeline_result` - expected `AgePipelineResult` shape

## HTML fixtures

- `webpage_valid_age.html` - valid HTML for a successful parser and validator path
- `webpage_invalid_validation_age.html` - parser-readable HTML with invalid values for validation
- `webpage_empty_age_values.html` - parser-readable HTML where empty values become `None`

## Current behavior documented

`webpage_download_failed_current_behavior` intentionally documents the current pipeline behavior:

When `get_data_from_webpage(URL)` returns `false`, the pipeline creates an `AgeTimeResult` with empty `AgeTimeData`. Because the validator accepts `None` values, the final pipeline result is currently `ok=true`.

The expected `errors` value in that case is a string, because the current pipeline assigns `errors=webpage[1]` directly.
