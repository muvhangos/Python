def make_car(manufacturer, model, **car_info):
    """
    Store information about a car in a dictionary.
    """
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    for key, value in car_info.items():
        car[key] = value
    return car

# Call the function with required information and additional name-value pairs
car_profile = make_car('Toyota', 'Corolla', color='blue', sunroof=True)

# Print the car profile
print(car_profile)