from schemas import AllianceData

def alliance_countries_building(overview_data, snapshot_data) -> AllianceData:

    for snapshot_country in snapshot_data:
        # get every country in the snapshot
        number = snapshot_country["number"]
        if number.isdigit():
            number = int(number)
            
        # get the same country from the overview    
        overivew_country = overview_data[number]
        
        for country in overview_data[number]:
            pass
