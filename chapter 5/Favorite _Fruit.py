usernames = ["admin", "jaden", "sophia", "michael", "emma"]

# Loop through the list and print a greeting to each user
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")