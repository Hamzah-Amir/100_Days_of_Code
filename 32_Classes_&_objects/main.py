class Human:
    name = "Hamza"
    age = 18
    occupation = "Software Engineer"
    country = "Pakistan"
    def info(self):
        return f"{self.name} is a {self.age}-year-old {self.occupation} from {self.country}."

person = Human()
# print(f"Name: {person.name}")
# print(f"Age: {person.age}") 
# print(f"Occupation: {person.occupation}")
# print(f"Country: {person.country}")  
print(person.info())
# If i want to change the name of the person
person.name = "Ali" # Similarly we can change age, occupation and country
print(person.name) # Now it will print "Ali"