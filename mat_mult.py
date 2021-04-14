import pandas as pd
from tabulate import tabulate
import threading
import time


class mat_mult:
    def __init__(self, matrix_a, matrix_b):
        """ Create a new point at the origin """
        self.X = matrix_a
        self.Y = matrix_b


    def mult(self, file_a, file_b):
        result = [[0]*self.m]
        for z in range(len(self.Y[0])):
            for k in range(len(self.Y)):
                result[0][z] += self.X[0] * self.Y[k][z]

        threads = list()


        start = time.perf_counter()
        for i in range(len(self.X[0])):
            self.X = threading.Thread(target=self.mult, args=(self.X[i], self.Y))
            threads.append(self.X)
            self.X.start()

        for index, thread in enumerate(threads):
            thread.join()
        end = time.perf_counter()

        print(
            f"Time taken to complete mult() {self.m}x{self.m}: {round(end - start, 5)} seconds(s)")
   
   
   # print(f" {result}")
        # print(tabulate(file_a, headers='keys', tablefmt='pretty'))
        # print(tabulate(file_b, headers='keys', tablefmt='pretty'))

        # print(f"FILE A {file_a}")
        # print(f"FILE B {file_b}")
