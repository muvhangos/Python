favorite_numbers = {
    'Alice': [7, 14, 21],
    'Bob': [13, 26],
    'Charlie': [22, 33, 44],
    'Diana': [5, 10],
    'Eve': [42, 84]
}

# Printing each person's name and their favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")