# Initial dictionary of favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# List of people who should take the poll
people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'mike', 'anna']

# Loop through the list of people who should take the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, please take our favorite languages poll!")
