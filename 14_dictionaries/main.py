# Dictionaries in Python
# This file shows basic dictionary operations and methods

# Example 1: Basic Dictionary Operations
print("Example 1 - Basic Dictionary Operations:")
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Original dictionary:", person)
person["job"] = "Developer"
print("After adding job:", person)
del person["age"]
print("After removing age:", person)

# Example 2: Dictionary Methods
print("\nExample 2 - Dictionary Methods:")
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

# Example 3: Dictionary Comprehension
print("\nExample 3 - Dictionary Comprehension:")
squares = {x: x**2 for x in range(1, 4)}
print("Squares dictionary:", squares) 