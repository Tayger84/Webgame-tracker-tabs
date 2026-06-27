from validation.validation_overview import overview_structer_validation
from parsers.overview import load_alliance_overview_data
from pathlib import Path

DATA_URL = Path(__file__).parents[1] / "tests" / "fixtures" / "overview_parser_test_data" / "original_NTRLTY_aliance.html"

html = DATA_URL.read_text(encoding="utf-8")

parser_result = load_alliance_overview_data(html)

validation_result = overview_structer_validation(parser_result.data)






