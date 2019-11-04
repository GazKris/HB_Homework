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

melon_seedlessness = {
    'Honeydew': True,
    'Crenshaw': False,
    'Crane': False,
    'Casaba': False,
    'Cantaloupe': False,
}

melon_flesh_color = {
    'Honeydew': None,
    'Crenshaw': None,
    'Crane': None,
    'Casaba': None,
    'Cantaloupe': None,
}

melon_avg_weight = {
    'Honeydew': None,
    'Crenshaw': None,
    'Crane': None,
    'Casaba': None,
    'Cantaloupe': None,
}

# attributes = [
#     melon_prices, 
#     melon_seedlessness, 
#     melon_flesh_color, 
#     melon_avg_weight
# ]

def make_dict_melon_names(melon_names):
    
    melon_dict = {}

    for melon_name in melon_names:
        melon_dict[melon_name] = {}

    return melon_dict


def add_melon_price(melon_dict, melon_prices):


    for melon_name in list(melon_prices.keys()):
        melon_dict[melon_name]["Melon_Price"] = melon_prices[melon_name]
        
    return melon_dict


def add_melon_seedlessness(melon_dict, melon_seedlessness):


    for melon_name in list(melon_seedlessness.keys()):
        melon_dict[melon_name]["Melon_Seedlessness"] = \
            melon_seedlessness[melon_name]
        
    return melon_dict


def add_melon_flesh_color(melon_dict, melon_flesh_color):

    for melon_name in list(melon_flesh_color.keys()):
        melon_dict[melon_name]["Melon_Flesh_Color"] = \
            melon_flesh_color[melon_name]

    return melon_dict


def add_melon_weight(melon_dict, melon_avg_weight):

    for melon_name in list(melon_avg_weight.keys()):
        melon_dict[melon_name]["Melon_Avg_Weight"] = \
            melon_avg_weight[melon_name]

    return melon_dict   

melon_dict_names = make_dict_melon_names(melon_names)

melon_dict_price = add_melon_price(melon_dict_names, melon_prices)

melon_dict_seedlessness = add_melon_seedlessness(melon_dict_price, melon_seedlessness)

melon_dict_flesh_color = add_melon_flesh_color(melon_dict_seedlessness, melon_flesh_color)

melon_dict = add_melon_weight(melon_dict_flesh_color, melon_avg_weight)