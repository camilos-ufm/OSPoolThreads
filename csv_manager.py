import csv
from os import read
import pandas as pd


class csv_manager:

    @staticmethod
    def read(file_name="matA.csv"):
        df = pd.read_csv(file_name, sep=',', header=None)
        return df


    @staticmethod
    def write(output_filename="out.csv", content="No content found."):
        text_file = open(output_filename, "w")
        text_file.write(content)
        text_file.close()
