# While Loops in Python
# This file shows different ways to use while loops

# Example 1: Basic While Loop
print("Example 1 - Basic While Loop:")
count = 1
while count <= 3:
    print(f"Count is: {count}")
    count += 1

# Example 2: While Loop with Break
print("\nExample 2 - While Loop with Break:")
number = 1
while True:
    if number > 3:
        break
    print(f"Number: {number}")
    number += 1

# Example 3: While Loop with Continue
print("\nExample 3 - While Loop with Continue:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping 3!")
        continue
    print(f"Count: {count}")

# Example 4: While Loop with User Input
print("\nExample 4 - While Loop with User Input:")
# Uncomment to run this example
# password = ""
# while password != "secret":
#     password = input("Enter password: ")
# print("Access granted!")

# Example 5: While Loop with List
print("\nExample 5 - While Loop with List:")
fruits = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits):
    print(f"Fruit at index {index}: {fruits[index]}")
    index += 1 