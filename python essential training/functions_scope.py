
#locals: num1, num2 and operation, those are the variables available locally inside the function
def performOperation(num1, num2, operation='sum'):
    print(locals()) 

#performOperation(1,2,operation='multiply') #print the dictionary: {'num1': 1, 'num2': 2, 'operation': 'multiply'}


#globals: variables definedl in the main body of the code, outside functions
#print(globals())
message = 'Some global data'
varA = 10
def func1(varA, varB):
    print(message)
    print(locals())

def func2(varC, varB):
    print(message)
    print(locals())

func1(1,2) #print {'varA': 1, 'varB': 2}
func2(3,4) #print {'varC': 3, 'varB': 4}

