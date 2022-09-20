#Lambda functions
# - Convinient way to write "mini funcitons" as values
# - 

(lambda x: print(x + 3))(5)

my_list = [5,1,4,2,3]
print(sorted(my_list))

my_list = [{'num': 2},{'num': 3}, {'num': 1}]

print(sorted(my_list, key=lambda x: x['num']))

def someFunc(func):
    print(func(5) + 2)

someFunc(lambda x: x * 3) #print 17