import requests

def get_data_from_webpage(url: [str]) -> str:
     
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        
    except requests.RequestException as error:
        return  f"Response from server failed with exception {error}"
        
    return res