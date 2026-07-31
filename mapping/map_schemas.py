from dataclasses import dataclass, field

    
@dataclass(frozen=True)
class CountryIdentity:
    number: int
    name: str
    player_name: str 
    alliance: str | None
    
@dataclass(frozen=True)
class Military:
    soldiers: float # k
    tanks: float # k
    fighters: float # k
    bunkers: float # k
    mechs: float # k
    agents: int
    conventional_rackets: int
    biocid_rackets: int
    emp_rackets: int
    nuclear_rackets: int
    
@dataclass(frozen=True)
class MilitaryProperties:
    army_experiences: int # K
    rank: int
    experiences_of_age: int # K
    sanctity: int   
    
@dataclass(frozen=True)
class EconomicTechnologies:
    economic_technologies: float # K
    construction_speed: float # K 
    business: float # K
    population_density: float # K
    farming: float # K
    factory_automation: float # K
    energetics: float # k
    
@dataclass(frozen=True)
class MilitaryTechnologies:
    military_technologies: float # k
    force_of_arms: float # k
    domestic_market_price: float # k
    rocket_development: float # k
    missile_defense: float # k
    intelligence_force: float # k
    space_exploration: float # k
    
@dataclass(frozen=True)
class CountryProperties:
    country_prestige: float # k
    population: float # M
    money: float # M
    food: float # k
    energy: float # k
    satisfaction: float # %
    stored_on_the_market: float # ???
    played_rounds: int
    free_rounds: int
    inaccessible_rounds: int
    
@dataclass(frozen=True)
class Buildings:
    country_area: float # k
    villages: float # k
    cities: float # k
    business_zones: float # k
    farms: float # k
    laboratories: float # k
    factories: float # k
    barracks: float # k
    power_plants: float # k
    entertainment_centers: float # k
    military_bases: float # k
    construction_companies: int
    unbuilt: float # k
    ruins: float # k
    
dataclass(frozen=True)
class Bonuses:
    bonus_villages: int # %
    bonus_farms: int # %
    bonus_laboratories: int # %
    bonus_factories: int # %
    bonus_barracks: int # %
    bonus_power_plants: int # %
    bonus_military_bases: int # %
    bonus_money: int # %
    bonus_max_economic_technolgies: int # %
    bonus_max_military_technologies: int # %
    bonus_efekt_economy_technologies: int # %
    bonus_attak: int # %
    bonus_defense: int # %
    bonus_colonization: int # %
    bonus_wages: int # %
    
    
@dataclass(frozen=True)
class Production:
    money_increase: float # k
    food_increase: int
    energy_increase: int
    soldiers_increase: int
    parts_of_units_increase: int
    technology_increase: int
    
@dataclass(frozen=True)
class OtherProperties:
    logout: str
    start_of_developing: str | None
    last_economic_aid: str | None
    incoming_aids: int
    outcoming_aids: int
    last_humanitarian_aids: str | None
    alliance_last_message: str | None
    to_cash_register: int # %
    from_cash_register: float # M
    space_exploartion_increase: float # % 
    points_of_utopia: float # k
    proportion_of_androids: int # %
    UFO_chance: float # %
    embargo_votes: int
    operations: int


@dataclass(frozen=True)
class CountrySnapshot:
    identity: CountryIdentity  
    military: Military
    military_properties: MilitaryProperties
    economic_tech: EconomicTechnologies
    military_tech: MilitaryTechnologies
    properties: CountryProperties
    buildings: Buildings
    bonuses: Bonuses
    production: Production
    otherproperties: OtherProperties
    
    
      