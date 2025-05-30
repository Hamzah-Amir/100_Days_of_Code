# Recursion in Python
# This file shows basic recursive functions

# Example 1: Factorial using Recursion
print("Example 1 - Factorial:")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Example 2: Fibonacci using Recursion
print("\nExample 2 - Fibonacci:")
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("First 5 Fibonacci numbers:")
for i in range(5):
    print(fibonacci(i), end=" ")
print()

# Example 3: Sum of Numbers using Recursion
print("\nExample 3 - Sum of Numbers:")
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print(f"Sum of numbers from 1 to 5: {sum_numbers(5)}") 