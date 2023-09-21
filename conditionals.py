'''
raining = input("Is it raining? (y/n)")
if raining == "y" or raining == "Y":
    print("You will need an Umbrella!")

n = input("Please enter a number between -10 and 10 here: ") #n is a string

n = int(n) #converted the response to an integer

if n < 5:
    print("the integer is less than 5.")
else:
    print("the integer is greater than 5.")

def minimum(x, y):
    if x < y:
        return x
    else:
        return y

result = minimum(2, 5)
print(result)
result = minimum(6, 3)
print(result)


raining = input("Is it raining? (y/n)")
umbrella = input("Do you have an Umbrella? (y/n)")
if raining.lower() == "y" and umbrella.lower() == "y":
    print("Don't forget your umbrella when you go out!")
elif raining.lower() == "y" and umbrella.lower() == "n":
    print("Wear a waterproof jacket when you go out!")


x = input("Enter a number: ")
x = float(x)

if x < 2:
    print(str(x) + " is less than 2.")
elif x < 6:
    print(str(x) + " is less than 6.")
elif x < 8:
    print(str(x) + " is less than 8.")

'''

def abs_val(num):
    if num < 0:
        return -1 * num
    elif num == 0:
        return 0
    else:
        return num

mynum = input("Enter an integer number: ")
mynum = int(mynum)
result = abs_val(mynum)
print("The absolute value of " + str(mynum) + " is " + str(result))
