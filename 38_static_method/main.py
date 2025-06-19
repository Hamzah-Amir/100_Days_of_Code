from dataclasses import dataclass

@dataclass
class Mathematics:
    num:int

    def addtonum(self, n):
        self.num = self.num + n
        return print(self.num)
    
    @staticmethod
    def add(a,b):
        return print(a+b)
    
a = Mathematics(6)
a.addtonum(3)

Mathematics.add(3, 4)  # Static method can be called without an instance

# Static method are just used when if we want that person to whom i am sharing my code or the class should be able to use the method without creating an instance of the class.