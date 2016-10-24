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
        self.assertTrue(type(sets) == list)
        print(sets)

    def test_write(self):
        # print("Write quotes")
        # write("in.csv", "out.csv")
        pass

    def test_get_set1(self):
        quotes = Quotes()
        sets = quotes.sets()

        for k in sets:
            arr = quotes.get_set(k)
            self.assertIsInstance(arr, list)

    def test_pick(self):
        quotes = Quotes()
        quote = quotes.pick('albert_einstein', 0)
        self.assertEqual(quote[0], 'Albert Einstein')
        self.assertEqual(quote[1], "You can't blame gravity for falling in love.")

        with self.assertRaises(KeyError):
            quotes.pick('harry_foobar')

        with self.assertRaises(IndexError):
            quotes.pick('albert_einstein', -1)

    def test_random_pick(self):
        quotes = Quotes()
        picked = [('albert_einstein', 0), ('henry_ford', 1)]
        quote = quotes.random(pick=picked)
        expected = ['Albert Einstein', 'Henry Ford']
        self.assertTrue(quote[0] in expected)

    def test_random(self):
        quotes = Quotes()
        keys = ['albert_einstein', 'henry_ford']
        q = quotes.random(keys=keys)
        self.assertTrue(q[0] in ['Albert Einstein', 'Henry Ford'])

        keys = ['emily_carr', 'does not exist']
        q = quotes.random(keys=keys)
        self.assertEqual(q[0], 'Emily Carr')

        q = quotes.random(keys=[])
        self.assertTrue(q is None)
