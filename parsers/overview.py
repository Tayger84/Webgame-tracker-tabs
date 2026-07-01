from bs4 import BeautifulSoup
from schemas import AllianceOverviewData, AllianceOverviewResult


def load_alliance_overview_data(html) -> AllianceOverviewResult:
    """
    Get Alliance Overview data for full country and player name and the regime of every country

    Args:
        html file that should be loaded from user

    Returns:
        AllianceOverviewResult: Dataclass for sharing information with main function
    """
    # find the correct data in the html file
    soup = BeautifulSoup(html, "html.parser") 
    
    # simple checking of correct file
    header = soup.find('h2', string=lambda t: t and "Alianční bonusy" in t) # if Alianční bonusy are present, almost full page should be present
    
    if not header:
        return AllianceOverviewResult(
            ok=False,
            errors=["Incorrect page for parsing, Alliance Overview is necessary"],
        )
        
    # get a aliance name header and its name
    alliance_name_header = soup.find("h1")
    
    if not alliance_name_header:
        return AllianceOverviewResult(
            ok=False,
            errors=["The Alliance name header was not able to find on the page"]
        )
        
    alliance_name = alliance_name_header.get_text(strip=True)
    
    # get correct ali table without <th> headers
    alliance_table = alliance_name_header.find_next("table")
    
    if not alliance_table:
        return AllianceOverviewResult(
            ok=False,
            errors=["No find an Alliance table on the page"]
        )
    
    rows = [ tr for tr in alliance_table.find_all("tr") if tr.find("a") ] # <tr><td><a>    

    countries: dict[int, AllianceOverviewData] = {}
    errors: list[str] = []

    for row in rows:
        country_text = row.get_text("|", strip=True).split("|")
        
        if len(country_text) < 9:
            errors.append(f"Invalid row structure: {country_text}")
            continue
               
        try:    
            name, number = country_text[2].split("(#", 1)
            number = int(number.rstrip(")").strip())
        except ValueError:
            errors.append(f"Invalid country name/number format: {country_text[2]}")
            continue
        
        if number in countries:
            errors.append(f"Duplicate country number in the countries: {number}")
            continue
        
        country = AllianceOverviewData(
            alliance_name=alliance_name,
            country_name=name,
            country_number=number,
            player_name=country_text[3].lstrip("- "),
            country_area=country_text[4].rstrip("km"),
            country_prestige=country_text[6],
            regime=country_text[8],            
        )
        
        countries[number] = country

    return AllianceOverviewResult(
       ok=len(errors)==0,
       data=countries,
       errors=errors
    )


