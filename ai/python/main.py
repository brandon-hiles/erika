__version__ = 0.2
__author__ = "Brandon Hiles"

import requests

# Custom Modules
from src.amanda.data_mining.parser import SiteMapParser
from src.amanda.data_mining.reuters import Reuters
from src.amanda.data_mining.wsj import WallStreetJournal
from src.amanda.data_mining.nyt import NewYorkTimes

from src.amanda.db.mongo import Mongo

host = 'localhost'
port = 27017

reuters = Reuters(host=host, port=port)
wsj = WallStreetJournal(host=host, port=port)
mongo = Mongo(host=host, port=port)