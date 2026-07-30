from data_services.overview_pipeline import load_alliance_overview_data
from data_services.snapshot_pipeline import load_alliance_snapshot_data
from contracts.snapshot_translation import snapshot_keys_translation
from contracts.alliance_building import alliance_countries_building

from schemas import LoadCountryData

def load_main_pipeline(overview_html_data: str, snapshot_html_data: str) -> LoadCountryData:
    """Final load pipeline for the loading Alliance Overview, Snapshost. Check if the files relate together. Main Alliance list creation.

    Args:
        overview__html_data (str): input data in html string format for parsing process
        snapshot_html_data (str): input data in html string format for parsing process

    Returns:
        LoadCountryData: _description_
    """
    
    
    overview_data = load_alliance_overview_data(overview_html_data)
    snapshot_data = load_alliance_snapshot_data(snapshot_html_data)
    
    # check if data are prepared for next processing
    if not overview_data.ok:
        return LoadCountryData(
            ok=False,
            erorrs=["Something wrong happened during overview parsing process: "] + overview_data.errors
        )
        
    if not snapshot_data.ok:
        return LoadCountryData(
            ok=False,
            erorrs=["Something wrong happened during overview parsing process: "] + snapshot_data.errors
        )
    
    # check if both files contents the same countries numbers    
    overview_countries_numbers = set(overview_data.data.keys())
    snapshot_countries_numbers = set(snapshot_data.data.country_numbers)
    
    if overview_countries_numbers != snapshot_countries_numbers:
        return LoadCountryData(
            ok=False,
            erorrs=[f"Different countries numbers in files: overview numbers - {overview_countries_numbers}, snapshot numbers - {snapshot_countries_numbers}"]
        )
    
    # all numbers are the same keys translation is in progress    
    snapshot_data_after_translation = snapshot_keys_translation(snapshot_data.data.snapshot_data)
    
    # time for alliance building
    builded_alliance = alliance_countries_building(overview_data.data, snapshot_data_after_translation)
    
    return LoadCountryData(
        ok=True,
        countries_final_data=builded_alliance,
        erorrs=[],
    )
    
    