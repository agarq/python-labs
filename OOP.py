'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof woof!")

mydog = Dog("Paco", 2) #fido is an instance of the Dog class
mydog.bark()
print(mydog.name)
print(mydog.age)
'''

class Dog(): #parent class or super class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name," is barking!")
    
    def addOneYear(self):
        self.age += 1
    
    def getInfo(self):
        print(self.name, "is", self.age, "years old.")
    
class Poodle(Dog): #child class or subclass
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight

    def bark(self, manner="energerically"): #this method is overwritten
        print(f"{self.name} is barking {manner}")
    
    def getInfo(self):
        print(f"{self.name} is a {self.age} years old, {self.color} poodle and weights {self.weight} pounds.")

class Corgi(Dog): #child class or subclass
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    
    def bark(self, manner="briefly"): #this method is overwritten
        print(f"{self.name} is barking {manner}")
    
    def getInfo(self):
        print(f"{self.name} is a {self.age} years old, {self.color} corgi and weights {self.weight} pounds.")

ella = Dog("Ella", 3.5) # ella is an instance of Dog
ella.getInfo()
ella.bark()
ella.addOneYear()
ella.getInfo()

ella = Poodle("Ella", 1.5, "grey", 40)
ella.getInfo()
ella.bark()
ella.addOneYear()
ella.getInfo()

bruno = Corgi("Bruno", 1.5, "grey", 40)
bruno.getInfo()
bruno.bark()
bruno.addOneYear()
bruno.getInfo()