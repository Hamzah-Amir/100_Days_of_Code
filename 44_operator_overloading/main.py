from dataclasses import dataclass
@dataclass
class Vector:
    i : int 
    j : int 
    k : int 

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}k + {self.k}k"
    
    def __add__(self, x): #here x is a recognition of another vector its name can vary
        return Vector(self.i+x.i, self.j+x.j, self.k+x.k)

v1 = Vector(5,6,7)
print(f"Vector 1: {v1}")

# Vector 2
v2 = Vector(8,9,10)
print(f"vector 2: {v2}")
# Consider i wnt to take resultant of these two vector
# print(v1 + v2) It will cause error because we cant add classes

# we can do it by adding __add__ method in class 

# now we can add these two to get resultant Vector
print(f"Resultant vector: {v1+v2}")
print(type(v1+v2)) # Its type is str we can type cast it to vector tyoe by th