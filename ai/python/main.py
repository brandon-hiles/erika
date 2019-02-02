__version__ = 0.2
__author__ = "Brandon Hiles"

import requests

# Custom Modules
from src.amanda.data_mining.parser import SiteMapParser
from src.amanda.data_mining.reuters import Reuters
from src.amanda.data_mining.wsj import WallStreetJournal
from src.amanda.data_mining.nyt import NewYorkTimes

from src.amanda.db.mongo import Mongo
# Consider adding Name entity recognition into AI section

# Basic Variables
host = 'localhost'
port = 27017
mongo = Mongo(host=host, port=port)
client = mongo.client()
db = client['news']
print(db)
# Parser Testing
# parser = SiteMapParser(host=host, port=port)

# Reuters Testing
reuters = Reuters(host=host, port=port)
reuters.store_websites(upper_bound=1000)

# Wall Street Journal Testing
# wsj = WallStreetJournal(host=host, port=port)

# New York Times Testing
#nyt = NewYorkTimes(host='localhost', port=27017)
#data = nyt.get_websites()

# Database Testing
#mongo = Mongo(host=host, port=port)

# Preprocessing Testing
#from src.amanda.preprocessing.reuters import ReutersPreProcessing

#example_query = {"title" : " Merkel protege suggests reducing gas flow through Nord Stream 2 pipeline "}
#r_preprocess = ReutersPreProcessing(host=host, port=port, query=example_query)
#data = r_preprocess.data_retrival(db='news', collection='reuters')
#data = data['article']
#preprocessed_data = r_preprocess.preprocess(data=data)