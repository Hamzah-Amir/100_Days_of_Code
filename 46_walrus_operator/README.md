# Walrus Operator in Python (:=)

This directory demonstrates the usage of the **walrus operator** (`:=`) in Python, introduced in Python 3.8. The walrus operator allows you to assign a value to a variable as part of an expression.

## What is the Walrus Operator?
The walrus operator (`:=`) lets you assign values to variables within an expression, such as within a condition or a loop. This can make your code more concise and readable.

## Example 1: Using Walrus Operator in a While Loop
```python
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(f"length of numbers: {n}")
    numbers.pop()
print("No number left in list")
```
**Explanation:**
- Here, `n` is assigned the value of `len(numbers)` in the while condition.
- The loop continues until the list is empty, printing the current length each time.

## Example 2: Using Walrus Operator with User Input
```python
foods = []
while (food := input('What food do you like: ')) != 'quit':
    foods.append(food)
```
**Explanation:**
- The input from the user is assigned to `food` and checked if it is not `'quit'`.
- If not, the food is added to the `foods` list.
- The loop ends when the user types `'quit'`.

## When to Use the Walrus Operator
- When you want to both assign and use a value in a single expression (e.g., in loops or comprehensions).
- To make your code more concise and avoid repeating function calls or expressions.

## Requirements
- Python 3.8 or higher (for the walrus operator support).

---
**Try running `main.py` to see the examples in action!** 