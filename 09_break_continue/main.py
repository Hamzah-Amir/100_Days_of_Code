# Break and Continue in Python
# This file shows how to use break and continue statements

# Example 1: Break Statement
print("Example 1 - Break Statement:")
for i in range(5):
    if i == 3:
        print("Breaking the loop!")
        break
    print(f"Number: {i}")

# Example 2: Continue Statement
print("\nExample 2 - Continue Statement:")
for i in range(5):
    if i == 2:
        print("Skipping 2!")
        continue
    print(f"Number: {i}")

# Example 3: Break in While Loop
print("\nExample 3 - Break in While Loop:")
count = 0
while True:
    if count == 3:
        print("Breaking the while loop!")
        break
    print(f"Count: {count}")
    count += 1 