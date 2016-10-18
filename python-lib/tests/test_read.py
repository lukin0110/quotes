import os
import unittest
import quotes


class TestRead(unittest.TestCase):
    def test_rigorous(self):
        print(quotes.random())
        self.assertTrue(True)

    def test_load_custom_sets(self):
        # setsfile = os.path.join(os.path.dirname(__file__), "assets/sets.csv")
        setsfile = "/usr/src/app/quotes/assets/index.csv"
        quotes.random(sets_file=setsfile)
        self.assertTrue(True)

    def test_persons(self):
        persons = quotes.persons()
        self.assertTrue(type(persons) == list)
        print(persons)

    def test_sets(self):
        sets = quotes.sets()
        self.assertTrue(type(sets) == dict)
        print(sets)

    def test_write(self):
        # print("Write quotes")
        # write("in.csv", "out.csv")
        pass

