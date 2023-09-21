a = 2
msj = "ex1: "
#example 1
if a < 5:
    print(msj + 'a < 5')
else:
    print(msj + 'a >= 5')

#example 2
msj = "ex2: "
if a < 5:
    print(msj + 'a < 5')
else:
    if a < 10:
        print(msj + '5 <= a <= 10')
    else:
        print(msj + 'a >= 10')

#example 3
msj = "ex3: "
if a < 5:
    print(msj + 'a < 5')
elif a < 10:
    print(msj + '5 <= a <= 10')
elif a >= 10:
    print(msj + 'a >= 10')


#example 4: Conditional expression, also known as the ternary operator
msj = "ex4: "
a = 25

#turn this
if a < 5:
    b = 'a < 5'
else:
    b = 'a >= 5'

print(b)

#into this with the conditional expression
msj = "ex5: "
b = 'a < 5' if a < 5 else 'a >= 5'

print(msj + b)

#name = input("What is your name: ")
#print (name)