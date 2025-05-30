# Tuples in Python
# This file shows basic tuple operations and characteristics

# Example 1: Basic Tuple Operations
print("Example 1 - Basic Tuple Operations:")
coordinates = (10, 20)
print("Coordinates:", coordinates)
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Example 2: Tuple Packing and Unpacking
print("\nExample 2 - Tuple Packing and Unpacking:")
person = ("John", 25, "New York")
name, age, city = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

# Example 3: Tuple Methods
print("\nExample 3 - Tuple Methods:")
numbers = (1, 2, 2, 3, 2, 4)
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3)) 