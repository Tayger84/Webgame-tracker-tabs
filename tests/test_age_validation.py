import pytest

from tests.helpers import load_json_fixture
from validation.validation_age_structure import age_structure_validation
from schemas import AgeTimeData

CASES = load_json_fixture("age_validation_test_data/age_structure_validation_cases.json")


@pytest.mark.parametrize("case_name, case", CASES.items(), ids=CASES.keys())
def test_age_validation(case_name, case):
    input_data = case["input"]
    expected_data = case["expected"]
    
    for_test_data = AgeTimeData(**input_data)
    
    result = age_structure_validation(for_test_data)
    
    assert result.ok is expected_data["ok"]
    assert result.errors == expected_data["errors"]