#SLICING LISTS

my_list = [1,2,3,4,5]

print(my_list[3:]) #returns [4, 5]
print(my_list[0:6:2]) #returns [1, 3, 5] - last parameter indicates every other number, equivalent to [::2]
print(my_list[0:6:3]) #returns [1, 4]

#we can use range to create a bigger lists
#for i in range(100):
#    print (i) #prints number from 0 to 99

#we can cast that range to a list
my_list = list(range(100))
print(my_list[::5]) #will print steps of 5 in the list from 0 to 95

print(my_list[::-1]) #will print the list backwards, from 99 to 0


#MODIFYING LISTS
my_list = [1,2,3,4]
my_list.append(5) #will add 5 at the end of the list
print(my_list)

#to insert an item at any position, use insert
my_list.insert(3,'a new value')
print(my_list) #prints [1, 2, 3, 'a new value', 4, 5]

#to remove items from a list. If the item is not in the list, will throw an error
my_list.remove('a new value')
print(my_list)

#other way to remove is using pop, to remove the item at the end of the list
var = my_list.pop() #a will get the value of 5
print (var)
print(my_list) #prints [1, 2, 3, 4]

while len(my_list):
    print(my_list.pop()) #will print each item starting from the end, while it's removing it from the list

print(my_list) #prints an empty list

a = [1,2,3,4,5]
b = a
a.append(6)
print(b) #prints [1,2,3,4,5,6]

c = [1,2,3,4,5]
d = c
a.append(6)
print(b) #prints [1,2,3,4,5,6]