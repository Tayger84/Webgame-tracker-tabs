import requests
from pathlib import Path

def get_data_from_webpage(url_file: str | Path) -> tuple[bool, str]:
    """
    The function for get time data for parser in HTML

    Args:
        url (str): WEBPAGE_URL

    Returns:
        tuple[bool, str]: first test if the webpage is in str or error
    """
    if url_file.startswith('http://') or url_file.startswith('https://'):         
        try:
            res = requests.get(url_file, timeout=10)
            res.raise_for_status()
            return True, res.text
            
        except requests.RequestException as error:
            return False, f"Response from server failed with exception {error}"
    
    return True, url_file
   