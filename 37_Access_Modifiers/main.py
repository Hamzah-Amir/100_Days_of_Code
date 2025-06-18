from dataclasses import dataclass
@dataclass
class Person:
    name = "John"
    age = 30

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

john = Person()
print("\n")
john.greet()
# Accessing the attributes directly
print(john.name)  # Output: John
 # in python there is no public or private access modifier but there is a convention
# to indicate that an attribute is private by prefixing it with double underscore

@dataclass
class Person:
    __name = "John"
    __age = 30

    def greet(self):
        print(f"Hello, my name is {self.__name} and I am {self.__age} years old.")

print("\nAccessing private attributes:")
human = Person()
try:
    print(human.__name)  # This will raise an AttributeError
except AttributeError as e:
    print(e)

# we can access this attribute using the name mangling technique
# Method of doing so is:
# instance name._class_name__attribute_name
print("\nAccessing through name mangling")
print(human._Person__name)  # Output: John
print(human._Person__age)   # Output: 30