# List of places I'd like to visit
places_to_visit = ["Tokyo", "Paris", "New York", "Cape Town", "Sydney"]

# Print the list in its original order
print("Original list:", places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the actual list
print("Alphabetical order:", sorted(places_to_visit))

# Show that the list is still in its original order
print("Original list after sorted():", places_to_visit)

# Use sorted() to print the list in reverse-alphabetical order without changing the order of the original list
print("Reverse-alphabetical order:", sorted(places_to_visit, reverse=True))

# Show that the list is still in its original order
print("Original list after reverse sorted():", places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("List after reverse():", places_to_visit)

# Use reverse() to change the order of the list again
places_to_visit.reverse()
print("List after reversing again:", places_to_visit)

# Use sort() to change the list so it's stored in alphabetical order
places_to_visit.sort()
print("List after sort():", places_to_visit)

# Use sort() to change the list so it's stored in reverse-alphabetical order
places_to_visit.sort(reverse=True)
print("List after reverse sort():", places_to_visit)

