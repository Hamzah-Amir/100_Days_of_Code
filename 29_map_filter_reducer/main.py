# Map method in Python
print("Map Method Examples in Python")
def square(x):
    return x * x
square(6) # It is simple
# What if we want to iterate list of int and square each element?
# old approach is using for loop
# but we will do it using map function
l = [5,6,8,1,2,7,3]
# using map function
newl = map(square,l)
print(newl) # it will return map object
# we can type cast it to get the list 
newl = list(newl)
print(newl)

# filter method in Python
# We will create a filter condition  function
print("Filter Method Examples in Python")
def filter_function(a): # This is the condition of filteration
    return a > 5

l = filter(filter_function, l) 
print(l) # it will return filter 
# typecasting it in a list
l = list(l)
print(l)  

print("Reduce Method Examples in Python")
from functools import reduce
num = [1,6,1,2,3,4,5]
def add(x,y):
    return x + y
s = reduce(add, num) # it will return a single value
# this reduce function will add each and single element of the list
print(s)