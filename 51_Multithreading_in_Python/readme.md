# Multithreading Sleep Demo

This simple Python script demonstrates the use of **multithreading** to run functions concurrently using the `threading` module.

## Description

The script defines a function `func(sec)` that:
- Prints how many seconds it will sleep.
- Sleeps for the specified number of seconds using `time.sleep()`.

### Execution Flow

1. **Sequential Execution:**
   - The function is first called three times in a row: `func(3)`, `func(4)`, and `func(4)`.
   - These are executed **sequentially**, meaning the total sleep time is `3 + 4 + 4 = 11 seconds`.

2. **Concurrent Execution (Multithreading):**
   - Three threads (`t1`, `t2`, and `t3`) are created to run the `func` with arguments `4`, `2`, and `1` seconds respectively.
   - All threads are started using `.start()`, allowing them to run **concurrently**.
   - The main thread waits for all three to finish using `.join()`.

### Expected Output

The sequential part will output:
