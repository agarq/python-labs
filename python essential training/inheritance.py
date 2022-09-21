class Dog:
    _legs = 4 #this is a static attribute. Underscore as a convention

    def __init__(self, name): #constructor
        #instance attributes: name and legs
        self.name = name 
    
    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + ' says: Bark !')

class Chihuahua(Dog): #We use these parentheses after the class name to indicate that this class is extending the parent dog class
    def speak(self):
        print(f'{self.name} says: yap yap yap.')

    def wagTail(self):
        print('Vigorous wagging')


my_little_dog = Chihuahua('Roxy')
my_little_dog.speak()
print(my_little_dog.getLegs())
my_little_dog.wagTail()

my_dog = Dog('Rover')
my_dog.speak()

#EXTENDING BUILT-IN CLASSES

my_list = list() #list() is a Class

class UniqueList(list):
    def __init__(self):
        #. There's also another really common use case where super is used and that's in the constructor. 
        # So, say you want to add another attribute to your child class instance. 
        # So the problem is that we're completely overriding the constructor and the parent class now where it may have some 
        #  really important stuff that it needs to initialize. We can solve this by using super again. 
        # And this makes sure that the parent constructor gets called first. And then we add our new property someProperty. 
        # And we can see that when we instantiate it. 
        super().__init__()
        self.someProperty = 'Unique list !'

    def append(self, item):
        if item in self:
            return
        super().append(item) #super() gets the underlying instance of the parent class (the list() class)

unique_list = UniqueList()
unique_list.append(1)
unique_list.append(1)
unique_list.append(1)
unique_list.append(2)

print(unique_list)
print(unique_list.someProperty)
