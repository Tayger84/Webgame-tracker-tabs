from schemas import  AllianceOverviewData, OverviewStructureResult

def overview_structure_validation(parsed_overview_data: dict[int, AllianceOverviewData]) -> OverviewStructureResult:
    """
    The function for check is there one of data pattern is None or in the correct shape. 

    Args:
         parsed_overview_data (AllianceOverviewData)

    Returns:
        OverviewStructureResult (_type_): _description_
    """
    errors = []
    
    allowed_regimes = {"Demo", "Rep", "Dikt", "Fund", "Kom", "Feud", "Utop", "Robo", "Anar", "Tech"}
    
    for country_number, country in parsed_overview_data.items():
                
        if country.country_number is not None:
            if country.country_number != country_number:
                errors.append(f"Country number: {country_number} is not match with stored country number: {country.country_number}")
                
            if not isinstance(country.country_number, int):
                errors.append(f"Stored country number {country.country_number} is not intiger")
                
        if country.country_area is not None:
            if not country.country_area.isdigit():
                errors.append(f"Country area is not integer {country.country_number}: {country.country_area}")
        
        if country.country_prestige is not None:
            if not country.country_prestige.isdigit():
                errors.append(f"Country prestige is not integer {country.country_number}: {country.country_prestige}")
                
        if country.regime is not None:
            if not country.regime in allowed_regimes:
                errors.append(f"Incorrect regime that was never defined {country.country_number}: {country.regime}")
                
        print(country_number, country, errors)
    return OverviewStructureResult(
        ok=len(errors)==0,
        errors=errors
    )
            

                         
    

    
   
   

    #         country = AllianceOverviewData(
    #         alliance_name=alliance_name,
    #         country_name=name,
    #         country_number=number,
    #         player_name=country_text[3].lstrip("- "),
    #         country_area=country_text[4],
    #         country_prestige=country_text[6],
    #         regime=country_text[8],            
    #     )
        
    #     countries[number] = country

    # return AllianceOverviewResult(
    #    ok=len(errors)==0,
    #    data=countries,
    #    errors=errors
    # )
    
