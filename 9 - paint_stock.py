# a program that checks a user's entered paint color against a list of available paint colors.

def paint_stock(search_item, paint_colors = ["blue","pink","beige","magenta","fuschia","yellow"]):
    for color in paint_colors:
        if search_item.lower() == color.lower():
            return "Found"
        else:
            pass
    return "Not Found"

color_request = input("Which color would you like?: ")

paint_stock(color_request)
