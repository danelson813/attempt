# Attempt/main.py

from helpers.utils import log, timing


@timing
@log
def do_it():
    results = []
    for _ in range(100000):
        results.append("a")
    print(len(results))


do_it()
