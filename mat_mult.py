import pandas as pd
from tabulate import tabulate


class mat_mult:

    @staticmethod
    def mult(file_a, file_b):
        print(tabulate(file_a, headers='keys', tablefmt='psql'))
        print(tabulate(file_b, headers='keys', tablefmt='psql'))

        print(f"FILE A {file_a}")
        print(f"FILE B {file_b}")
