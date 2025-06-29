class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary


class Programmer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)  # Using super() to call the parent class constructor
        self.programming_language = programming_language

hamza = Programmer("Hamza", 5000, "Python")
print(f"Name: {hamza.name}, Salary: {hamza.salary}, Programming Language: {hamza.programming_language}")