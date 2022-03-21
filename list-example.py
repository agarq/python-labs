# Python3 code here creating class
'''
class Geeks:
    def __init__(self, name="", roll=""):
        self.name = name
        self.roll = roll

# creating list
list = []

# appending instances to list
list.append(Geeks('cero', 0))
list.append(Geeks('uno', 1))
list.append(Geeks('dos', 2))
list.append(Geeks('tres'))

list.insert([4]['cuatro',4])

for obj in list:
    print(obj.name, obj.roll, sep=';')

# We can also access instances attributes
# as list[0].name, list[0].roll and so on.

print('name index 2: {}'.format(list[2].name))
print('roll index 2: {}'.format(list[2].roll))
'''

list = ['Instance Id;Volume Id;Snapshot Id;Start Time (UTC);Progress;State;State Message;Volume Size (GiB);Encrypted']

list.append('11111111;3333333')

for item in list:
   print(item)



print(list)
