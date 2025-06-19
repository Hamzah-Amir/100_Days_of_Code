# 🧮 Static Method Example in Python

This project demonstrates the use of **static methods** in Python classes using a simple `Mathematics` class.

## Code Overview
- **Mathematics class**: Uses `@dataclass` for easy data handling.
- `addtonum(self, n)`: Adds `n` to the instance's `num` value.
- `@staticmethod add(a, b)`: Adds two numbers. Can be called **without creating an object**.

## Usage
```python
a = Mathematics(6)
a.addtonum(3)        # Outputs: 9
Mathematics.add(3,4) # Outputs: 7
```

## What is a Static Method?
- Defined with `@staticmethod` decorator.
- **Does not access** instance (`self`) or class (`cls`) data.
- Can be called on the class itself, no need to create an object.
- Useful for utility functions related to the class, but not dependent on its data.

---
**Tip:** Use static methods for helper functions that logically belong to a class but don't need to access or modify its data. 