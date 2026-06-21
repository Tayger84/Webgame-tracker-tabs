from services.age_pipeline import process_age_time
from tests.helpers import load_fixture, load_json_fixture

CASES = load_json_fixture("age_pipeline_test_data/pipeline_cases.html")

def test_webpage_valid_age():
    
    html_str = load_fixture("age_pipeline_test_data/webpage_valid_age.html")

    result = process_age_time(html_str)
    
    assert result.ok is True
    assert result.data.name == "97. věk"
    assert result.data.start == "01.06.2026 - 18:00"
    assert result.data.end == "30.06.2026 - 18:00"
    assert result.data.rest_time == "17 dní 6 hodin 30 minut"
    assert result.errors == []
    
def test_webpage_invalid_validation_age():
    
    html_str = load_fixture("age_pipeline_test_data/webpage_invalid_validation_age.html")
    
    result = process_age_time(html_str)
    
    assert result.ok is False
    assert "Missing/Incorrect Age name" in result.errors

def test_webgame_empty_age_values():
    
    
    html_str = load_fixture("age_pipeline_test_data/webpage_empty_age_values.html")
    
    result = process_age_time(html_str)
    
    assert result.ok is True
    assert result.data.name == None
    assert result.data.start == None
    assert result.data.end == None
    assert result.data.rest_time == None
    assert result.errors == []
    
