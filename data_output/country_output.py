
def build_country_identity(countries):
    rows = []
    
    for country in countries:
        country_name = country.identity.country_name
        country_number = country.identity.country_number
        player_name = country.identity.player_name
        alliance_name = country.identity.alliance_name

        rows.append({
            "country_name": country_name,
            "country_number": country_number,
            "player_name": player_name,
            "alliance_name": alliance_name,
        })

    return {
        "alliance_name": alliance_name,
        "rows": rows,
    }

def build_military_breakdown(countries):
    rows = []
    
    total_soldiers = 0
    total_tanks = 0
    total_fighters = 0
    total_bunkers = 0
    total_mechs = 0
    
    for country in countries:
        soldiers = country.military.soldiers
        tanks = country.military.tanks
        fighters = country.military.fighters
        bunkers = country.military.bunkers
        mechs = country.military.mechs
        
        total_soldiers += soldiers
        total_tanks += tanks
        total_fighters += fighters
        total_bunkers += bunkers
        total_mechs += mechs
                       
        rows.append({
            "country_name":country.identity.country_name,
            "country_number": country.identity.country_number,
            "soldiers":soldiers,
            "tanks":tanks,
            "fighters":fighters,
            "bunkers":bunkers,
            "mechs":mechs,
            })
        
    return {
        "total_soldiers": total_soldiers,
        "total_tanks": total_tanks,
        "total_fighters": total_fighters,
        "total_bunkers": total_bunkers,
        "total_mechs": total_mechs,
        "rows": rows,        
    }
    
def build_military_properties(countries):
    rows = []
    country_count = len(countries)
    total_exps = 0
    total_rounds = 0
    
    rank_limits = {
        "1.": (0, 10),
        "2.": (10, 20),
        "3.": (20, 40),
        "4.": (40, 80),
        "5.": (80, 150),
        "6.": (150, 250),
        "7.": (250, 400),
        "8.": (400, 600),
        "9.": (600, 850),
        "10.": (850, 1150),
        "11.": (1150, 1500),
        "12.": (1500, 1950),
        "13.": (1950, 2450),
        "14.": (2450, 1000000),        
    }
        
    for country in countries:
        army_experiences = country.military_properties.army_experiences
        rank = country.military_properties.rank
        experiences_of_age = country.military_properties.experiences_of_age
        sanctity = country.military_properties.sanctity
        played_rounds = country.properties.played_rounds
        
        total_exps += experiences_of_age
        total_rounds += played_rounds
        
        rows.append({
            "country_name": country.identity.country_name,
            "country_number": country.identity.country_number,
            "army_experiences": army_experiences,
            "rank": rank,
            "experiences_of_age": experiences_of_age,
            "sanctity": sanctity,            
            })
            
    average_exp = total_exps // country_count # avarege of values of all numbers in the list
    
    for rank, (l_min, l_max) in rank_limits.items():
        if l_min <= average_exp < l_max:
            alliance_rank =  rank
            rank_limits(l_min, l_max)
            
            average_alliance_exp = (rank, l_min, l_max, average_exp)
            
    # total_exp, average_exp, rank, l_min, l_max --- next average exp to rounds and rest_exp to higher rank level
    
    average_played_rounds = total_rounds // country_count
    exps_to_played_rounds = average_exp // average_played_rounds
    

        
    return {
        "rows": rows,
        "average_exp": average_exp,
        "rank": rank,
        "rank_limits": rank_limits,
        "total_exps": total_exps,
        "country_count": country_count,
               
    }

def build_economic_tech(countries):
    rows = []
    
    for country in countries:
        total_economic_technologies = country.economic_tech.economic_technologies
        construction_speed = country.economic_tech.construction_speed
        business = country.economic_tech.business
        population_density = country.economic_tech.population_density
        farming = country.economic_tech.farming
        factory_automation = country.economic_tech.factory_automation
        energetics = country.economic_tech.energetics
        
        rows.append({
            "country_name": country.identity.country_name,
            "country_number": country.identity.country_number,
        })
    return {
        "rows": rows,
    }

def build_military_tech(countries):
    rows = []
    
    for country in countries: 
        militamilitary_technologies = country.military_tech.militamilitary_technologies
        force_of_arms = country.military_tech.force_of_arms
        domestic_market_price = country.military_tech.domestic_market_price
        rocket_development = country.military_tech.rocket_development
        missile_defense = country.military_tech.missile_defense
        intelligence_force = country.military_tech.intelligence_force
        space_exploration = country.military_tech.space_exploration
        
        rows.append({
            "country_name": country.identity.country_name,
            "country_number": country.identity.country_number,
        })
    return {
        "rows": rows,
    }    
        
