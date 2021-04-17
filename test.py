import threading
import time
import pandas as pd
import numpy as np 

m = 3
X = pd.read_csv("mA.csv", sep=',', header=None).to_numpy()
Y = pd.read_csv("mB.csv", sep=',', header=None).to_numpy()
 
print(len(X[0]))
print(len(Y))

def mult(X, Y):
   result = [[0]*m]
   for z in range(len(Y[0])):
       for k in range(len(Y)):
           result[0][z] += X[0] * Y[k][z]
   print(f" {result}")
 
threads = list()
start = time.perf_counter()
for i in range(len(X[0])):
   x = threading.Thread(target = mult, args=(X[i], Y))
   threads.append(x)
   x.start()
 
for index, thread in enumerate(threads):
   thread.join()
end = time.perf_counter()
 
print(f"Time taken to complete mult() {m}x{m}: {round(end - start, 5)} seconds(s)")