# Super Keyword in Python

This script demonstrates the use of the `super()` keyword in Python inheritance to call parent class methods.

## What is Super?

The `super()` function is used to call methods from a parent class. It's particularly useful in inheritance scenarios to avoid hardcoding the parent class name.

## Code Example

The script shows:
- A base `Employee` class with name and salary attributes
- A `Programmer` class that inherits from `Employee`
- Using `super().__init__()` to call the parent class constructor
- Adding a new attribute (`programming_language`) specific to programmers

## Key Points

- `super()` calls the parent class method without explicitly naming the parent
- Useful for maintaining clean inheritance hierarchies
- Allows child classes to extend parent functionality
- Helps avoid code duplication

## Usage

Run the script to see how inheritance works with the `super()` keyword. 