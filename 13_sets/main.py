# Sets in Python
# This file shows basic set operations and methods

# Example 1: Basic Set Operations
print("Example 1 - Basic Set Operations:")
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)
fruits.add("orange")
print("After adding:", fruits)
fruits.remove("banana")
print("After removing:", fruits)

# Example 2: Set Operations
print("\nExample 2 - Set Operations:")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Example 3: Set Methods
print("\nExample 3 - Set Methods:")
numbers = {1, 2, 3, 4, 5}
print("Is 3 in set?", 3 in numbers)
print("Is 6 in set?", 6 in numbers)
print("Set length:", len(numbers)) 