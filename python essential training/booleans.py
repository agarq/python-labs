#CASTING BOOLEANS
print (bool(1)) #returns True
print (bool(0)) #returns False
print(bool(-1)) #returns True
print(bool(1j)) #returns True
print (bool(0.0)) #returns False
print (bool(0j)) #returns False
print(bool('True')) #returns True
print(bool('False')) #returns True
print(bool('')) #returns False. Empty string, list, or dictionary is false.

print(bool(None)) #returns False

my_list = [1,2,3]
if my_list: #or you can use casting: if bool(my_list)
    print('my_list has some values in it.')

a = 4
b = 4
if a - b: #the only way taht a - b evaluates to zero or False, is if a is equal to b
    print ('a and b are not equal')

#BOOLEAN LOGIC

weather_is_nice = True
have_umbrella = False

if have_umbrella or weather_is_nice:
    print('Go for a walk')
else:
    print('Stay at home')
