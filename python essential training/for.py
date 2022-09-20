mylist = [1,2,3,4,5]

for item in mylist:
    print(item)

animal_lookup = {
    'a': ['aardvark', 'ant'],
    'b': ['bear'],
    'c': ['cat'],
    'd': ['dog']
}

#pass
for letter, animals in animal_lookup.items():
    pass #do anything

#continue
for letter, animals in animal_lookup.items():
    if len(animals) > 1:
        continue
    print(f'Only one animal: {animals[0]}')

#break
for letter, animals in animal_lookup.items():
    if len(animals) > 1:
        print(f'Found {len(animals)}: {animals}')
        break

for number in range(2,100):
    for factor in range(2, int(number**0.5)):
        if number % factor == 0:
            break
    else:
        print(f'{number} is prime')