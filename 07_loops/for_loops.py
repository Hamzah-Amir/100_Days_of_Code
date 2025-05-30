# For Loops in Python
# This file shows different ways to use for loops

# Example 1: Basic For Loop with List
print("Example 1 - For Loop with List:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Example 2: For Loop with Range
print("\nExample 2 - For Loop with Range:")
print("Counting from 0 to 4:")
for i in range(5):
    print(f"Number: {i}")

print("\nCounting from 2 to 5:")
for i in range(2, 6):
    print(f"Number: {i}")

print("\nCounting by 2s from 0 to 6:")
for i in range(0, 7, 2):
    print(f"Number: {i}")

# Example 3: For Loop with enumerate
print("\nExample 3 - For Loop with enumerate:")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Example 4: Nested For Loop
print("\nExample 4 - Nested For Loop:")
for i in range(1, 3):
    for j in range(1, 3):
        print(f"i={i}, j={j}, product={i*j}")

# Example 5: For Loop with Dictionary
print("\nExample 5 - For Loop with Dictionary:")
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}") 