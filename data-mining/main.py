__version__ = 0.3
__author__ = "Brandon Hiles"

# Default Modules
import argparse
import requests
import unittest

# Custom Dev Modules
from src.api.data_mining.parser import SiteMapParser
from src.api.data_mining.reuters import Reuters
from src.api.data_mining.wsj import WallStreetJournal
from src.api.data_mining.nyt import NewYorkTimes

from src.api.db.mongo import Mongo

# Test Modules
from test import *


# Database Variables
host = 'localhost'
port = 27017

# Parser Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--coverage") # Unit Test Coverage
parser.add_argument("--reuters") # Reuters Data
parser.add_argument("--wsj") # Wall Street Journal Data
parser.add_argument("--nyt") # New York Times Data
parser.add_argument("--thread") # Threading module

if __name__ == '__main__':

    # Analyze arguments passed to python script
    args = parser.parse_args()

    import time
    startTime = time.time()

    # If --coverage is passed, then run unit tests.
    # Syntax: python main.py --coverage=true
    if args.coverage:
        print("coverage turned on")
        print("Executing Unit Tests")
        runner = unittest.TextTestRunner()
        runner.run(site_availability_suite())
        runner.run(parser_suite())
        runner.run(reuter_suite())

    # If --reuters is passed, then run reuter scripts.
    # Syntax: python main.py --reuters=true
    if args.reuters:
        print("Gathering data from reuters")
        reuters = Reuters(host=host, port=port)
        reuters.store_websites(upper_bound=10000)

    # If --wsj is passed, then run wsj scripts.
    # Syntax: python main.py --wsj=true
    if args.wsj:
        print("Gathering data from WSJ")
        wsj = WallStreetJournal(host=host, port=port)
        wsj.store_websites(upper_bound=1000)

    # If --nyt is passed, then run nyt scripts.
    # Syntax: python main.py --nyt=true
    if args.nyt:
        print("Gathering data from New York Times")
        nyt = NewYorkTimes(host=host, port=port)
        nyt.store_websites(upper_bound=1000)

    if args.thread:
        parser = SiteMapParser(website='https://www.reuters.com', host=host, port=port, collection="reuters")
        parser.main()


    print(f"Time Execution: {time.time() - startTime} s")
