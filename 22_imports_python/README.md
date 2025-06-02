# Python Imports

This guide covers different ways to import modules and packages in Python, along with best practices and common patterns.

## Basic Import Statements

### 1. Importing an Entire Module
```python
import math
# Usage
result = math.sqrt(16)
```

### 2. Importing Specific Items
```python
from math import sqrt, pi
# Usage
result = sqrt(16)
print(pi)
```

### 3. Importing with Aliases
```python
import numpy as np
# Usage
array = np.array([1, 2, 3])
```

## Advanced Import Techniques

### 1. Importing Multiple Items
```python
from math import (
    sqrt,
    pi,
    sin,
    cos
)
```

### 2. Importing All Items (Not Recommended)
```python
from math import *  # Imports all public items
```

### 3. Relative Imports
```python
# Inside a package
from . import module_name  # Import from same directory
from .. import module_name  # Import from parent directory
```

## Import Best Practices

1. **Be Specific with Imports**
   - Prefer `from module import specific_item` over `import *`
   - Makes code more readable and explicit

2. **Use Aliases for Long Module Names**
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   ```

3. **Group Imports**
   ```python
   # Standard library imports
   import os
   import sys
   
   # Third-party imports
   import numpy as np
   import pandas as pd
   
   # Local application imports
   from mypackage import mymodule
   ```

4. **Avoid Circular Imports**
   - Restructure code to prevent circular dependencies
   - Use lazy imports when necessary

## Common Import Patterns

### 1. Conditional Imports
```python
try:
    import numpy as np
except ImportError:
    print("NumPy is required for this functionality")
```

### 2. Lazy Imports
```python
def my_function():
    import heavy_module  # Only imported when function is called
    return heavy_module.do_something()
```

### 3. Importing from Parent Directory
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

## Package Structure Example
```
my_package/
│
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

## Common Issues and Solutions

1. **ModuleNotFoundError**
   - Check if the module is installed
   - Verify the Python path
   - Check for typos in module names

2. **ImportError**
   - Check for circular imports
   - Verify module dependencies
   - Check for version conflicts

3. **AttributeError**
   - Verify the imported item exists
   - Check for typos in attribute names

## Best Practices for Package Development

1. **Use `__init__.py` Files**
   - Makes directories into packages
   - Can be used to expose specific items

2. **Version Your Packages**
   ```python
   # In __init__.py
   __version__ = '1.0.0'
   ```

3. **Document Your Imports**
   - Add comments explaining non-obvious imports
   - Document version requirements

## Additional Resources

- [Python Import System Documentation](https://docs.python.org/3/reference/import.html)
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/#imports)
- [Python Packaging User Guide](https://packaging.python.org/) 