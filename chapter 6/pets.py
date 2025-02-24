# Creating a dictionary called favorite_places
favorite_places = {
    'Alice': ['Paris', 'New York', 'Tokyo'],
    'Bob': ['London', 'Sydney'],
    'Charlie': ['Rome', 'Barcelona', 'Amsterdam']
}

# Looping through the dictionary and printing each person's name and their favorite places
for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")