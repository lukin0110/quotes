import os
import unittest
from quotes import Quotes


class TestRead(unittest.TestCase):
    def test_rigorous(self):
        quotes = Quotes()
        print(quotes.random())
        self.assertTrue(True)

    def test_load_custom_sets(self):
        # setsfile = os.path.join(os.path.dirname(__file__), "assets/sets.csv")
        setsfile = "/usr/src/app/quotes/assets/index.csv"
        quotes = Quotes(setsfile)
        quotes.random()
        self.assertTrue(True)

    def test_persons(self):
        quotes = Quotes()
        persons = quotes.persons()
        self.assertTrue(type(persons) == list)
        print(persons)

    def test_sets(self):
        quotes = Quotes()
        sets = quotes.sets()
        self.assertTrue(type(sets) == dict)
        print(sets)

    def test_write(self):
        # print("Write quotes")
        # write("in.csv", "out.csv")
        pass

    def test_get_set1(self):
        quotes = Quotes()
        sets = quotes.sets()

        for k, v in sets.items():
            arr = quotes.get_set(v)
            self.assertIsInstance(arr, list)

            arr = quotes.get_set(v.replace('.csv', ''))
            self.assertIsInstance(arr, list)
