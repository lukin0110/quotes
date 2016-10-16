import os
import unittest

from pyquotes import random, load_sets


class TestStringMethods(unittest.TestCase):
    def test_rigorous(self):
        print(random())
        self.assertTrue(True)

    def test_load_sets(self):
        # setsfile = os.path.join(os.path.dirname(__file__), "assets/sets.csv")
        setsfile = "/usr/src/app/pyquotes/assets/sets.csv"
        random(sets_file=setsfile)
        self.assertTrue(True)

    def test_write(self):
        # print("Write quotes")
        # write("in.csv", "out.csv")
        pass

