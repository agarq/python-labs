import math
#SLICING
name = 'My name is James Bond'
print (name[0]) #returns 'M'
print (name[0:7]) #returns 'My name'. Is equivalent to name[:7]
print (name[11:]) #returns 'James Bond'

my_list = [1,2,3,4,5]

print(my_list[2:4]) #returns [3, 4]

#length of a string
print(len(name))


#FORMATTING
print('My number is: ' + str(5))
print(f'My number is {5} and twice that is {2*5}')
print(f'PI is {math.pi:.2f}') #you have to import math at the top of the script

print('PI is {}'.format(math.pi))

#MULTI-LINE STRINGS with triple quotes
str = '''
Here is a long block of text
I can add new lines
The text doesn't stop until it find triple quotes (\'\'\')
'''
print (str)