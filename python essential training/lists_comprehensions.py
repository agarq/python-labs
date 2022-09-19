#lists_comprehensions: square brackets

mylist = [1,2,3,4,5]

print([2*item for item in mylist]) #square brackets surround the list comprehension, [2, 4, 6, 8, 10]


#list comprehensions with filters
mylist = list(range(100))

filteredlist = [item for item in mylist if item % 10 == 0] #print [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print(filteredlist)

#list comprehensions with functions

mystring = 'My name is James Bond, I live in Boston'

print(mystring.split(',')) #print ['My name is James Bond', ' I live in Boston']
print(mystring.split()) #print ['My', 'name', 'is', 'James', 'Bond,', 'I', 'live', 'in', 'Boston']

def cleanWord(word):
    return word.replace('.','').lower() #Calling one function after the other in a single line like this is called chaining functions.

print([cleanWord(word) for word in mystring.split()]) #print ['my', 'name', 'is', 'james', 'bond,', 'i', 'live', 'in', 'boston']

print([cleanWord(word) for word in mystring.split() if len(cleanWord(word)) < 3]) #print ['my', 'is', 'i', 'in']


#Nested list comprehensions

print([[cleanWord(word) for word in sentence.split()] for sentence in mystring.split(',')])

