# Creating a dictionary with rivers and the countries they run through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Loop to print the name of each river
print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())

# Loop to print the name of each country
print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(country.title())