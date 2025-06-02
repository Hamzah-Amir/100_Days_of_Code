# Python OS Module

The `os` module in Python provides a way to interact with the operating system. It offers functions for file and directory operations, path manipulations, and system information.

## Important Functions

### Directory Operations
```python
os.getcwd()          # Get current working directory
os.chdir(path)       # Change current directory
os.listdir(path)     # List contents of directory
os.mkdir(path)       # Create new directory
os.rmdir(path)       # Remove directory
```

### File Operations
```python
os.remove(path)      # Delete a file
os.rename(src, dst)  # Rename file/directory
os.path.exists(path) # Check if path exists
```

### Path Operations
```python
os.path.join(path1, path2)  # Join paths
os.path.isfile(path)        # Check if path is file
os.path.isdir(path)         # Check if path is directory
```

### System Information
```python
os.name              # Operating system name
os.getenv(var)       # Get environment variable
os.sep               # Path separator
```

## Common Use Cases
- File and directory management
- Path manipulation
- System information retrieval
- Environment variable access
- Directory navigation 