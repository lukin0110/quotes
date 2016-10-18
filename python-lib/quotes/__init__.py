import random as randy
import os
from .read import read_file

# Relative path to this __init__ file
SETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/index.csv")
_quotes = None


def _get_quotes(sets_file=SETS):
    global _quotes
    if _quotes is None:
        _quotes = load_sets(sets_file)
    return _quotes


def random(sets_file=SETS):
    quotes = _get_quotes(sets_file)
    key = randy.choice(list(quotes.keys()))
    return key, randy.choice(_quotes[key]['lines'])[0]


def persons(sets_file=SETS):
    quotes = _get_quotes(sets_file)
    return list(quotes.keys())


def sets(sets_file=SETS):
    quotes = _get_quotes(sets_file)
    return {k: v['set'] for k, v in quotes.items()}


def load_sets(sets_file=SETS):
    sets = read_file(sets_file)
    results = {}

    # Skip the first line of each file, it's the header
    for item in sets[1:]:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sets_file)), item[1])
        results[item[0]] = {
            'lines': read_file(file_path)[1:],
            'set': item[1]
        }

    return results
