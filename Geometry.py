import math as m
from random import randint

# Defining Functions and Objects
class Vector:
    
    def __init__(self,x=0,y=0,z=0,w=1) -> None:
        self.x = float(x)
        self.y = float(y) 
        self.z = float(z)
        self.w = float(w)

    def Normalize(self):
        len = (self.x**2 + self.y**2 + self.z**2) ** 0.5
        if len != 0:
            self.x /= len
            self.y /= len
            self.z /= len
     
    def Make3D(self):
        if self.w != 0:    
            self.x /= self.w
            self.y /= self.w
            self.z /= self.w
            self.w /= self.w
        else: print('W is 0')

    def Tuple(self):
        return (self.x,self.y,self.z)
    
    @classmethod
    def Random2D(cls, min_val=-1, max_val=1):
        x = randint(min_val * 500, max_val * 500) / 500
        y = randint(min_val * 500, max_val * 500) / 500
        return cls(x, y, 0, 1)

    @classmethod
    def TwoPoint(cls, point1, point2):
        return cls(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)
    
    def __add__(self,other : 'Vector')-> 'Vector':
        return Vector(
            self.x+other.x,
            self.y+other.y,
            self.z+other.z)
    
    __radd__ = __add__
    
    def __sub__(self,other : 'Vector')-> 'Vector':
        return Vector(
            self.x-other.x,
            self.y-other.y,
            self.z-other.z)
    
    __rsub__ = __sub__

    def __matmul__(self,other:'Vector')-> 'Vector': #CROSS PRODUCT
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x)
    
    def __mul__(self,other: float)-> 'Vector':
        return Vector(self.x * other ,self.y * other ,self.z * other)
    
    __rmul__ = __mul__

    def __pow__(self,other:'Vector')-> float: #DOT PRODUCT
        return self.x*other.x+self.y*other.y+self.z*other.z
    
    def __str__(self):
        self.Make3D
        self.Make3D()
        return f"({self.x},{self.y},{self.z})"
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y}, z={self.z}, w={self.w})"

class Plane():
    def __init__(self,normal : Vector,point : Vector):
        self.normal = normal
        self.point = point
        normal.Normalize()
        self.distance = - normal**point
    
    def classify_point(self,point : Vector):
        return (self.normal**point) + self.distance
    
    def interpolate_point(self,t : float,start : Vector,end : Vector):
        return start + (end - start)*t
  
if __name__ == '__main__':

    print('run D_Engine not Geometry file')