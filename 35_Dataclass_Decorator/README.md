# Python Dataclass Decorator

A simple demonstration of Python's `@dataclass` decorator and its benefits.

## What is @dataclass?

The `@dataclass` decorator is a Python feature that automatically adds generated special methods to classes, such as `__init__`, `__repr__`, `__eq__`, etc.

## Why Use @dataclass?

- **Less Boilerplate**: Automatically generates common methods
- **Clean Code**: Reduces repetitive code for class initialization
- **Type Hints**: Supports type annotations for better code clarity
- **Default Values**: Allows setting default values for class attributes

## Example

```python
@dataclass
class Person:
    name: str
    age: int
    nationality: str
```

Instead of writing:
```python
class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
```

## Features Demonstrated
- Basic dataclass implementation
- Default values in dataclasses
- Custom methods in dataclass 