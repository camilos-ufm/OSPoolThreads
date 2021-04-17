# imports
import sys, time
from threading import Thread
import numpy as np
import pandas as pd
 
class mat_mult:
    def __init__(self, matrix_a, matrix_b, pool_size):
        """ Create a new point at the origin """
        try:
            self.pool_size = int(pool_size)
        except ValueError:
            print(ValueError)
            print(f"Wrong pool_size, using default: 10")
            self.pool_size = 10;
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.matrix_c = []

    def validate_dimentions(self):
        m = self.matrix_a.shape[0]
        k1 = self.matrix_a.shape[1]
        k2 = self.matrix_b.shape[0]
        n = self.matrix_b.shape[1]
        self.matrix_c = np.zeros((m,n))
        return k1==k2

    def matmult(self, param1, param2):
        n = self.matrix_a.shape[1]
        for i in range(int(param1), int(param2)):
            for j in range(n):
                for k in range(n):
                    try:
                        self.matrix_c[i][j] += int(self.matrix_a[i][k] * self.matrix_b[k][j])
                    except:
                        pass

    def run(self):
        thread_pool_list = list()
        n = self.matrix_a.shape[1]

        for i in range(0, self.pool_size):
            init = (n/self.pool_size)
            end = (n/self.pool_size) 
            single_thread = Thread(target = self.matmult, args=(init * i, end * (i+1)))
            thread_pool_list.append(single_thread)
            single_thread.start()   

        for index, thread in enumerate(thread_pool_list):
            thread.join()
    
    def get_final_response(self):
        return self.matrix_c
