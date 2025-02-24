# List of usernames
usernames = ["admin", "jaden", "sophia", "michael", "emma"]

# Check if the list of users is empty
if usernames:
    # Loop through the list and print a greeting to each user
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Remove all usernames from the list
usernames = []

# Check if the list of users is empty again
if usernames:
    # Loop through the list and print a greeting to each user
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
