from contracts.snapshot import SNAPSHOT_METRIC_MAP

def snapshot_keys_translation(snapshot_data_to_translation: list[dict]):
    
    modified_countries = []
    
    for country in snapshot_data_to_translation:
        for old_key, new_key in SNAPSHOT_METRIC_MAP.items():
            if old_key in country:
                country[new_key] = country.pop(old_key)
        modified_countries.append(country)
        
    return modified_countries
    
