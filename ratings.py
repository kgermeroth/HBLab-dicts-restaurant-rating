"""Restaurant rating lister."""


# put your code here
def print_resturant_ratings(txtfile):
    """prints all resturants by alphabetical order and their associated rating
    """
    #restaurant_file = open(txtfile)

    with open(txtfile,'r') as f:
        restaurant_file = f.read()

    restaurant_dict = {}
    
    restaurant_lines = restaurant_file.rstrip().split("\n")

    for restaurant in restaurant_lines:
        rest_name, rest_rating = restaurant.split(":")

        restaurant_dict[rest_name] = rest_rating


    sorted_resturants = sorted(restaurant_dict.items())

    for restaurant in sorted_resturants:
        print(f"{restaurant[0]} is rated at {restaurant[1]}.")

   