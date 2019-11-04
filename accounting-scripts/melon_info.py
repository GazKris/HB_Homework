"""Print out all the melons in our inventory."""


from melons import melon_dict


def print_melon(melon_dict):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melon_dict.items():
        print(f"{melon_name}:")

        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")

        print("="*30)

print_melon(melon_dict)
