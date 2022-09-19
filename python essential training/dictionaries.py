#DICTIONARIES
from collections import defaultdict

animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat', #this comma is optional, but it's a good practice
}

print(animals)

print(animals['a'])

animals['d'] = 'dog'

print(animals)

animals['a'] = 'antelope'

print(animals)

print(animals.keys())
print(animals.values())

print(list(animals.keys())) #converts the dict_keys object to a list

#function get to return the value of a key
print(animals.get('e')) #print None because e doesn't exist in the dictionary
print(animals.get('d')) #print dog

#get the lenght of the dictionary
print(len(animals))

#dictionary of Lists
animals = {
    'a': ['aardvark','antelope'],
    'b': ['bear'],
}

print(animals) #print {'a': ['aardvark', 'antelope'], 'b': ['bear']}

#to add an item to the b values list
animals['b'].append('bison')

print(animals) #print {'a': ['aardvark', 'antelope'], 'b': ['bear', 'bison']}

#if I want to add a new key
animals['c'] = ['cat']
print(animals) #print {'a': ['aardvark', 'antelope'], 'b': ['bear', 'bison'], 'c': ['cat']}

#validate if the key exists in the dictionary
if 'c' not in animals:
    animals['c'] = []

animals['c'].append('cobra')
print(animals) #print {'a': ['aardvark', 'antelope'], 'b': ['bear', 'bison'], 'c': ['cat', 'cobra']}

#DEFAULT DICT
#we need to import the defaultdict from collections import defaultdict
#at the top of the script

animals = defaultdict(list)

animals['e'].append('elephant')
print(animals) #defaultdict(<class 'list'>, {'e': ['elephant']})

animals['e'].append('emu')
print(animals) #defaultdict(<class 'list'>, {'e': ['elephant', 'emu']})

animals['f']
print(animals) #no need to specify this is a list because of the defaultdict