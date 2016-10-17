#!/usr/local/bin/python
import argparse
import os
import sys
sys.path.append(".")
from quotes.spiders import runner


parser = argparse.ArgumentParser(prog='scripts/run.py', usage='%(prog)s [url]')
parser.add_argument('url', nargs='+', help='brainy quote url')
args = parser.parse_args()

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/usr/src/app/quotes/assets/out.csv")
runner(args.url[0], path)
# print(args.url)
print("Exported: " + path)
