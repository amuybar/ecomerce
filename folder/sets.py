# Accept user input to create two sets of integers
set1 = set(input("Enter elements for set 1 separated by spaces: ").split())
set2 = set(input("Enter elements for set 2 separated by spaces: ").split())

# Create a new set containing only the elements that are common to both sets
common_elements = set1.intersection(set2)

print("Common elements:", common_elements)
