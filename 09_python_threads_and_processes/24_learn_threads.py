"""Two workers in one program.

Run this file from the terminal:

    python 24_learn_threads.py

A thread runs a function while the rest of the program continues.
start() begins that work. join() waits until it finishes.
Both functions share this one process, so this file does not need
if __name__ == "__main__".

Each worker pauses for one second, three times. Together they finish
in about three seconds. One after the other would take about six.

    serve_tea   -- start --+
                           +-- both run, then join
    serve_snack -- start --+
"""

import threading
import time


def serve_tea():
    for cup in (1, 2, 3):
        time.sleep(1)
        print(f"tea {cup}")


def serve_snack():
    for snack in ("biscuit", "cake", "fruit"):
        time.sleep(1)
        print(f"snack {snack}")


started = time.time()
# target is the function this thread will run
tea_worker = threading.Thread(target=serve_tea)
snack_worker = threading.Thread(target=serve_snack)
# start lets both workers run together
tea_worker.start()
snack_worker.start()
# join waits here until that worker has finished
tea_worker.join()
snack_worker.join()
seconds = round(time.time() - started)
print(f"time taken: {seconds} seconds")
