from flask import jsonify
from pymongo import MongoClient

class Mongo(object):

    def __init__(self, host, port):
	    self.host = host
	    self.port = port

    def client(self):
	    return MongoClient(self.host, self.port)

    def json_data(self, db, collection, query):
        # Return json file of data from mongoDB
        client = self.client()
        db = client[db]
        collection = db[collection]
        result = collection.find_one(query)

        data = [
            {
                'title' : result['title'],
                'article': result['article'],
                'authors': result['authors'],
                'url' : result['meta']['url'],
                'tags': result['meta']['tags']
            }
        ]

        return jsonify({'data' : data})