import datetime

def greet_user():
    print("Welcome to the Greeting App!")
    name = input("Please enter your name: ")
    return name

def get_greeting(name):
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    return f"{greeting}, {name}!"

def main():
    name = greet_user()
    greeting = get_greeting(name)
    print(greeting)
    

if __name__ == "__main__":
    main()
