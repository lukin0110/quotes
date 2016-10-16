import random as randy
import os
from .read import read_file

# Relative path to this __init__ file
SETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/sets.csv")
_quotes = None


def random(sets_file=SETS):
    global _quotes
    if _quotes is None:
        _quotes = load_sets(sets_file)

    key = randy.choice(list(_quotes.keys()))
    return key, randy.choice(_quotes[key])[0]


def load_sets(sets_file=SETS):
    sets = read_file(sets_file)
    results = {}

    for item in sets:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sets_file)), item[1])
        results[item[0]] = read_file(file_path)

    return results
