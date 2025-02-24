# List of current usernames
current_users = ["admin", "jaden", "sophia", "michael", "emma"]

# List of new usernames
new_users = ["john", "sophia", "mike", "emma", "lisa"]

# Convert current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Loop through the new_users list to check for availability
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")
