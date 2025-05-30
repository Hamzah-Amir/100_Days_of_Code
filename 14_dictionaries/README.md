# Dictionaries in Python

This directory demonstrates the use of dictionaries, key-value pair collections in Python.

## Key Concepts

### Dictionaries
- Mutable key-value pairs
- Created using curly braces `{}`
- Keys must be unique and immutable
- Values can be any type

### Key Operations
1. **Basic Operations**
   - Add: `dict[key] = value`
   - Remove: `del dict[key]`
   - Access: `dict[key]`
   - Update: `dict.update()`

2. **Dictionary Methods**
   - `keys()`: Get all keys
   - `values()`: Get all values
   - `items()`: Get key-value pairs
   - `get()`: Safe value access

3. **Dictionary Comprehension**
   - Create dictionaries dynamically
   - Syntax: `{key: value for item in iterable}`
   - Can include conditions

### Best Practices
- Use meaningful key names
- Consider using `get()` for safe access
- Use for structured data
- Consider performance for large dictionaries

## Code Example
The `main.py` file demonstrates:
- Basic dictionary operations
- Dictionary methods usage
- Dictionary comprehension
- Common dictionary manipulations 