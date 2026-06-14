from parsers.age_parser import load_age_time_data
from tests.helpers import load_fixture

def test_valid_age_page():
    
    file_text = load_fixture("age_parser_test_data/valid_age_page.html")    
    result = load_age_time_data(html=file_text)
    
    assert result.ok is True
    assert result.data is not None
    assert result.data.end == "30.06.2026 18:00"
    assert result.data.name == "Age 97"
    assert result.data.rest_time == "17 dni 6 hodin"
    assert result.data.start == "01.06.2026 18:00"
    assert result.errors == []    
    
def test_no_time_data_page():
    
    file_text = load_fixture("age_parser_test_data/no_time_data_page.html")
    result = load_age_time_data(html=file_text)
    
    assert result.ok is False
    assert "No time data found in the html" in result.errors
    assert result.data is None
    
def test_missing_theme_page():
    
    file_text = load_fixture("age_parser_test_data/missing_theme_page.html")
    result = load_age_time_data(html=file_text)
    
    assert result.ok is False
    assert "No theme ID found in the html" in result.errors
    assert result.data is None
    
def test_extra_strong_tags_age_page():
    
    file_text = load_fixture("age_parser_test_data/extra_strong_tags_age_page.html")
    result = load_age_time_data(html=file_text)
    
    assert result.ok is False
    assert "Incorrect strongs tags in the theme" in result.errors
    assert result.data is None    
    assert len(result.raw_values) == 5 
    

def test_empty_values_age_page():
        
    file_text = load_fixture("age_parser_test_data/empty_values_age_page.html")
    result = load_age_time_data(html=file_text)

    assert result.ok is True
    assert result.data is not None
    assert result.data.name is None
    assert result.data.start is None
    assert result.data.end is None
    assert result.data.rest_time is None