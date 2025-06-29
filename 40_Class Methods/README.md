# Static Methods in Python

This script demonstrates the concept of static methods in Python classes using the `@staticmethod` decorator.

## What are Static Methods?

Static methods are methods that belong to a class but don't require an instance of the class to be called. They can be accessed directly through the class name.

## Code Example

The script shows:
- A `Mathematics` class with a regular instance method `addtonum()`
- A static method `add()` that can be called without creating an instance
- Comparison between instance methods and static methods

## Key Points

- Static methods use the `@staticmethod` decorator
- They don't receive `self` or `cls` as the first parameter
- Can be called directly on the class: `Mathematics.add(3, 4)`
- Useful when you want to share functionality without requiring class instantiation

## Usage

Run the script to see both instance method and static method in action. 