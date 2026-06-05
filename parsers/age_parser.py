import requests
from bs4 import BeautifulSoup
from schemas import AgeTimeData, AgeTimeResult
   
def load_age_time_data() -> AgeTimeResult:
    """
    Get Age data from 4 <strong> tags

    Expected value ordering:
        1. Age name
        2. Age start date
        3. Age end date
        4. Remaining time until the age ends
        
    Empty and non-significant values are replaced for None
    This function dous not validate required fields
    
    note: Expected exactly four <strong> tags in a stable order.
    """
    # requests block excecution
    url = 'https://www.webgame.cz/'
    
    try:
        res = requests.get( url, timeout=10)
        res.raise_for_status()
        
    except requests.RequestException as error:
        return AgeTimeResult(
            ok = False, 
            errors=[f"Response from server failed with exception {error}"],
        )
    
    # find the correct data in the html file            
    soup = BeautifulSoup(res.text, "html.parser")
    theme_header = soup.find(id="theme")
    time_data = theme_header.find_all("strong")
    
    if not time_data:
        return AgeTimeResult(
            ok=False,
            errors=["No time data found in the html"],
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
    