def isPrime(n, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes
    
print(f'primes.py module name is {__name__}') #print __main__ if I run this file. If run from another file, prints the name of that file.

if __name__ == '__main__':
    print('This is a Module. Please import using:\nimport primes')