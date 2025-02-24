sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'turkey', 'veggie', 'pastrami', 'chicken']


print("The deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")