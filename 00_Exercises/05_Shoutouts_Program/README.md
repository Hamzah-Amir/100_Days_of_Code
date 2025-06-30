# Shoutouts Program

This Python program gives shoutouts to a list of people using your computer's speech engine.

## How it works
- Uses the `win32com.client` library to access Windows' text-to-speech (SAPI).
- Iterates through a list of names and speaks a shoutout for each.

## Requirements
- Windows OS
- Python 3.6 or higher
- `pywin32` package (`pip install pywin32`)

## How to run
```sh
python main.py
``` 