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
            'key': item[1]
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
        return {k: v['key'] for k, v in self.quotes.items()}

    def get_set(self, key):
        """
        Get 1 specific set of quotes based on a key. The key of a set is the name of the csv file,
        with or without extension.

        :param key: a string with key of the set
        :return: a list of quotes
        """
        assert key
        _quotes = {v['key'].replace('.csv', ''): v['lines'] for k, v in self.quotes.items()}

        if key in _quotes:
            return _quotes[key]

        _key = key.replace('.csv', '')
        if _key in _quotes:
            return _quotes[_key]

        raise KeyError(key)
