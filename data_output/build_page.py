from alliance_summary import build_alliance
from country_output import build_country_computations

def build_page(countries):
    
    alliance = build_alliance(countries)
    
    country = build_country_computations(countries)