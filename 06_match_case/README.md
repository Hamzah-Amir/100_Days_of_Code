# Match-Case in Python

This directory demonstrates the use of match-case statements, introduced in Python 3.10.

## Key Concepts

### Match-Case Statement
- Similar to switch statements in other languages
- More powerful and flexible than traditional if-elif-else
- Requires Python 3.10 or later

### Features
1. **Basic Pattern Matching**
   ```python
   match value:
       case pattern1:
           # code
       case pattern2:
           # code
       case _:  # default case
           # code
   ```

2. **Multiple Patterns**
   - Use `|` to match multiple patterns
   - Example: `case "start" | "begin"`

### Best Practices
- Always include a default case (`case _`)
- Use clear, descriptive pattern names
- Consider pattern complexity

## Code Example
The `main.py` file demonstrates:
- Basic match-case usage
- Multiple pattern matching
- Default case handling 