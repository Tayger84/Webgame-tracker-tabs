import requests
from dataclasses import dataclass, field
from bs4 import BeautifulSoup

@dataclass(frozen=True)
class AgeTimeData:
    name: str | None = None
    start: str | None = None
    end: str | None = None
    rest_time: str | None = None
    
@dataclass(frozen=True)
class AgeTimeResult:
    ok: bool
    data: AgeTimeData | None = None
    errors: list[str] = field(default_factory=list)
    raw_values: list[str] = field(default_factory=list)
    
def load_age_time_data() -> AgeTimeData | None:
    
    url = 'https://www.webgame.cz/'
    
    try:
        res = requests.get( url, timeout=10)
        res.raise_for_status()
        
    except requests.RequestException as error:
        return AgeTimeResult(
            ok = False, 
            errors=[f"Response from server failed with exception {error}"],
        )
                
    soup = BeautifulSoup(res.text, "html.parser")
    theme_header = soup.find(id="theme")
    time_data = theme_header.find_all("strong")
    
    if not time_data:
        return AgeTimeResult(
            ok=False,
            errors=["No time data found in the html"],
        )
    
    raw_t_data = [ data.get_text(strip=True) for data in time_data ]
    
    empty_values = ("", ".", "_", ",", "-", "none", "null")    
    t_data = []
    
    for value in raw_t_data:
        
        if value.lower() in empty_values:
            t_data.append(None)
        else:
            t_data.append(value)
    
    if len(t_data) != 4:
        return AgeTimeResult(
            ok=False,
            errors=[f"Some time data was not found in the parser. Found {len(t_data)} values only"],
            raw_values=t_data,
        )
  
    return AgeTimeResult(
        ok=True,
        data=AgeTimeData(
        name=t_data[0],
        start=t_data[1],
        end=t_data[2],
        rest_time=t_data[3]
        ),
        raw_values=t_data,
    )
