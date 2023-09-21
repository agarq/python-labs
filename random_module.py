import random

#return a random integer between 1 and 100
x = random.randint(1,100) 
print('The random number is ' + str(x))

#return a random string from a list
movies = ["Aladdin", "Lion King", "Terminator", "X Project", "Troy", "Fast and Furiuos", "The Nun"]

watch = random.choice(movies)

print(watch)

#print items in a random order
deck = ["Ace", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
print(deck)
random.shuffle(deck)
print(deck)

