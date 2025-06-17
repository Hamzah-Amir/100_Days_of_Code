# Python Decorators

This directory contains examples and explanations of decorators in Python.

## What are Decorators?

Decorators are a powerful feature in Python that allows you to modify the behavior of functions or classes without directly changing their source code. They provide a clean and elegant way to add functionality to existing code.

## Example in this Directory

The `main.py` file demonstrates a simple decorator implementation:

```python
def greet(func):
    def mfunc(*args,**kwargs):
        print("Hello, how are you")
        func(*args, **kwargs)
        print("Thanks for using this program")
    return mfunc

def multiply(a,b):
    return a*b

greet(multiply)(5,6)
```

### How it Works

1. The `greet` function is a decorator that takes another function as an argument
2. Inside `greet`, we define a wrapper function `mfunc` that:
   - Prints a greeting message
   - Calls the original function with its arguments
   - Prints a thank you message
3. The decorator is applied to the `multiply` function
4. When `multiply` is called, it's wrapped with the additional functionality

## Key Concepts

- Decorators use the `@` syntax (though not shown in this example)
- They can accept arguments using `*args` and `**kwargs`
- They can modify the behavior of functions without changing their code
- They are useful for:
  - Logging
  - Timing
  - Access control
  - Caching
  - And many other cross-cutting concerns

## Usage

To use the example code:

```python
# Apply the decorator
greet(multiply)(5,6)
```

This will output:
```
Hello, how are you
Thanks for using this program
```

## Best Practices

1. Always use `*args` and `**kwargs` to make decorators more flexible
2. Return the wrapper function from the decorator
3. Use `functools.wraps` to preserve function metadata
4. Keep decorators simple and focused on a single responsibility 