from schemas import AgeTimeData
from validation.validation_age_structure import age_structure_validation

def test_age_structure_pass():
    parsed_age = AgeTimeData(
        name="188 věk",
        start="20.04.2026 - 12:00",
        end="07.06.2026 - 20:00",
        rest_time="7 dní 3 hodiny 12 minut",
    )
    
    result = age_structure_validation(parsed_age)
    
    assert result.ok is True
    assert result.errors == []
    
def test_age_stucture_failure():
    parsed_age = AgeTimeData(
        name="188 věk",
        start="20.04.2026 - 12:00",
        end=None,
        rest_time="7 dní 3 hodiny 12 minut",
    )
    
    result = age_structure_validation(parsed_age)

    assert result.ok == False
    assert "end" in result.errors[0].lower()
    
# test_age_structure_pass()
# test_age_stucture_failure()
    
    
