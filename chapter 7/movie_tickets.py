while True:
    age = input("Please enter your age (or 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break
    
    age = int(age)
    
    if age < 3:
        print("The ticket is free.")
    elif 3 <= age <= 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")