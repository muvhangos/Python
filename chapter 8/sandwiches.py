def build_profile(first, last, **user_info):
    """
  
  """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Build a profile of yourself
my_profile = build_profile(
    first='John',
    last='Doe',
    location='Johannesburg',
    profession='Software Developer',
    hobby='Photography'
)

# Print the profile
print(my_profile)