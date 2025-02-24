# Creating dictionaries for three people
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'Johannesburg'
}

person2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Cape Town'
}

person3 = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'Durban'
}

# Storing the dictionaries in a list called people
people = [person1, person2, person3]

# Looping through the list of people and printing their information
for person in people:
    print(f"\nInformation about {person['first_name']} {person['last_name']}:")
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")