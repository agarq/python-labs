import threading
import time


def longSquare(num, results):
    time.sleep(1) # sleeps for 1 second
    results[num] = num**2

results = {}
#this is one way
#t1 = threading.Thread(target = longSquare, args=(1,results))
#t2 = threading.Thread(target = longSquare, args=(2,results))
#t1.start()
#t2.start()
#t1.join()
#t2.join()

#this is another way
threads = [threading.Thread(target = longSquare, args=(n,results)) for n in range (0,100)]
[t.start() for t in threads]
[t.join() for t in threads]

print(results)