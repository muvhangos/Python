# Original list of pizzas
pizzas = ["Margherita", "Pepperoni", "Hawaiian"]

# Make a copy of the list and call it friend_pizzas
friend_pizzas = pizzas.copy()

# Add a new pizza to the original list
pizzas.append("BBQ Chicken")

# Add a different pizza to the list friend_pizzas
friend_pizzas.append("Veggie")

# Prove that you have two separate lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
