# Short If-Else (Ternary Operator) in Python

This project demonstrates the use of Python's ternary operator, a concise way to write conditional expressions.

## Program Description

The program shows two different ways to use the ternary operator:
1. For conditional printing
2. For conditional value assignment

## Syntax

The ternary operator in Python follows this syntax:
```python
value_if_true if condition else value_if_false
```

## Examples in the Code

### 1. Conditional Printing
```python
print("A is greater than b") if a>b else print("B is greater than a")
```
This is equivalent to:
```python
if a > b:
    print("A is greater than b")
else:
    print("B is greater than a")
```

### 2. Conditional Value Assignment
```python
c = 56 if a<b else 34
```
This is equivalent to:
```python
if a < b:
    c = 56
else:
    c = 34
```

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory
3. Run the program:
```bash
python main.py
```

## Output Example

```
A is greater than b
34
```

## Benefits of Using Ternary Operator

- More concise code
- Single-line conditional expressions
- Useful for simple if-else conditions
- Can be used in expressions where if-else statements cannot

## Best Practices

- Use for simple conditions only
- Avoid nesting multiple ternary operators
- Keep the code readable
- Use when the condition and outcomes are straightforward 