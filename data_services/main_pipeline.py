from loader_webpage import get_data_from_webpage
from overview_pipeline import load_alliance_overview_data
from snapshot_pipeline import load_alliance_snapshot_data

from schemas import LoadCountryData

def load_main_pipeline(overview__html_data: str, snapshot_html_data: str) -> LoadCountryData:
    """Final load pipeline for the loading Alliance Overview, Snapshost and present Age data

    Args:
        overview__html_data (str): input data in html string format for parsing process
        snapshot_html_data (str): input data in html string format for parsing process

    Returns:
        LoadCountryData: _description_
    """
    
    
    overivew_data = load_alliance_overview_data(overview__html_data)
    snapshot_data = load_alliance_snapshot_data(snapshot_html_data)
    
    