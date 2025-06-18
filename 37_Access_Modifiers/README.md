# Access Modifiers in Python

## Overview
This project demonstrates how access modifiers work in Python, including the concept of name mangling for "private" attributes.

## Key Concepts

### Public Attributes
- In Python, all attributes are public by default
- No special syntax required
- Can be accessed directly from outside the class

### Private Attributes (Convention)
- Python doesn't have true private attributes
- Convention: prefix with double underscore (`__`) to indicate "private"
- This triggers **name mangling** - Python automatically renames the attribute

### Name Mangling
- When you prefix an attribute with `__`, Python renames it to `_ClassName__attribute`
- This makes it harder (but not impossible) to access from outside the class
- Example: `__name` becomes `_Person__name`

## Code Examples

### Public Attributes
```python
@dataclass
class Person:
    name = "John"  # Public attribute
    age = 30       # Public attribute

person = Person()
print(person.name)  # Direct access works
```

### Private Attributes (Name Mangling)
```python
@dataclass
class Person:
    __name = "John"  # "Private" attribute
    __age = 30       # "Private" attribute

person = Person()
# This will raise AttributeError:
# print(person.__name)

# This works (name mangling):
print(person._Person__name)
```

## Important Notes
- Python's "private" attributes are not truly private
- Name mangling is a convention, not a security feature
- It's meant to prevent accidental access, not malicious access
- The `@dataclass` decorator is used for convenience in this example

## Running the Code
```bash
python main.py
```

The code demonstrates both public attribute access and the name mangling technique for accessing "private" attributes. 