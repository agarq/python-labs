from decimal import Decimal, getcontext

#INT
print (int(20 / 5)) #returns 4.0

#casting
print (int(20 / 5)) #returns 4

#when you cast from float to string, Python does not round for you
print (int(8.9999999)) #returns 8 although it's closer to 9

#round function
print (round(8.9999999)) #returns 9

#we can pass to round the amount of decimal places we want to round
print (round(14/3, 2)) #returns 4.67

#FLOATS, are aproximations
print (1.2 - 1.0) #returns 0.19999999999999996
print (14/3) #returns 4.666666666666667


#DECIMAL
#we have to import Decimal at the top of the script

getcontext().prec = 4

print(Decimal(1) / Decimal(3)) #returns 0.3333 -> a decimal with precision 4

getcontext().prec = 2

print(Decimal(1) / Decimal(3)) #returns 0.33 -> a decimal with precision 2