def build_properties(countries):
    rows = []
    
    for country in countries:
        country_prestige = country.properties.country_prestige
        population = country.properties.population
        money = country.properties.money
        food = country.properties.food
        energy = country.properties.energy
        satisfaction = country.properties.satisfaction
        stored_on_the_market = country.propeties.stored_on_the_market
        played_rounds = country.properties.played_rounds
        free_rounds = country.properties.free_rounds
        inaccessible_rounds = country.propeties.inaccessible_rounds
        
        rows.append({
            "country_name": country.identity.country_name,
            "country_number": country.identity.country_number,
        })
    return {
        "rows": rows,
    }

def build_buildings(countries):
    rows = []
    
    for country in countries:
        country_area = country.buildings.country_area
        villages = country.buildings.villages
        cities = country.buildings.cities
        business_zones = country.buildings.business_zones
        farms = country.buildings.farms
        laboratories = country.buildings.laboratories
        factories = country.buildings.factories
        barracks = country.buildings.barracks
        power_plants = country.buildings.power_plants
        entertainment_centers = country.buildings.entertainment_centers
        military_bases = country.buildings.military_bases
        construction_companies = country.buildings.construction_companies
        unbuilt = country.buildings.unbuilt
        ruins = country.buildings.ruins
        
        rows.append({
            "country_name": country.identity.country_name,
            "country_number": country.identity.country_number,
        })
    return {
        "rows": rows,
    }

def build_bonuses(countries):
    rows = []
    
    for country in countries:
        bonus_villages = country.bonuses.bonus_villages
        bonus_farms = country.bonuses.bonus_farms
        bonus_laboratories = country.bonuses.bonus_laboratories
        bonus_factories = country.bonuses.bonus_factories
        bonus_barracks = country.bonuses.bonus_barracks
        bonus_power_plants = country.bonuses.bonus_power_plants
        bonus_military_bases = country.bonuses.bonus_military_bases
        bonus_money = country.bonuses.bonus_money
        bonus_max_economic_technolgies = country.bonuses.bonus_max_economic_technolgies
        bonus_max_military_technologies = country.bonuses.bonus_max_military_technologies
        bonus_efekt_economy_technologies = country.bonuses.bonus_efekt_economy_technologies
        bonus_attak = country.bonuses.bonus_attak
        bonus_defense = country.bonuses.bonus_defense
        bonus_colonization = country.bonuses.bonus_colonization
        bonus_wages = country.bonuses.bonus_wages
        
        rows.append({
            "country_name": country.identity.country_name,
            "country_number": country.identity.country_number,
        })
    return {
        "rows": rows,
    }

def build_production(countries):
    rows = []
    
    for country in countries: 
        money_increase = country.production.money_increase
        food_increase = country.production.food_increase
        energy_increase = country.production.energy_increase
        soldiers_increase = country.production.soldiers_increase
        parts_of_units_increase = country.production.parts_of_units_increase
        technology_increase = country.production.technology_increase
        
        rows.append({
            "country_name": country.identity.country_name,
            "country_number": country.identity.country_number,
        })
    return {
        "rows": rows,
    }

def Build_otherproperties(countries):
    rows = []
    
    for country in countries:
        logout = country.otherproperties.logout
        start_of_developing = country.otherproperties.start_of_developing
        last_economic_aid = country.otherproperties.last_economic_aid
        incoming_aids = country.otherproperties.incoming_aids
        outcoming_aids = country.otherproperties.outcoming_aids
        last_humanitarian_aids = country.otherproperties.last_humanitarian_aids
        alliance_last_message = country.otherproperties.alliance_last_message
        to_cash_register = country.otherproperties.to_cash_register
        from_cash_register = country.otherproperties.from_cash_register
        space_exploartion_increase = country.otherproperties.space_exploartion_increase
        points_of_utopia = country.otherproperties.points_of_utopia
        proportion_of_androids = country.otherproperties.proportion_of_androids
        ufo_chance = country.otherproperties.ufo_chance
        embargo_votes = country.otherproperties.embargo_votes
        operations = country.otherproperties.operations
        
        rows.append({
            "country_name": country.identity.country_name,
            "country_number": country.identity.country_number,
        })
    return {
        "rows": rows,
    }
        
# def country_summary(countries):
#     table = []
    
#     for country in countries:
#         table.append({
#             "country_number": country.identity.country_number,
#             "country_name": country.identity.country_name,
#             "player_name": country.identity.player_name, 
#             "alliance_name": country.identity.alliance_name,
#         })
        
#     return table
#         prestige_total_country_units = soldiers+tanks*5+fighters*3.5+bunkers*3.5+mechs*2.7
#       prestige_total_alliance_units += prestige_total_country_units