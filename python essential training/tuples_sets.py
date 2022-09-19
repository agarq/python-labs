#SETS
from typing import MutableSequence


myset = {'a','b','c'}
print (myset)

#remove duplicates from list:
mylist = ['a','b','b','c','c']
mylist = list(set(mylist))

print(mylist)

#we can add items to a set
myset.add('d')
print (myset)

print('a' in myset) #prints True

#we can get the length of a set
print (len(myset)) #prints 4

while(len(myset)):
    print(myset.pop()) #prints with no order and empty the set

print (myset)

myset = {'a','b','c'}

# to delete a particular element from the set
myset.discard('a')
print (myset) #print {'b', 'c'}


#TUPLES
mytuple = ('a','b','c')
print (mytuple)

print(mytuple[0]) #prints a

#Tuple does not support item assignment
#mytuple[0] = 'd' #this throws an error: 

def returnsMultipleValues():
    return 1,2,3

print(type(returnsMultipleValues())) #print <class 'tuple'>

a, b, c = returnsMultipleValues()

print(a) #print 1
print(b) #print 2
print(c) #print 3