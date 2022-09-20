import math

def performOperation(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    elif operation == 'multiply':
        return num1 * num2

print(performOperation(2, 4, 'multiply'))

#named parameters, optional parameter
def performOperation2(num1, num2, operation='sum'):
    if operation == 'sum':
        return num1 + num2
    elif operation == 'multiply':
        return num1 * num2

print(performOperation2(2, 4)) #print 6 because I'm not sending the operation parameter value

# *args, it's a pointer to the values are passed in
def performOperation3(*args):
    print(args)

performOperation3(1,2,3)
#performOperation3(1,2,3,operation='sum') #this throws an error


# *kargs, it's a pointer to the values are passed in
def performOperation4(*args, **kargs):
    print(args) #print (1, 2, 3), it's a tuple
    print(kargs) #print {'operation': 'sum'}, it's a dictionary

performOperation4(1,2,3)
performOperation4(1,2,3,operation='sum')

def performOperation5(*args, operation='sum'):
    if operation == 'sum':
        return sum(args)
    elif operation == 'multiply':
        return math.prod(args)

print(performOperation5(3,4,1,2,operation='multiply'))