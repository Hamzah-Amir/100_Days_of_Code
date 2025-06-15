# Constructors in Object-Oriented Programming

This project demonstrates the implementation of constructors in Python using a simple `Person` class.

## Code Overview

The code shows:
- A `Person` class with a constructor (`__init__` method)
- Constructor parameters: name, age, and nationality
- Two methods: `greet()` and `info()`
- Example usage with a Person instance

## Constructor Features
- The `__init__` method initializes object attributes
- Parameters are assigned to instance variables using `self`
- Constructor is called automatically when creating a new object

## Example Usage
```python
a = Person("John", 30, "American")
a.greet()  # Output: John says hello!
a.info()   # Output: John is 30 years old, and is American citizen.
``` 