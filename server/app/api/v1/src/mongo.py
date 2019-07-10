from flask import jsonify
from pymongo import MongoClient

class Mongo(object):

    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[db]

    def return_all(self, collection):
        lst = []
        data = self.db[collection].find()
        for data_point in data:
            lst.append(data_point['article'])
        return lst

    def get_query(self, collection, query):
        # Helper function: Gets result from db based on collection and query
        return self.db[collection].find(query)

    def article(self, collection, query):
        # Article Endpoint

        result = self.get_query(collection=collection, query=query)
        if result.count() <= 0:
            return jsonify(
            {
            "Status Code" : "404",
            "Article" : "Article not found on servers"
            })

        data = []
        for index in range(0, result.count()):
            data.append(
                {
                    'Status Code' : '200',
                    'Article' : result[index]['article'],
                    'URL' : result[index]['url']
                }
            )
        return jsonify({'articles' : data})
