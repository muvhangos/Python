cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the most populous metropolitan area in the world.',
        'area': '2,194 km²',
        'famous_landmark': 'Tokyo Tower'
    },
    'New York': {
        'country': 'United States',
        'population': 8419600,
        'fact': 'New York City is known as "The Big Apple".',
        'area': '783.8 km²',
        'famous_landmark': 'Statue of Liberty'
    },
    'Paris': {
        'country': 'France',
        'population': 2140526,
        'fact': 'Paris is known as "The City of Light".',
        'area': '105.4 km²',
        'famous_landmark': 'Eiffel Tower'
    }
}

# Looping through the dictionary and printing each city's information
for city, info in cities.items():
    print(f"\nInformation about {city}:")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print(f"Area: {info['area']}")
    print(f"Famous Landmark: {info['famous_landmark']}")