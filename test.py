a = 30
#example 1
if a < 5:
    print('a < 5')
else:
    print('a >= 5')
 
 
#example 2
if a < 5:
    print('a < 5')
else:
    if a < 10:
        print('5 <= a <= 10')
    else:
        print('a >= 10')

#example 3
if a < 5:
    print('a < 5')
elif a < 10:
    print('5 <= a <= 10')
elif a >= 10:
    print('a >= 10')


#example 4: Conditional expression, also known as the ternary operator
a = 25

#turn this
if a < 5:
    b = 'a < 5'
else:
    b = 'a >= 5'

print(b)

#into this with the conditional expression

b = 'a < 5' if a < 5 else 'a >= 5'

print(b)
