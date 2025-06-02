# Python Enumerate Function Examples

This project demonstrates different ways to use Python's `enumerate()` function, which is a built-in function that adds a counter to an iterable and returns it as an enumerate object.

## Examples

### 1. Traditional Index Tracking
The first example shows the traditional way of tracking indices in a loop using a separate counter variable:
```python
index = 0
for fruit in fruits:
    print(fruit)
    if (index == 4):
        print(f"The fruit {fruit} is at index {index}")
    index += 1
```

### 2. Using Enumerate
The second example demonstrates how to use `enumerate()` to get both the index and value simultaneously:
```python
for index, fruit in enumerate(fruits):
    print(fruit)
    if (index == 5):
        print(f"The fruit {fruit} is at index {index}")
```

### 3. Custom Start Index
The third example shows how to start the enumeration from a custom number (in this case, 1 instead of 0):
```python
for index, fruit in enumerate(fruits, start=1):
    print(fruit)
    if (index == 6):
        print(f"The fruit {fruit} is at index {index}")
```

## Benefits of Using Enumerate
- More Pythonic and cleaner code
- Eliminates the need for manual index tracking
- Reduces the chance of index-related errors
- Provides a more readable and maintainable solution

## Sample Output
When you run the program, you'll see three different examples of iterating through a list of fruits, each demonstrating a different approach to index tracking. 