"""Square several numbers in a pool of processes.

Run this file from the terminal:

    python 27_learn_process_pool.py

ProcessPoolExecutor gives each number to a separate process.
map passes one number into square_number and returns the results in
the same order as the list. max_workers=3 keeps three processes busy.

The with block closes the pool. The process creation stays inside
if __name__ == "__main__", for the same reason as a single Process:
the child process imports this file and must not start another pool.

    if __name__ == "__main__"
        numbers 2, 3, 4, 5, 6, 7
                    |
               3 processes
                    |
        map prints each square in list order
"""

import time
from concurrent.futures import ProcessPoolExecutor


def square_number(number):
    time.sleep(1)
    return f"{number} squared is {number * number}"


if __name__ == "__main__":
    numbers = [2, 3, 4, 5, 6, 7]
    # with closes the pool. Keep this inside __main__.
    with ProcessPoolExecutor(max_workers=3) as executor:
        # one number goes into square_number, then the next
        for line in executor.map(square_number, numbers):
            print(line)
