# Creating a Command Line Utility in Python

This guide will walk you through creating a command line utility in Python using the `argparse` and `requests` modules. By the end, you'll be able to build a simple CLI tool that takes user input and fetches data from the internet.

## Prerequisites
- Python installed (version 3.6 or above recommended)
- Basic knowledge of Python

## Step 1: Set Up Your Project
1. Create a new directory for your project.
2. Inside the directory, create a file named `main.py`.

## Step 2: Install Required Modules
- `argparse` is part of the Python standard library, so no installation is needed.
- Install `requests` using pip:

```bash
pip install requests
```

## Step 3: Import Modules in Your Script
In your `main.py`, import the necessary modules:

```python
import argparse
import requests
```

## Step 4: Set Up Argument Parsing
Use `argparse` to handle command line arguments:

```python
parser = argparse.ArgumentParser(description='A simple CLI utility')
parser.add_argument('url', type=str, help='The URL to fetch data from')
args = parser.parse_args()
```

## Step 5: Make a Request Using `requests`
Fetch data from the provided URL:

```python
response = requests.get(args.url)
print('Status Code:', response.status_code)
print('Content:', response.text[:200])  # Print first 200 characters
```

## Step 6: Run Your Utility
In your terminal, run:

```bash
python main.py https://example.com
```

You should see the status code and the first 200 characters of the page content.

## Step 7: Add More Features (Optional)
- Add more arguments (e.g., HTTP method, headers)
- Handle errors and exceptions
- Format the output

## Example: Full Script
```python
import argparse
import requests

parser = argparse.ArgumentParser(description='A simple CLI utility')
parser.add_argument('url', type=str, help='The URL to fetch data from')
args = parser.parse_args()

try:
    response = requests.get(args.url)
    print('Status Code:', response.status_code)
    print('Content:', response.text[:200])
except Exception as e:
    print('An error occurred:', e)
```

---

With these steps, you can create and expand your own command line utilities in Python using `argparse` and `requests`! 