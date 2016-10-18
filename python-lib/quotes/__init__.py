import random as randy
import os
from .read import read_file


def load_sets(sets_file):
    set_list = read_file(sets_file)
    results = {}

    # Skip the first line of each file, it's the header
    for item in set_list[1:]:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sets_file)), item[1])
        results[item[0]] = {
            'lines': read_file(file_path)[1:],
            'set': item[1]
        }

    return results


class Quotes(object):
    # Relative path to this __init__ file
    SETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/index.csv")

    def __init__(self, sets_file=SETS):
        self.sets_file = sets_file
        self.quotes = load_sets(self.sets_file)

    def random(self):
        key = randy.choice(list(self.quotes.keys()))
        return key, randy.choice(self.quotes[key]['lines'])[0]

    def persons(self):
        return list(self.quotes.keys())

    def sets(self):
        return {k: v['set'] for k, v in self.quotes.items()}
