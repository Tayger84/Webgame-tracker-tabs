from pathlib import Path
from parsers.overview import load_alliance_overview_data

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" # fixtures folder

def load_fixture(filename: str) -> str:
    html_test_file = FIXTURE_DIR / filename
    return html_test_file.read_text(encoding="utf-8")

def test_valid_input():
    
    file_text = load_fixture("original_NTRLTY_aliance.html")    
    result = load_alliance_overview_data(html=file_text)
    
    assert result.ok is True
    assert result.errors == []
    
    for data in result.data.items():
        print(data, end=" ")


def test_overview_bad_country_number_format():
    
    file_text = load_fixture("overview_bad_country_number_format.html")    
    result = load_alliance_overview_data(html=file_text)
    
    assert result.ok is False
    assert len(result.errors) >= 1
    assert any("country name/number" in error.lower() for error in result.errors)
    print(result.errors)
    
def test_overview_corrupted_short_row():
    pass
    

# test_valid_input()
test_overview_bad_country_number_format()