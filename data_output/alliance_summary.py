def alliance_summary_data(countries):
    country_table = []
    
    country_counter = len(countries)
    alliance_name = countries[0].identity.alliance_name
    
    for country in countries:
        country_table.append({
            "country_number": country.identity.country_number,
            "country_name": country.identity.country_name,
            "player_name": country.identity.player_name, 
        })
        
    extended_data = (alliance_name, country_counter)
        
    return country_table, extended_data
