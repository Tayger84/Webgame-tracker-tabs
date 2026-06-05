from parsers.age_parser import load_age_time_data
from validation.validation_age_structure import age_structure_validation
from schemas import AgePipelineResult


def process_age_time() -> AgePipelineResult:
    """
    Age time data processing function

    Returns:
        AgePipelineResult: returns every error that was created during processing in dataclass format
    """
    parsed_age = None
    validation_age = None
    
    parsed_age = load_age_time_data()
    
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
        
    return AgePipelineResult(
        ok=True,
        data=parsed_age.data,
        errors=[]
    )

    