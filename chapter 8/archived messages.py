def make_sandwich(*items):
    """
    Accepts a list of items for a sandwich and prints a summary of the order.
    """
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function three times with different numbers of arguments
make_sandwich("ham", "cheese", "lettuce", "tomato")
make_sandwich("turkey", "bacon", "avocado")
make_sandwich("peanut butter", "jelly")