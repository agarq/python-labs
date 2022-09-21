#INSTANCE ATTRIBUTES

class Dog:
    def __init__(self, name): #constructor
        #instance attributes: name and legs
        self.name = name 
        self.legs = 4
    
    def speak(self):
        print(self.name + ' says: Bark !')

my_dog = Dog('Rover')
print(my_dog.name)
print(my_dog.legs)

#STATIC ATTRIBUTES
#Also called static variables in the sense that they're unchanging with each instance. They're not dynamic. They're static.
#Traditionally, static variables are used to hold constants in fundamental business logic, and that sort of thing, 
# but be careful because just like any variable, you can reset it on the class
class Dog:
    _legs = 4 #this is a static attribute. Underscore as a convention

    def __init__(self, name): #constructor
        #instance attributes: name and legs
        self.name = name 
    
    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + ' says: Bark !')

my_dog = Dog('Rover')
print(my_dog.name)

print(my_dog.getLegs())
# You can see that we're changing the instance variable, _legs, but not the class variable. That remains the same.
my_dog._legs = 3
print(Dog._legs) #print 4
print(my_dog.getLegs()) #print 3