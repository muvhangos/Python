class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User {self.username}: {self.first_name} {self.last_name}, Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Create an instance of the User class
user = User("John", "Doe", "johndoe", "johndoe@example.com")

# Call increment_login_attempts() several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the value of login_attempts to make sure it was incremented properly
print(f"Login attempts: {user.login_attempts}")

# Call reset_login_attempts() and print login_attempts again to make sure it was reset to 0
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")