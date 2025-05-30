# Functions in Python
# This file shows how to create and use functions

# Example 1: Basic Function
print("Example 1 - Basic Function:")
def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))

# Example 2: Function with Multiple Parameters
print("\nExample 2 - Function with Parameters:")
def calculate_sum(a, b):
    return a + b

print(f"Sum of 5 and 3 is: {calculate_sum(5, 3)}")

# Example 3: Function with Default Parameter
print("\nExample 3 - Function with Default Parameter:")
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))
print(greet_with_title("Smith", "Dr.")) 