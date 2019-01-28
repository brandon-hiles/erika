__version__ = 0.2
__author__ = "Brandon Hiles"

# Custom Modules
from src.api.data_mining.parser import SiteMapParser
from src.api.data_mining.reuters import Reuters
from src.api.data_mining.wsj import WallStreetJournal
from src.api.data_mining.nyt import NewYorkTimes

# Basic Variables
host = 'localhost'
port = 27017

# Parser Testing
# parser = SiteMapParser(host=host, port=port)

# Reuters Testing
# reuters = Reuters(host=host, port=port)

# Wall Street Journal Testing
# wsj = WallStreetJournal(host=host, port=port)

# New York Times Testing
#nyt = NewYorkTimes(host='localhost', port=27017)
#data = nyt.get_websites()

