melon_names = [
    'Honeydew',
    'Crenshaw',
    'Crane',
    'Casaba',
    'Cantaloupe'
]


melon_prices = {
    'Honeydew': 0.99,
    'Crenshaw': 2.00,
    'Crane': 2.50,
    'Casaba': 2.50,
    'Cantaloupe': 0.99,
}

# melon_seedlessness = {
#     'Honeydew': True,
#     'Crenshaw': False,
#     'Crane': False,
#     'Casaba': False,
#     'Cantaloupe': False,
# }

# attributes = [
#     melon_prices, 
#     melon_seedlessness, 
#     melon_rind_color, 
#     melon_avg_weight
# ]

def make_dict_melon_names(melon_names):
    
    melon_dict = {}

    for melon_name in melon_names:
        melon_dict[melon_name] = {}

    return melon_dict

def add_melon_price(melon_dict, melon_prices):


    for melon_name in list(melon_prices.keys()):
        melon_dict[melon_name]["Melon Price"] = melon_prices[melon_name]
        
    return melon_dict

def add_melon_seedlessness(melon_dict, melon_seedlessness):


    for melon_name in list(melon_prices.keys()):
        melon_dict[melon_name]["Melon Seedlessness"] = 
            melon_seedlessness[melon_name]
        
    return melon_dict

melon_names_dict = make_dict_melon_names(melon_names)

melon_dict = add_melon_price(melon_names_dict, melon_prices)