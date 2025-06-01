# Custom Error Handling in Python

This project demonstrates how to implement custom error handling in Python using the `raise` statement.

## Program Description

The program takes a user input and validates it against specific criteria:
- Accepts a number between 6 and 10
- Allows the user to quit by entering 'quit'
- Raises a custom error if the input is outside the valid range

## Features

- Input validation
- Custom error handling
- Graceful program termination
- User-friendly error messages

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory
3. Run the program:
```bash
python main.py
```

## Usage

- Enter a number between 6 and 10 to run the program successfully
- Enter 'quit' to exit the program
- Enter any other value to see the custom error message

## Example Output

```
Enter a value between 6 and 10: 7
Program runs successfully.

Enter a value between 6 and 10: 4
Value should be between 6 and 10

Enter a value between 6 and 10: quit
Quitting the program.
``` 