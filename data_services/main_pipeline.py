from data_services.loader_webpage import get_data_from_webpage
from data_services.overview_pipeline import load_alliance_overview_data
from data_services.snapshot_pipeline import load_alliance_snapshot_data
from contracts.snapshot_translation import snapshot_keys_translation
from contracts.alliance_building import alliance_countries_building

from schemas import LoadCountryData

def load_main_pipeline(overview_html_data: str, snapshot_html_data: str) -> LoadCountryData:
    """Final load pipeline for the loading Alliance Overview, Snapshost and present Age data

    Args:
        overview__html_data (str): input data in html string format for parsing process
        snapshot_html_data (str): input data in html string format for parsing process

    Returns:
        LoadCountryData: _description_
    """
    
    
    overivew_data = load_alliance_overview_data(overview_html_data)
    snapshot_data = load_alliance_snapshot_data(snapshot_html_data)
    
    if overivew_data.ok == False:
        return LoadCountryData(
            ok=False,
            erorrs=["Something wrong happened during overview parsing process: "] + overivew_data.errors
        )
        
    if snapshot_data.ok == False:
        return LoadCountryData(
            ok=False,
            erorrs=["Something wrong happened during overview parsing process: "] + snapshot_data.errors
        )
    
    # check if both files contents the same countries    
    overview_countries_numbers = list(overivew_data.data.keys())
    snapshot_countries_numbers = list(snapshot_data.data.country_numbers)
    
    if overview_countries_numbers != snapshot_countries_numbers:
        return LoadCountryData(
            ok=False,
            erorrs=["Different countries numbers in files: "] + overview_countries_numbers + snapshot_countries_numbers
        )
        
    snapshot_data_after_translation = snapshot_keys_translation(snapshot_data.data.snapshot_data)
    
    if snapshot_data_after_translation == None:
        return LoadCountryData(
            ok=False,
            erorrs=["The failure observed during snapshot keys translation"]
        )
    
    built_alliance = alliance_countries_building(overivew_data.data, snapshot_data_after_translation)
    
    