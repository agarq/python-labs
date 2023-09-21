
#LISTS: sequence with a specific order, items can be updated after creation.
name = "Brad" #string
group = ["Daniel","Luis","Ricardo","Jose","Pedro","Marvin"] #list, is a kind of sequence. Sequence is collection of data.

print(type(name)) #str
print(type(group)) #list

listA = [5, 10, 15, 20]
print(listA)
print(type(listA))
print(listA[0]) #first item

#update the 3rd item in the list
listA[2] = 150
print(listA)

# items in List could have different data types
listB = [True, "star", 5, 22.4]
print(listB)

#TOUPLES. sequence with specific order.  Items cannot be changed after creation. Parenthesis are used to enclose the items.
child1_birth = ("Julia", "Hospital 1", "Medellin", "Colombia", "07/29/2019", "09:42")
child2_birth = ("Andres", "Hospital 2", "Cali", "Colombia", "07/28/2019", "16:25")

print(type(child1_birth))
print(type(child2_birth))

print(child1_birth)
print(child2_birth)

print(child1_birth[0]) #to print the name


