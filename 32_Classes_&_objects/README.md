# Human Class Implementation

This is a simple Python program demonstrating the use of classes and objects. The program implements a `Human` class with basic attributes and methods.

## Features

- A `Human` class with the following attributes:
  - name
  - age
  - occupation
  - country
- An `info()` method that returns a formatted string with the person's information
- Ability to modify class attributes after object creation

## Usage

```python
# Create a new Human object
person = Human()

# Access attributes
print(person.name)  # Output: Hamza
print(person.age)   # Output: 18

# Get formatted information
print(person.info())  # Output: Hamza is a 18-year-old Software Engineer from Pakistan.

# Modify attributes
person.name = "Ali"
print(person.name)  # Output: Ali
```

## Default Values

The `Human` class comes with the following default values:
- name: "Hamza"
- age: 18
- occupation: "Software Engineer"
- country: "Pakistan" 