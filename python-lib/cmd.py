#!/usr/bin/python
import sys
sys.path.append('pyquotes')
from pyquotes.read import read_file, random_quote


if __name__ == "__main__":
    print("Read quotes")
    print(random_quote("../quotes/albert_einstein.csv"))
