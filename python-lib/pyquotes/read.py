import csv
import random


def read_file(filename):
    result = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            result.append(row)
    return result


def random_quote(filename):
    return random.choice(read_file(filename))
