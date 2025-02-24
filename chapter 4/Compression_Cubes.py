# Create a list of the first 10 cubes
cubes = [number**3 for number in range(1, 11)]

# Print the list of cubes
print("List of cubes:", cubes)

# Print the first three items in the list
print("The first three items in the list are:", cubes[:3])

# Print three items from the middle of the list
middle_index = len(cubes) // 2
print("Three items from the middle of the list are:", cubes[middle_index-1:middle_index+2])

# Print the last three items in the list
print("The last three items in the list are:", cubes[-3:])