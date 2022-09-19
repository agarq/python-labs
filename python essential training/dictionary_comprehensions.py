#dictionary_comprehensions

animal_list = [('a', 'aardvark'), ('b','bear'), ('c', 'cat'), ('d', 'dog')]

animals_dict = {item[0]: item[1] for item in animal_list}

print(animals_dict) #print {'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

#a better way to write the comprehension
animals_dict = {key: value for key, value in animal_list}

print(animals_dict) #print {'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

#take the dictionary and convert it back into a list

print(animals_dict.items()) #print type dict_items


values = [[1, 'i', 'a'], ['2', 'we', 'be', 'it'], [3, 'are', 'few', 'too']]

print({item[0]: item[1:] for item in values})