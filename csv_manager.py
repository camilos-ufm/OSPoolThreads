import csv
from os import read
import pandas as pd


class csv_manager:

    @staticmethod
    def read(file_name="matA.csv"):
        df = pd.read_csv(file_name, sep=',', header=None)
        return df.to_numpy()

    @staticmethod    
    def write(output_filename="out.csv", content="No content found."):
        text_file = open(output_filename, "a+")
        text_file.write(content)
        text_file.close()

    @staticmethod
    def write_final_response(matrix, output_filename="out.csv"):
        pd.DataFrame(matrix).to_csv(output_filename, header=None, index=None)