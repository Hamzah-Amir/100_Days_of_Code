# Exception Handling in Python

This directory demonstrates how to handle errors and exceptions in Python programs.

## Key Concepts

### Exception Handling
- Manages runtime errors gracefully
- Prevents program crashes
- Allows error recovery
- Provides error information

### Try-Except Blocks
1. **Basic Structure**
   ```python
   try:
       # Code that might raise an exception
   except ExceptionType:
       # Handle the exception
   ```

2. **Multiple Exceptions**
   - Can catch different types
   - Specific exception handling
   - Order matters (most specific first)

3. **Common Exceptions**
   - ValueError: Invalid value
   - IndexError: Invalid index
   - TypeError: Invalid type
   - ZeroDivisionError: Division by zero

### Best Practices
- Catch specific exceptions
- Keep try blocks small
- Provide meaningful error messages
- Clean up resources properly

## Code Example
The `main.py` file demonstrates:
- Basic try-except usage
- Multiple exception handling
- Common error scenarios
- Error message handling 