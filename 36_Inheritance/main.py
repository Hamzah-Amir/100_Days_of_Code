from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    id: int
    salary: int

    def display(self):
        return print(f"Name: {self.name}, Age: {self.id}, Salary: {self.salary}")

print("\n---Example 1----\n")
hamza = Employee(name="Hamza", id=1, salary=1000)
hamza.display()
# All things are good till now
# Consider now i want to make a programming language class or Post class that which employee is at which Post 
# What should i do create another class and defining all things we can do it but the convenient way is to use inheritance
# All classes like programming language and empolyee post will contain name of employee and id as well so we can inherit those property from the parent class Employee

@dataclass
class EmployeePost(Employee):
    post: str

    def display(self):
        return print(f"Name: {self.name}, Id: {self.id} is a {self.post}.")

print("\n---Example 2----\n")
hamza_post = EmployeePost(name="Hamza", id=1,salary=1000, post="Software Engineer")
hamza_post.display()

# Similarly for programming language
#Now we will inherit from EmployeePost class and add programming language property to it
@dataclass
class EmployeeProgrammingLanguage(EmployeePost):
    programming_language: str

    def display(self):
        return print(f"Name: {self.name}, is a {self.post} and works with {self.programming_language}.")

print("\n---Example 3----\n")
hamza_programming_language = EmployeeProgrammingLanguage(name="Hamza", id=1, salary=1000, post="Software Engineer", programming_language="Python")
hamza_programming_language.display()