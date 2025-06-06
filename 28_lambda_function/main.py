# Our old approach to make simple expression functions like this one
def cube(x):
    return x*x*x

# We can use a lambda function to achieve the same result in a more concise way
cube = lambda x: x*x*x
print(cube(3))

# We can also use lambda functions to create more complex expressions
def add(x, y):
    return x + y

add = lambda x, y: x + y
print(add(3, 4))

# Note only use lamba functions for simple expressions

a = lambda x,y,z: x+y-z

print(a(5,85,2))

      