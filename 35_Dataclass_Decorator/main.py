from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int
    nationality:str
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Example usage
hamza = Person("Hamza", 18, "Pakistani")
print(hamza.greet()) #Instead of creating __init__ function we can use dataclass deocrator to create it automatically

# Here we have defined our variable and assign thier value while making an instance but we can also define its value inside class
@dataclass
class Person2:
    name:str = "Amir"
    age:int = 42
    nationality:str = "Pakistani"
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Example usage
print("----Example 2----")
amir = Person2()
print(amir.greet()) # We can also use greet function from Person class