from abc import ABC,abstractmethod
#ABC is a Class and abc is a module
class Shape(ABC):
    @abstractmethod   #eta likhleo o/p asbe na likhleo asbe
    def __init__(self):
        pass
class Rect(Shape):
    def __init__(self,a=0,b=0):
        ar=a*b
        print("area of the rectangle=",ar)
class Square(Shape):
    def __init__(self,a=0):
        ar=a**2
        print("area of square:",ar)
class Circle(Shape):
    def __init__(self,a=0,b=0.0):
        ar=b*a*a
        print("area of circle: ",ar)
r=Rect(10,20)
s=Square(10)
c=Circle(10,3.14)
        
