# walrus operator is used to assign a value to a variable as part of an expression
# Example: Using the walrus operator to assign a value to a variable in a list comprehension

numbers = [1, 2, 3, 4, 5]

while (n:= len(numbers)) > 0:
    print(f"length of numbers: {n}")
    numbers.pop()
print("No number left in list")
# The walrus operator allows us to assign the length of the list to n and use it in the while condition

foods = []
while (food := input('WHat food do you like: ')) != 'quit':
    foods.append(food)