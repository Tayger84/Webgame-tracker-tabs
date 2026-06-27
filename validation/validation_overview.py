from schemas import  AllianceOverviewData, OverviewStructureResult

def overview_structer_validation(parsed_overview_data: AllianceOverviewData) -> OverviewStructureResult:
    """
    The function for check is there one of data pattern is None or in the correct shape. 

    Args:
         parsed_overview_data (AllianceOverviewData)

    Returns:
        OverviewStructureResult (_type_): _description_
    """
    errors = []
    nones = 0
    
    for country_number in parsed_overview_data.keys():
        pass
    

    
   
   

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
    
