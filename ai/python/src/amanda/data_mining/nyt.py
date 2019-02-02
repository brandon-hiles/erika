__version__ = 0.2
__author__ = "Brandon Hiles"

from pymongo import MongoClient

from src.amanda.db.mongo import Mongo
from src.amanda.data_mining.parser import SiteMapParser

class NewYorkTimes(SiteMapParser):

    """
    NewYorkTimes is an interface for parsing data from reuters.com

    Initialization Parameters:
    1. Host: Default parm: localhost
    2. Port: Used to specify the port instance of the db
       Default Parm: 27017
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.db = "news" 
        self.mongo = Mongo(host=host, port=port)
        self.client = self.mongo.client()
        super().__init__(website='https://www.nytimes.com/')


    def _extract_text(self, website):

        element = super().grab_elements(website)
        text = element[0].find_all("p")
        text = [''.join(text[num].text) for num, val in enumerate(text)]
        text = "".join(text)
        return text

    def store_websites(self, upper_bound):

        db = self.client[self.db]
        nyt = db['nyt']

        urls = super().get_websites()

        for index in range(0, upper_bound+1):
            website = requests.get(urls[index]).content.decode('utf-8')
            query = { 
                "article" : self._extract_text(website),
                "url" : urls[index]
                }
            check_query = {"url" : urls[index]}
            check = self.mongo.check_collection(db=self.db, collection='nyt',query=check_query)
            if check == False: # Checks that doesn't already exist in db
                nyt.insert_one(query).inserted_id