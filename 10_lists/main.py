# Lists in Python
# This file shows basic list operations and methods

# Example 1: Basic List Operations
print("Example 1 - Basic List Operations:")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
fruits.append("orange")
print("After append:", fruits)
fruits.remove("banana")
print("After remove:", fruits)

# Example 2: List Slicing and Methods
print("\nExample 2 - List Slicing and Methods:")
numbers = [1, 2, 3, 4, 5]
print("First three numbers:", numbers[:3])
print("Last two numbers:", numbers[-2:])
print("Reversed list:", numbers[::-1])

# Example 3: List Comprehension
print("\nExample 3 - List Comprehension:")
squares = [x**2 for x in range(1, 4)]
print("Squares of numbers 1-3:", squares) 