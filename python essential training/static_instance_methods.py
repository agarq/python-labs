import math

class Orientation:
    _pi = 3.14
    
    def __init__(self, x_pos, y_pos, degrees):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir, self.y_dir = Orientation.getUnitVectorFromDegrees(degrees)
    
    def getUnitVectorFromDegrees(degrees): #static method
        radians = (degrees/180) * Orientation._pi
        return math.sin(radians), -math.cos(radians)
    
    def getNextPos(self): #instance method
        return self.x_pos + self.x_dir, self.y_pos + self.y_dir

myOrientation = Orientation(5, 5, 75)

print(myOrientation.getNextPos())

#DECORATORS

class Orientation2:
    _pi = 3.14
    
    def __init__(self, x_pos, y_pos, degrees):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir, self.y_dir = self.getUnitVectorFromDegrees(degrees)
    
    @staticmethod #this is a decorator, the static method decorator
    def getUnitVectorFromDegrees(degrees): #static method
        radians = (degrees/180) * Orientation2._pi
        return math.sin(radians), -math.cos(radians)
    
    def getNextPos(self): #instance method
        return self.x_pos + self.x_dir, self.y_pos + self.y_dir

myOrientation = Orientation2(5, 5, 75)

print(myOrientation.getNextPos())