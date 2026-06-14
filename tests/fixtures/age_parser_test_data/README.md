# Test data for `age_parser.py`

These fixtures cover the HTML shapes that matter for `load_age_time_data`.

The current parser downloads `https://www.webgame.cz/` directly, so unit tests should mock `requests.get` and return one of these HTML files as `response.text`.

## Fixtures

- `valid_age_page.html` - normal page with exactly four `<strong>` values inside `id="theme"`.
- `empty_values_age_page.html` - values that should be converted to `None`.
- `no_time_data_page.html` - `id="theme"` exists, but there are no `<strong>` tags.
- `missing_theme_page.html` - page does not contain `id="theme"`.
- `extra_strong_tags_age_page.html` - page contains more than four `<strong>` tags.

## Notes

`missing_theme_page.html` documents a current edge case: `theme_header.find_all("strong")` raises `AttributeError` when the theme block is missing.

`extra_strong_tags_age_page.html` documents that `raw_values` can contain more values than are mapped into `AgeTimeData`.
