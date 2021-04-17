<h1 align="center">
  <!-- a href="https://github.com/denysdovhan/spaceship-prompt" -->
    <img alt="cpu" src="https://github.com/camilos-ufm/OSPoolThreads/blob/main/image.png" width="200">
  <br>🚀 OSPoolThreads <br>
</h1>

<div align="center">
  <h4>
    <a href="#Solution">Solution</a> |
    <a href="#Requirements">Requirements</a> |
    <a href="#Installing and running the app">Installing</a> |
    <a href="#Contributing">Contributing</a> |
    <a href="#License">License</a>
  </h4>
</div>

<div align="center">
  <sub>Built with ❤︎ by
  <a href="#">Katherine Mazariegos</a>,
  <a href="#">Daniel Hernández</a> and <a href="#">Andres Bolaños</a>
</div>
<br>

matrix multiplication using a thread pool to multiprocess the arithmetic operations

<sub>Vist <a href="#">Troubleshooting</a> to find more.</sub>

## Solution

- Read the CSV files and convert them into matrix.
- A csv_manager was implemented (read and write files with static methods).
- We created a class to implement the solution, it is called mat_mult.py
- This class has several methods that help with the implementation: verify the dimention of the matrix, run the actual code and managing the atributes.
- We used a time package from the python library to keep track of the total amount used for the algorithm.
- The class mat mult has a main method: run() and it implements a list o threads (pool), in which we store each pool.
- We created different partitions of the matrix according to the pool size.
- A part of the matrix is assigned to each thread for it to operate.
- At the end, we iterate in the list of threads and join them all to the main thread.
- All operations are storaged in an atribute in the class instance, so we print it into a csv.

Final time result for a 500x500 operation: 362.452 seconds

**💡 Warning:** It can take some time and % of the CPU.

## Requirements

To work correctly, you will first need:

- [`Python`](https://www.python.org/downloads/release/python-394/) must be installed.

Then run this command in order to install all the aditional dependencies from pip

```
pip install -r requirements.txt

```

## Installing and running the app

Now that the requirements are satisfied, you can install and run the Mat Mult. First download or clone the repository and:

### [Production]

```
python main.py m1A.csv m1B.csv 4 output.csv

```

Done. This command should run the code.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

