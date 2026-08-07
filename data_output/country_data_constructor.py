from mapping.map_schemas import CountrySnapshot, CountryIdentity, Military, MilitaryProperties, EconomicTechnologies, MilitaryTechnologies, CountryProperties, Buildings, Bonuses, Production, OtherProperties
from dataclasses import fields, is_dataclass

def build_dataclass(cls, row):
    values = {}
    
    for field in fields(cls):
        values[field.name] =  row[field.name]

    return cls(**values) 

def converting_data_to_obj(row: dict) -> CountrySnapshot:
    """function for converting data from input dictionary to objects

    Args:
        row (dict): input data from parsers

    Returns:
        CountrySnapshot: builded object with sub_object with data
    """
    return CountrySnapshot(
        identity = build_dataclass(CountryIdentity, row),
        military = build_dataclass(Military, row),
        military_properties = build_dataclass(MilitaryProperties, row),
        economic_tech = build_dataclass(EconomicTechnologies, row),
        military_tech = build_dataclass(MilitaryTechnologies, row),
        properties = build_dataclass(CountryProperties, row),
        buildings = build_dataclass(Buildings, row),
        bonuses = build_dataclass(Bonuses, row),
        production = build_dataclass(Production, row),
        otherproperties = build_dataclass(OtherProperties, row),
    )

