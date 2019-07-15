"""Restaurant rating lister."""


# put your code here
def print_restaurant_ratings(txtfile):
    """prints all resturants by alphabetical order and their associated rating
    """
   
    with open(txtfile,'r') as f:
        restaurant_file = f.read()

    restaurant_dict = {}
    
    restaurant_lines = restaurant_file.rstrip().split("\n")

    for restaurant in restaurant_lines:
        rest_name, rest_rating = restaurant.split(":")

        restaurant_dict[rest_name] = rest_rating

    # ask user if they want to add a restaurant, if yes add it to the dictionary
    while True:
        add_rest_choice = input("Would you like to add a restuarant? Y or N: ").upper()

        if add_rest_choice.startswith("Y"):
            add_restaurant_name = input("Add a new restaurant: ")
            add_restaurant_rating = input(f"Add {add_restaurant_name}'s rating: ")

            restaurant_dict[add_restaurant_name] = add_restaurant_rating
            print(f"Thank you. {add_restaurant_name}: {add_restaurant_rating} has been added.")
            print()
        else:
            print()
            break

    sorted_restaurants = sorted(restaurant_dict.items())

    for restaurant in sorted_restaurants:
        print(f"{restaurant[0]} is rated at {restaurant[1]}.")

    # return restaurant_dict



   