# 2016 December 25 by Simon Anatole Orlovsky

import random

def factorial(n):
    """The input n is a nonnegative integer. Returns the factorial n!."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    for i in range(5):
    	# Generate a somewhat random integer between 0 and 20 (more like 0 and 19).
        n = int(20.0 * random.random())
        print factorial(n), "=", n, "!"
    # Launch the help viewer for factorial (press Q to exit).
    help(factorial)
