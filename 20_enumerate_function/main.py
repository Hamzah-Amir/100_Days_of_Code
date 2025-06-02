fruits = ['apple','mango','banana','pineapple','peach','guava']
# to do a particular task when loop reaches to given index we have to do this

print("\n-------First Example-------")
index = 0
for fruit in fruits:
    print(fruit)
    if (index == 4):
        print(f"The fruit {fruit} is at index {index}")
    index += 1
# or we can use enumerate function to get index and value at the same time
print("\n-------Second Example-------")
for index,fruit in enumerate(fruits):
    print(fruit)
    if (index == 5):
        print(f"The fruit {fruit} is at index {index}")

# if we want that indexing should start from 1 instead of 0 we can do this
print("\n-------Third Example-------")
for index,fruit in enumerate(fruits, start=1):
    print(fruit)
    if (index == 6):
        print(f"The fruit {fruit} is at index {index}")