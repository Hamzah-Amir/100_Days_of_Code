# Method Overriding in Python

## Overview
This directory demonstrates the concept of method overriding in Python using dataclasses and inheritance. Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.

## Code Example

### Shape Class (Parent Class)
```python
@dataclass
class Shape:
    x: int
    y: int

    def area(self):
        return self.x * self.y
```

### Circle Class (Child Class)
```python
@dataclass
class Circle(Shape):
    def __init__(self, radius: int):
        super().__init__(radius, radius)
    
    pie : float = 3.14

    def radius(self):
        return self.pie * super().area()
```

## Key Concepts Demonstrated

### 1. Method Overriding
- The `Circle` class inherits from `Shape` class
- The `radius()` method in `Circle` overrides the behavior by using the parent's `area()` method
- This shows how child classes can customize or extend parent class functionality

### 2. Inheritance with Dataclasses
- Using `@dataclass` decorator for both parent and child classes
- Demonstrates inheritance with dataclasses in Python

### 3. Constructor Overriding
- The `Circle` class overrides the `__init__` method of the parent class
- Uses `super().__init__()` to call the parent constructor
- **Note**: Overriding `__init__` in dataclasses is generally not recommended, but shown here for educational purposes

### 4. Using Parent Class Methods
- The `radius()` method uses `super().area()` to access the parent class's area calculation
- This demonstrates how to leverage parent class functionality while adding custom behavior

## Usage Example
```python
# Create a rectangle (Shape instance)
rec = Shape(10, 20)
print(f"Area of rectangle: {rec.area()}")  # Output: 200

# Create a circle (Circle instance)
circle = Circle(10)
print(f"Area of circle: {circle.radius()}")  # Output: 314.0
```

## Important Notes
- Method overriding allows for polymorphism in object-oriented programming
- The child class can completely replace or extend the parent class method
- Using `super()` is the recommended way to access parent class methods
- While dataclasses simplify class creation, overriding `__init__` should be done carefully

## Learning Objectives
- Understand method overriding in Python
- Learn how to use inheritance with dataclasses
- Practice using `super()` to access parent class methods
- See how to customize behavior in child classes while maintaining parent class functionality 