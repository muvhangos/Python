def describe_city(city, country='Iceland'):
    """Print a simple sentence about a city and its country."""
    print(f"{city} is in {country}.")

# Calling the function for three different cities
describe_city('Reykjavik')
describe_city('Akureyri')
describe_city('Tokyo', 'Japan')