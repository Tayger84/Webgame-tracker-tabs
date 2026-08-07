from data_output.country_data_constructor import converting_data_to_obj

def get_data_for_processing(data):
    list_of_alliance_countries = []
    
    for country in data:
        list_of_alliance_countries.append(converting_data_to_obj(country))

    return list_of_alliance_countries