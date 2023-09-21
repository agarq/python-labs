#check how many vowels are in a word
'''
word = "serendipitous"
vowels = ["a","e","i","o","u"]

vowelCount = 0

for character in word:
    if character in vowels:
        vowelCount += 1

print("There are " + str(vowelCount) + " vowels in the word " + word)

#range():
#takes inputs as: range(start, stop, step)
#if start not specified, default is 0
#if step not specified, default is 1

#print number between 0 and 3, both included
for i in range(4):
    print (i)

#print odd numbers between 1 and 7, both included
for i in range(1,8,2):
    print(i)

#loop the items in a list
vowels = ["a","e","i","o","u"]
for v in vowels:
    print(v)
'''

#len() returns the lenght 
vowels = ["a","e","i","o","u"]
i = 0
while i < len(vowels): #the iteration variable needs to be created, initialized and incremented.
    print(vowels[i])
    i += 1