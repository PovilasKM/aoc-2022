import time
start = time.time()
ii = []
for i in range(4000000):
    ii.append(i)
end = time.time()
print('It took ' + str(end-start) +' seconds to generate 1000000 numbers')
