from tests.helpers import load_fixture
from parsers.overview import load_alliance_overview_data

def test_valid_input():
    
    file_text = load_fixture("overview_parser_test_data/original_NTRLTY_aliance.html")    
    result = load_alliance_overview_data(html=file_text)
    
    assert result.ok is True
    assert result.errors == []
    
    for data in result.data.items():
        print(data, end=" ")


def test_overview_bad_country_number_format():
    
    file_text = load_fixture("overview_parser_test_data/overview_bad_country_number_format.html")    
    result = load_alliance_overview_data(html=file_text)
    
    assert result.ok is False
    assert len(result.errors) >= 1
    assert any("country name/number" in error.lower() for error in result.errors)
    print(result.errors)
    
def test_overview_corrupted_short_row():
    file_text = load_fixture("overview_parser_test_data/overview_corrupted_short_row.html")    
    result = load_alliance_overview_data(html=file_text)
    
    assert result.ok is False
    assert len(result.errors) > 0
    

