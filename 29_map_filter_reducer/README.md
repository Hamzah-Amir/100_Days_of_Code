# Python Map, Filter, and Reduce Functions

This repository contains examples demonstrating the usage of three powerful functional programming tools in Python: `map()`, `filter()`, and `reduce()`.

## Map Function
The `map()` function applies a given function to each item in an iterable (like a list) and returns a map object.

```python
def square(x):
    return x * x

numbers = [5, 6, 8, 1, 2, 7, 3]
squared_numbers = list(map(square, numbers))
# Result: [25, 36, 64, 1, 4, 49, 9]
```

## Filter Function
The `filter()` function creates an iterator from elements of an iterable for which a function returns true.

```python
def filter_function(a):
    return a > 5

numbers = [5, 6, 8, 1, 2, 7, 3]
filtered_numbers = list(filter(filter_function, numbers))
# Result: [6, 8, 7]
```

## Reduce Function
The `reduce()` function from `functools` module applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.

```python
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 6, 1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
# Result: 22
```

## Key Points
- `map()` transforms each element in an iterable
- `filter()` selects elements that meet a condition
- `reduce()` combines all elements into a single value

## Requirements
- Python 3.x
- No additional packages required 