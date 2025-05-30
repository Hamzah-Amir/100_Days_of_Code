# Break and Continue in Python

This directory demonstrates the use of break and continue statements for loop control in Python.

## Key Concepts

### Break Statement
- Exits the loop immediately
- Used to terminate a loop early
- Can be used in both for and while loops
- Example:
  ```python
  for i in range(5):
      if i == 3:
          break
  ```

### Continue Statement
- Skips the current iteration
- Continues with the next iteration
- Useful for skipping specific conditions
- Example:
  ```python
  for i in range(5):
      if i == 2:
          continue
  ```

### Best Practices
- Use break for early loop termination
- Use continue to skip specific iterations
- Avoid deep nesting of break/continue
- Consider readability when using these statements

## Code Example
The `main.py` file demonstrates:
- Break statement in for loops
- Continue statement usage
- Break in while loops
- Common use cases for both statements 