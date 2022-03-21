import time

start_time = time.time()

for x in range(1, 500000):
  print(x)

end_time = time.time()

print('Start Time: {}'.format(start_time))
print('End Time: {}'.format(end_time))
print("%s seconds" % (time.time() - start_time))
