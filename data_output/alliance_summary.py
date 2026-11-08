def build_alliance(countries):
    
    print(type(countries[0].buildings.country_area))
    
    alliance_header = build_alliance_header(countries)
    

    return {
        "alliance_header": alliance_header,
        "alliance_body": countries,
    }


def build_alliance_header(countries):
    
    rank_limits = {
        "1": (0, 10),
        "2": (10, 20),
        "3": (20, 40),
        "4": (40, 80),
        "5": (80, 150),
        "6": (150, 250),
        "7": (250, 400),
        "8": (400, 600),
        "9": (600, 850),
        "10": (850, 1150),
        "11": (1150, 1500),
        "12": (1500, 1950),
        "13": (1950, 2450),
        "14": (2450, 1000000),        
    }
    
    alliance_name = countries[0].identity.alliance_name
    members_count = len(countries)
    
    alliance_area = 0
    alliance_prestige = 0
    alliance_exps = 0

    
    for country in countries:
        alliance_area += int(country.buildings.country_area) # k
        alliance_prestige += float(country.properties.country_prestige) # k
        alliance_exps += int(country.military_properties.experiences_of_age) # k
        
    max_war = alliance_prestige * 2    
    
    average_exp = alliance_exps / members_count
    
    for rank, (l_min, l_max) in rank_limits.items():
                
        if l_min <= average_exp < l_max:
            alliance_rank = int(rank)
            one_country = l_max - average_exp
            new_alliance_level = one_country * members_count
                        
            break
        
    return {
        "name": alliance_name,
        "members": members_count,
        "area": alliance_area,
        "prestige": alliance_prestige,
        "max_prest_to_war": max_war,
        "rank": alliance_rank,
        "new_level": new_alliance_level,
        "exp_to_country": one_country,        
    }

