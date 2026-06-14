from parsers.age_parser import load_age_time_data
from services.age_pipeline import process_age_time
from validation.validation_age_structure import age_structure_validation
from schemas import AgePipelineResult, AgeTimeData, AgeStructureResult, AgeTimeResult

def test_process_age_time_pass():

    result = process_age_time()
    
    assert result.ok is True
    assert result.errors == []
    print(result.data)
    
def test_process_age_time_none_failure_data():
    
    parsed_age = AgeTimeResult(
        ok=True,
        data=AgeTimeData(
            name="188 a věk",
            start="20.04.2026 - 12:00",
            end="07.06.2026 - 20:00",
            rest_time="7 dní 3 hodiny 12 minut",
    ),
        errors=[],
    )
    
    validation_age = AgeStructureResult(
        ok=True,
        errors=[],        
    )
    
    if not parsed_age.ok:
        return AgePipelineResult(
            ok=False,
            errors=["The parsing process failed."] + parsed_age.errors,
        )
        
    validation_age = age_structure_validation(parsed_age.data)
    
    if not validation_age.ok:
        return AgePipelineResult(
            ok=False,
            errors=[f"The validation process failed"] + validation_age.errors
        )
        
    result = AgePipelineResult(
        ok=True,
        data=parsed_age.data,
        errors=[]
    )
    
    assert result.ok is False
    assert bool(result.data) == False
    assert bool(result.errors) == True



# assert result.ok ==True
# assert bool(result.data) == True
# assert result.errors == []

