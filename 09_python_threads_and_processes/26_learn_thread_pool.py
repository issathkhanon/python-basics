"""Several orders, with only three workers at a time.

Run this file from the terminal:

    python 26_learn_thread_pool.py

map calls prepare_order once for each name. The names can be a list
or any sequence. max_workers=3 means only three calls run at once, so
six one-second orders finish in about two seconds.

The with block closes the pool when the block ends. That waits for the
workers and then stops them. There is no separate close() call.

submit runs one call and returns a future. result() waits for that
call. Use submit for a single order, or when each call needs different
arguments. map is the shorter form when every call uses the same
function and the next value from a sequence.

    tea, coffee, juice, cake, biscuit, fruit
                    |
                3 workers
                    |
         map returns each order in the same order
         submit runs the one water order
"""

import time
from concurrent.futures import ThreadPoolExecutor


def prepare_order(name):
    time.sleep(1)
    return f"{name} is ready"


orders = ["tea", "coffee", "juice", "cake", "biscuit", "fruit"]

# with closes the pool at the end of this block
with ThreadPoolExecutor(max_workers=3) as executor:
    # map calls prepare_order once for each name, in this order
    for ready in executor.map(prepare_order, orders):
        print(ready)

    # submit is one call. result() waits for the returned text
    one_order = executor.submit(prepare_order, "water")
    print(one_order.result())
