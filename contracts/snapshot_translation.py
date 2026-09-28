from contracts.snapshot import SNAPSHOT_METRIC_MAP

def snapshot_keys_translation(snapshot_data_to_translation: list[dict]):
    
    return [
       normalize_country(country) for country in snapshot_data_to_translation
    ]
    
    
def normalize_country(raw_country: dict) -> dict:
    
    normalized_country = {}
    
    for source_key, value in raw_country.items():
        try:
            normalized_key = SNAPSHOT_METRIC_MAP[source_key]
        except KeyError:
            raise KeyError(
                f'Chybí překlad klíče {source_key!r}'
            )
    
        normalized_country[normalized_key] = value

    return normalized_country    
    


    
