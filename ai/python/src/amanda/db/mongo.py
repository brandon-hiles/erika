__version__ = 0.2
__author__ = "Brandon Hiles"

from pymongo import MongoClient

class Mongo(object):

    def __init__(self, host, port):
	    self.host = host
	    self.port = port

    def client(self):
	    return MongoClient(self.host, self.port)

    def check_collection(self, db, collection,query):
        # Check if collection exists in db

        database = self.client()[db]
        collections = database[collection]
        result = collections.find(query)
        if collections.find(query).count() > 0:
            return True
        else:
            return False	