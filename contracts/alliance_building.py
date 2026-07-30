from dataclasses import dataclass, fields

def alliance_countries_building(overview_data: dict, snapshot_data: list[dict]) -> list[dict]:
    """Combine country data from overview and snapshot sources. The overview_data has higher priority for writing data.

    Args:
        overview_data: Overview countries indexed by country number.
        snapshot_data: Countries parsed from the snapshot file.

    Returns:
        AllianceData containing combined country data and possible errors.
    """
    alliance = []

    for snapshot_country in snapshot_data:
        country_number = int(snapshot_country["country_number"])
        
        final_country = snapshot_country.copy()
        overview_country = overview_data.get(country_number)

        
        for field in fields(overview_country):
            final_country[field.name] = getattr(overview_country, field.name)
                            
        alliance.append(final_country)
    
    return alliance
