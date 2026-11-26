"""The same two jobs in separate processes.

Run this file from the terminal:

    python 25_learn_processes.py

A process runs the function in its own program. On this Mac, Python
starts that program by importing this file again. The child import
must not create more processes, so start() and join() stay inside
if __name__ == "__main__". The functions stay outside that block,
because the child process needs to import them.

Each job pauses for one second, three times. Together they finish in
about three seconds.

    this file
        |
        +-- if __name__ == "__main__"
                serve_tea   -- start --+
                                       +-- join
                serve_snack -- start --+
"""

import multiprocessing
import time


def serve_tea():
    for cup in (1, 2, 3):
        time.sleep(1)
        print(f"tea {cup}")


def serve_snack():
    for snack in ("biscuit", "cake", "fruit"):
        time.sleep(1)
        print(f"snack {snack}")


# This file is the main program only when you run it.
# A child process imports the file, so this name is not "__main__" there.
if __name__ == "__main__":
    started = time.time()
    tea_worker = multiprocessing.Process(target=serve_tea)
    snack_worker = multiprocessing.Process(target=serve_snack)
    tea_worker.start()
    snack_worker.start()
    tea_worker.join()
    snack_worker.join()
    seconds = round(time.time() - started)
    print(f"time taken: {seconds} seconds")
