# Creating dictionaries for different pets
pet1 = {
    'animal': 'dog',
    'owner': 'Alice'
}

pet2 = {
    'animal': 'cat',
    'owner': 'Bob'
}

pet3 = {
    'animal': 'rabbit',
    'owner': 'Charlie'
}

pet4 = {
    'animal': 'parrot',
    'owner': 'Diana'
}

pet5 = {
    'animal': 'hamster',
    'owner': 'Eve'
}

# Storing the dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4, pet5]

# Looping through the list of pets and printing their information
for pet in pets:
    print(f"\nInformation about the pet:")
    print(f"Kind of animal: {pet['animal'].title()}")
    print(f"Owner's name: {pet['owner'].title()}")