#1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16 ...

#if else statements

from http.client import SWITCHING_PROTOCOLS


for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    else:
        if n % 3 == 0:
            print('Fizz')
        else:
            if n % 5 == 0:
                print('Buzz')
            else:
                print(n)

#Elif

for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

#single line If statement
print('******')
n = 5
print('Fizz' if n % 3 == 0 else n)

# In programming, this is what's known as a ternary operator, so a ternary operator takes in some boolean condition, 
# in this case, n modulus three is equal to zero, evaluates it and returns one value if the condition is true, 
# and then another value if the condition is false.
myvar = 'Fizz' if n % 3 == 0 else n
print(myvar)

myvar = 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n
print(myvar)

#same example with the for using ternary operator
print(['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1,101)])
