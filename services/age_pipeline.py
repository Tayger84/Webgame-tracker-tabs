from .loader_webpage import get_data_from_webpage
from parsers.age_parser import load_age_time_data
from validation.validation_age_structure import age_structure_validation
from schemas import AgePipelineResult, AgeTimeData, AgeTimeResult


def process_age_time(html: str) -> AgePipelineResult:
    """
    Age time data processing function

    Returns:
        AgePipelineResult: returns every error that was created during processing in dataclass format
    """
    webpage = None
    parsed_age = None
    validation_age = None
    
    webpage = get_data_from_webpage(html) # used for getting html page from public part of server touple[bool, str]
    
    if webpage[0]:
        # webpage [1] page is available there as str
        parsed_age = load_age_time_data(webpage[1])        
    
    if not webpage[0]:
        # webpage [1] error is available there
        parsed_age = AgeTimeResult(
            ok=True,
            data=AgeTimeData(
                name=None,
                start=None,
                end=None,
                rest_time=None,
            ),
            errors=webpage[1]
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
        
    return AgePipelineResult(
        ok=True,
        data=parsed_age.data,
        errors=parsed_age.errors
    )

    