from dataclasses import dataclass

@dataclass
class Human:
    name : str
    gender : str
    nation : str

    def id(self):
        print(f"{self.name} is a {self.gender} and is {self.nation}")
    
    @classmethod
    def change_nation(self, new_nation):
        self.nation = new_nation

hamza = Human("Hamza", 'Male', 'Pakistani')
hamza.id()

# If i will call change nation method it will change nationality
hamza.change_nation("Irani") # But it ill not change value of the nation variable at class level it only changes it in instance level 
hamza.id()

# To change it on class level we have to use class method decorator.
print(Human.nation)