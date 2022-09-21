import csv

with open('10_02_us.csv','r') as f:
    #this file contains tab-separated values, so we specify \t in the delimiter
    reader = csv.reader(f, delimiter='\t') #reader is an Iterable
    next(reader) #to skip the headers
    #for row in reader:
    #    print(row) #print each line comma-separated
    
with open('10_02_us.csv','r') as f:
    #convert the result into a list
    reader = list(csv.reader(f, delimiter='\t'))
    #for row in reader[1:]:
    #    print(row)

with open('10_02_us.csv','r') as f:
    #convert the result into a dictionary
    reader = csv.DictReader(f, delimiter='\t')
    #for row in reader:
    #    print(row)

#FILTERING DATA
with open('10_02_us.csv', 'r') as f:
    data = list(csv.DictReader(f, delimiter='\t'))

#filter postal codes from Massachusetts that are prime numbers
primes = []
for number in range(2, 99999):
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break
    else:
        primes.append(number)

data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']
print(len(data))

#write the filtered data
with open('10_02_ma_prime.csv', 'w') as f:
    writer = csv.writer(f) #if I don't specify the delimeter, comma is the default
    for row in data:
        writer.writerow([row['place name'], row['county']])