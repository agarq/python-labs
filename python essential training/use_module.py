# module is literally just a Python file.

#one way is to import the whole module
#import primes
#print(primes.isPrime(5))

#another way is to import an individual function instead of the whole primes module
from primes import listPrimes

print(listPrimes(100))