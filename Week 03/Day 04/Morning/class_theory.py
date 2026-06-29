#         ============================ Inheritance =========================
#   topics : Inheritance (single, multilevel, hirerachial, multiple) , method overriding



class Animal:                       # Parent / Base class
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound


    def speak(self):
        return f"{self.name} says {self.sound}"


    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):                          #Child/Derived class
    def __init__(self, name, breed):
        super().__init__(name, "woof")
        self.breed=breed

    def fetch(self):
        return f"{self.name} fetches the ball ! "


d=Dog("Bruno","Labrador")
print(d.speak())
print(d.fetch())


#         ============================ Method Overriding =========================
class Shape:
    def __init__(self,color="white"):
        self.color=color

    def area(self):
        return 0

    def describe(self):
        return f"{self.color} shape , area={self.area():.2f} "

class Circle(Shape):
        def __init__(self,radius,color="blue"):
            super().__init__(color)
            self.radius=radius

        def area(self):
            return 3.14159*self.radius**2

    
        

class Rectangle(Shape):
    def __init__(self,w,h,color="red"):
        super().__init__(color)
        self.w,self.h=w,h

    def area(self):
        return self.w*self.h


shapes=[Circle(5),Rectangle(4,6)]
for sh in shapes:
    print(sh.describe())            # polymorphic call