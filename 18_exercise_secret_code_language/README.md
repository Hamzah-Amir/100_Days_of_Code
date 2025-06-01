# Secret Code Language Program

This program implements a simple secret code language that can encode and decode messages using a specific algorithm.

## Program Description

The program provides two main functions:
1. **Encode**: Converts normal text into a secret code
2. **Decode**: Converts the secret code back to normal text

## Encoding Rules

The encoding process follows these rules:
- For words longer than 3 characters:
  1. Move the first letter to the end
  2. Add 'uon' at the start
  3. Add 'acs' at the end
- For words 3 characters or shorter:
  - Simply reverse the word

## Decoding Rules

The decoding process reverses the encoding:
- For words longer than 3 characters:
  1. Remove 'uon' from start and 'acs' from end
  2. Move the last letter to the front
- For words 3 characters or shorter:
  - Reverse the word back to original

## How to Use

1. Run the program:
```bash
python main.py
```

2. Choose your operation:
   - Enter 'e' to encode a message
   - Enter 'd' to decode a message
   - Enter 'quit' to exit the program

## Example Usage

```
Do you want to encode or decode a message or quit the program? (e/d/quit): e
Enter your message: HELLO
Encoded message: uonELLOHacs

Do you want to encode or decode a message or quit the program? (e/d/quit): d
Enter your encoded message: uonELLOHacs
Decoded message: HELLO
```

## Features

- Interactive command-line interface
- Error handling for invalid inputs
- Support for both short and long words
- Case-insensitive processing
- Continuous operation until user chooses to quit

## Error Handling

The program includes error handling for:
- Invalid user inputs
- Encoding/decoding errors
- Program termination 