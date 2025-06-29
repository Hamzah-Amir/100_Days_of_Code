from dataclasses import dataclass

@dataclass
class Shape:
    x: int
    y: int

    def area(self):
        return self.x * self.y

rec = Shape(10, 20)
print(f"Area of rectangle: {rec.area()}")
# Now consider i have to calculate radius of circle and its formula is pie * r * r.

@dataclass
class Circle(Shape):
    def __init__(self, radius: int):
        super().__init__(radius, radius)
    
    pie : float = 3.14

    def radius(self):
        return self.pie * super().area() # Using the area method from Shape to calculate the area of the circle
        # Area of circle = π * r^2, but here we use the area method from Shape to get r^2 
        # Here we override init method of parent class while it is not recommended to override init method of parent class as now we use dataclass decorator
        ## but for this example, we are doing it to show how to use the area method from Shape class.

circle = Circle(10)
print(f"Area of circle: {circle.radius()}")