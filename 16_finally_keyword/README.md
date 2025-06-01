# Understanding the `finally` Keyword in Python

This project demonstrates the usage and importance of the `finally` keyword in Python's exception handling mechanism.

## Program Description

The program showcases two different implementations of error handling:
1. A simple try-except-finally block
2. A function-based implementation showing how `finally` works with return statements

## Key Concepts

- The `finally` block always executes, regardless of whether:
  - The try block succeeds
  - An exception occurs
  - A return statement is encountered
- This makes it perfect for cleanup operations and ensuring certain code always runs

## Features

- Basic exception handling with try-except
- Demonstration of `finally` block execution
- Function-based implementation
- Comparison between different approaches to code execution

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory
3. Run the program:
```bash
python main.py
```

## Usage

The program will:
1. First demonstrate a simple try-except-finally block
2. Then show a function-based implementation
3. In both cases, you'll be prompted to enter a number to access a list element

## Example Output

```
Enter your number: 2
1
I will execute on any cause

Enter your number: 10
Error occured
I will execute on any cause
```

## Why Use `finally`?

The `finally` block is particularly useful when:
- You need to ensure certain cleanup code always runs
- Working with resources that need to be closed (files, database connections)
- You want to execute code regardless of whether an exception occurred
- You need to maintain program state or logging even when errors occur 