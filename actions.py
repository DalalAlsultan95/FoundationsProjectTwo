# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.achoo.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print("- %s" % store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store_name.lower() == store.name.lower():
            return store

    return False


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print("Pick a store by typing its name, or type 'checkout' to pay your bills and say your goodbyes.")
    
    while True:
        user_input = input().lower()
        if user_input.lower() == "checkout":
            return "checkout"

        store_obj = get_store(user_input)
        if store_obj:
            return store_obj

        print("Invalid store name.")

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to cart.
    """
    # your code goes here!
    print("Wot yu want mate? Correct spelling plz. Type 'back' to get out")
    while True:
        user_input = input().lower()
        for product in picked_store.products:
            if user_input.lower() == product.name.lower():
                cart.add_to_cart(product)

        if user_input == "back":
            break

def shop():
    """
    The main shopping functionality
    """
    cart_obj = Cart()
    # your code goes here!
    while True:
        print_stores()
        user_input = pick_store()
        if user_input == "checkout":
            cart_obj.checkout()
            return
        else:
            user_input.print_products()
            pick_products(cart_obj, user_input)

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
