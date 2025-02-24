# Import the functions from printing_functions.py
from printing_functions import print_models, show_completed_models

# List of unprinted designs
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call the functions
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
