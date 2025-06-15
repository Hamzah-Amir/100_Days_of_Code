class Person():
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def greet(self):
        print(f'{self.name} says hello!')
    
    def info(self):
        return print(f"{self.name} is {self.age} years old, and is  {self.nationality} citizen.")

a = Person("John", 30, "American")
a.greet()
a.info()