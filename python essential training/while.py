from datetime import datetime

#yyyy-mm-dd hh:mm:ss.milsec
#print(datetime.now()) #2022-09-20 10:29:42.130552
#print(datetime.now().second) #print the current second

wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    print('Still waiting !')

print(f'We are at {wait_until} seconds !')

#pass: help to keep the while indentation without having to use the print('Still waiting !') for example
wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    pass

print(f'We are at {wait_until} seconds !')

#break
wait_until = datetime.now().second + 2
while True:
    if datetime.now().second == wait_until:
        print(f'We are at {wait_until} seconds !')
        break

#Continue skips any lines that follow it inside of the while loop
wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    continue
    print('Still waiting !') #this will never print because of the Continue

print(f'We are at {wait_until} seconds !')

#Continue is usually used with if statements
wait_until = datetime.now().second + 2
while True:
    if datetime.now().second < wait_until:
        continue
    break
print(f'We are at {wait_until} seconds !')