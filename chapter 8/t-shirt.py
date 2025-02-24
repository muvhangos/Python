def make_shirt(size, message):
    """Print a summary of the shirt size and the message on it."""
    print(f"The shirt size is {size} and the message on it is: '{message}'")

# Calling the function using positional arguments
make_shirt('Medium', 'Hello World!')

# Calling the function using keyword arguments
make_shirt(size='Large', message='Python is Awesome!')