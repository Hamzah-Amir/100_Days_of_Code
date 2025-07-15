# Function Caching Example (functools.lru_cache)

This example demonstrates how to use Python's `functools.lru_cache` decorator to cache the results of an expensive function call.

## How It Works
- The `fx(n)` function simulates a time-consuming computation by sleeping for 3 seconds, then returns `n * 5`.
- The `@lru_cache(maxsize=None)` decorator caches the results of previous calls to `fx(n)`, so repeated calls with the same argument return instantly without delay.
- The script calls `fx` with several values, printing a message after each call to show when the computation is done.

## Usage
Run the script with:
```bash
python main.py
```
You will notice that the first call for each unique argument takes 3 seconds, but repeated calls with the same argument are instantaneous due to caching.

## Output Example
```
 done for 16
 done for 3
 done for 10
 done for 16
 done for 3
Done for 13 
 done for 10
```

## Requirements
- Python 3.x
- No external dependencies (uses standard library) 