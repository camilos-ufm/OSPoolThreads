from mat_mult import mat_mult
from csv_manager import csv_manager
import sys, time

import sys
# python main file1 file2 pool_size fileoutput


def show_help():
    print("Help Menu\n\n"
          "fileA:\n  Archivo (matriz) de entrada 1 de 2.\n"
          "\nfileB:\n  Archivo (matriz) de entrada 2 de 2.\n"
          "\npool_size:\n  El tamaño del pool a utilizar.\n"
          "\noutput_filename:\n  Nombre del archivo de salida.\n")


if __name__ == "__main__":
    arguments = sys.argv
    if (len(arguments) == 5):
        file_a = arguments[1]
        file_b = arguments[2]
        pool_size = arguments[3]
        output_filename = arguments[4]

        file_a_df = csv_manager.read(file_a)
        file_b_df = csv_manager.read(file_b)
        mult = mat_mult(file_a_df, file_b_df, pool_size)
        if(mult.validate_dimentions()):
            start = time.perf_counter()
            mult.run()
            end = time.perf_counter()
        else:
            print("Not able to operate, mismatched dimentions")
            
        print(f"Time taken to complete mat_mult(): {round(end - start, 5)} seconds(s)")
        csv_manager.write_final_response(mult.get_final_response(), output_filename)

    else:
        show_help()
