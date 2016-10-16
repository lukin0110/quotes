import csv
import random


def read_file(filename):
    result = []
    # iterator should return strings, not bytes (did you open the file in text mode?)
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            result.append(row)
    return result
