dream_vacations = {}

# Polling users about their dream vacation
while True:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    
    # Storing the response in the dictionary
    dream_vacations[name] = place
    
    # Asking if another user wants to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != 'yes':
        break

# Printing the results of the poll
print("\n--- Poll Results ---")
for name, place in dream_vacations.items():
    print(f"{name} would like to visit {place}.")