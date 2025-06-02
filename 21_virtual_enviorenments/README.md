# Python Virtual Environments (venv)

A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. Virtual environments help isolate project dependencies and avoid conflicts between different projects.

## Why Use Virtual Environments?

- **Isolation**: Each project can have its own dependencies, regardless of what dependencies every other project has.
- **Clean Environment**: Start with a clean Python installation and add only what you need.
- **Dependency Management**: Easily manage project-specific packages.
- **Version Control**: Different projects can use different versions of the same package.

## Creating a Virtual Environment

### Windows
```bash
# Create a new virtual environment
python -m venv myenv

# Activate the virtual environment
myenv\Scripts\activate

# Deactivate when done
deactivate
```

### macOS/Linux
```bash
# Create a new virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Deactivate when done
deactivate
```

## Common Commands

1. **Create a new virtual environment**:
   ```bash
   python -m venv myenv
   ```

2. **Activate the environment**:
   - Windows: `myenv\Scripts\activate`
   - macOS/Linux: `source myenv/bin/activate`

3. **Install packages**:
   ```bash
   pip install package_name
   ```

4. **List installed packages**:
   ```bash
   pip list
   ```

5. **Create requirements.txt**:
   ```bash
   pip freeze > requirements.txt
   ```

6. **Install from requirements.txt**:
   ```bash
   pip install -r requirements.txt
   ```

## Best Practices

1. **Create a new virtual environment for each project**
   - This keeps dependencies isolated and prevents conflicts

2. **Always activate the virtual environment before working on your project**
   - You'll know it's activated when you see `(myenv)` at the start of your command prompt

3. **Keep requirements.txt updated**
   - This makes it easy for others to recreate your environment
   - Makes deployment easier

4. **Don't commit the virtual environment to version control**
   - Add `myenv/` to your `.gitignore` file
   - Instead, commit `requirements.txt`

## Example Project Structure
```
my_project/
│
├── myenv/                  # Virtual environment (not committed to git)
├── src/                    # Source code
├── tests/                  # Test files
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Common Issues and Solutions

1. **Command not found: activate**
   - Make sure you're using the correct path to the activate script
   - Check if the virtual environment was created successfully

2. **Package installation fails**
   - Ensure the virtual environment is activated
   - Check your internet connection
   - Verify you have the necessary permissions

3. **Python version mismatch**
   - Create the virtual environment with the correct Python version
   - Use `python3 -m venv` if you have multiple Python versions installed

## Additional Resources

- [Python venv Documentation](https://docs.python.org/3/library/venv.html)
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [Python Packaging User Guide](https://packaging.python.org/) 