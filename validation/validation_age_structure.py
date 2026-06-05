import re
from schemas import AgeTimeData, AgeStructureResult

def age_structure_validation(parsed_age: AgeTimeData) -> AgeStructureResult:
    """
    The function for check is there one of data pattern is None or in the correct shape. 

    Args:
        parsed_age (AgeTimeData)

    Returns:
        AgeStructureResult: _description_
    """
    
    errors = []
    
    name = parsed_age.name
    start = parsed_age.start
    end = parsed_age.end
    rest_time = parsed_age.rest_time
    
    NAME_PATTERN = r"\d+\.?\s+(?:věk|Věk)"
    START_END_PATTERN = r"\d{2}\.\d{2}\.\d{4} - \d{2}:\d{2}"
    REST_TIME_PATTERN = r"\d+\s+(?:dní|den)\s+\d+\s+(?:hodin|hodiny)\s+\d+\s+(?:minut|minuty)"
    

    if name is None or re.fullmatch(NAME_PATTERN, name, flags=re.IGNORECASE) is None:
        errors.append(f"Missing/Incorrect Age name")
    
    if start is None or re.fullmatch(START_END_PATTERN, start) is None:
        errors.append("Missing/Incorrect Age start")
    
    if end is None or re.fullmatch(START_END_PATTERN, end) is None:
        errors.append("Missing/Incorrect age end")
    
    if rest_time is None or re.fullmatch(REST_TIME_PATTERN, rest_time) is None:
        errors.append("Missing/Incorrect Age rest time")
        
 
    return AgeStructureResult(
        ok=not errors,
        errors=errors,
    )