from bs4 import BeautifulSoup
from schemas import AllianceSnapshotResult, AllianceSnapshotData

def load_alliance_snapshot_data(html) -> AllianceSnapshotResult:
    """
    Get Alliance Snapshot data include based on country number for serialization with overview

    Args:
        html file that should be loaded from user

    Returns:
        AllianceSnapshotResult: Dataclass for sharing information with main function
    """
    parsed_keys = []
    country_numbers = []
    
    # find the HTML content for parsing
    soup = BeautifulSoup(html, 'html.parser')
    
    # find the header for check correct page 
    header = soup.find(['h1', 'h2', 'h3'], string=lambda t: t and "Detaily zemí aliance" in t) # find first "Detaily zemí aliance" in tag regadless on other characters
    
    if not header:
        return AllianceSnapshotResult(
            ok=False,
            errors=["Incorrect html file or webpage"]
        )
        
    # find first table after header "Detaily zemí aliance"
    table = header.find_next("table")
    if not table:
        return AllianceSnapshotResult(
            ok=False,
            errors=["Tag <table> was not found on the imported webpage"]
        )
        
    rows = table.find_all("tr")
    if not rows:
        return AllianceSnapshotResult(
            ok=False,
            errors=["Found no rows in the table"]
        )
        
    # get info how many countries according storaged td in cells
    first_row_cells = rows[0].find_all("td")
    if not first_row_cells or len(first_row_cells) < 2:
        return AllianceSnapshotResult(
            ok=False,
            errors=["Incorrect count of the countries in the Snapshot"]
        )
        
    # how many countries and cells are there? 
    expected_cell_count = len(first_row_cells)
    num_countries = expected_cell_count - 1 
     
    # create template for country list(dict{})
    countries = [ {} for _ in range(num_countries) ]
    
    
    # fill rows in the cell in dictionary 
    for row in rows:
        cells = [ c.get_text(strip=True) for c in row.find_all("td") ]
        
        if not cells:
            return AllianceSnapshotResult(
                ok=False,
                errors=[f"No strings were found in the country data for the country template"]
            )
            
        if len(cells) != expected_cell_count:
            return AllianceSnapshotResult(
                ok=False,
                errors=[f"Expected {expected_cell_count}, got {len(cells)}. Row {cells}"]
            )
        
        # header of the property of every country   
        metric_name = cells[0]
        parsed_keys.append(metric_name) # parsed keys for validation snapshot structure
        
        # fill countries via metric_name and cells values
        for i in range(1, len(cells)): # len(cells) countries in the every row
            if metric_name == 'Číslo':
                if cells[i].isdigit():
                    country_numbers.append(int(cells[i]))
                else:
                    return AllianceSnapshotResult(
                        ok=False,
                        errors=[f"Invalid country number format: {cells[i]}"],
                        )
            countries[i-1][metric_name] = cells[i] # duplicity matric_name - in this case the value is stored again in the same key 

    if num_countries != len(country_numbers):
        return AllianceSnapshotResult(
            ok=False,
            errors=[
                f"Invalid count of country numbers. " 
                f"Expected: {num_countries}, got {len(country_numbers)}. "
                f"Country numbers: {country_numbers}"
                ]
        )
            
    return AllianceSnapshotResult(
        ok=True,
        data=AllianceSnapshotData(
            country_numbers=country_numbers,
            parsed_keys=parsed_keys,
            snapshot_data=countries,
        )
    )
