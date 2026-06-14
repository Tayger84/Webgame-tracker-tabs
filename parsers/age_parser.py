from bs4 import BeautifulSoup
from schemas import AgeTimeData, AgeTimeResult
   
def load_age_time_data(html: str) -> AgeTimeResult:
    """
    Get Age data from 4 <strong> tags on the webgame.cz

    Expected value ordering:
        1. Age name
        2. Age start date
        3. Age end date
        4. Remaining time until the age ends
        
    Empty and non-significant values are replaced for None
    This function dous not validate required fields
    
    note: Expected exactly four <strong> tags in a stable order.
    """
            
    # find the correct data in the html file            
    soup = BeautifulSoup(html, "html.parser")
    theme_header = soup.find(id="theme")
    
    if not theme_header:
        return AgeTimeResult(
            ok=False,
            errors= ["No theme ID found in the html"],
        )
    
    time_data = theme_header.find_all("strong")
   
    if not time_data:
        return AgeTimeResult(
            ok=False,
            errors=["No time data found in the html"],
        )
        
    if len(time_data) != 4:
        return AgeTimeResult(
            ok=False,
            errors=["Incorrect strongs tags in the theme"],
            raw_values=time_data,
        )
        
    
    raw_t_data = [ data.get_text(strip=True) for data in time_data ]
    
    # check None data present between <strong> tags
    empty_values = ("", ".", "_", ",", "-", "none", "null")    
    t_data = []
    
    for value in raw_t_data:
        
        if value.lower() in empty_values:
            t_data.append(None)
        else:
            t_data.append(value)
    
    # return object of data
    return AgeTimeResult(
        ok=True,
        data=AgeTimeData(
            name=t_data[0],
            start=t_data[1],
            end=t_data[2],
            rest_time=t_data[3]
        ),
        errors=[],
        raw_values=t_data,
    )
    