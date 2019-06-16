__version__ = 0.2
__author__ = "Brandon Hiles"

import nltk

from src.amanda.db.mongo import Mongo

class ReutersPreProcessing(object):

    """ 
    ReutersPreProcessing is a preprocessing class that extracts
    the important information from the article and stores the new values
    into a new database called <Insert DB Name>

    Parameters:
    1. query: Specify information you want to extract from
    previous database
    2. host: Specify host of the database
    3. port: Specify on which port you want to run your
    database on
    """

    def __init__(self, host, port, query):
        self.query = query
        self.host = host
        self.port = port
        self.mongo = Mongo(host=self.host, port=self.port)
        self.client = self.mongo.client()

    def data_retrival(self, db, collection):

        db = self.client[db]
        collection = db[collection]
        result = collection.find_one(self.query) # Works with find_one, test find() method
        return result

    def preprocess(self,data):

        data = nltk.word_tokenize(data)
        data = nltk.pos_tag(data)
        return data