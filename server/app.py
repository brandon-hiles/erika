from flask import Flask, request, jsonify, abort

from src.api.mongo import Mongo # Local DB
#from src.api.aws import *

app = Flask(__name__) # Setup flask server

# Setup mongo init variables
host = 'localhost'
port = 27017

mongo = Mongo(host=host, port=port)

@app.route('/api/v1.0/db/')
def db():
	# Database Page used for searching for data
    example_query = {"title" : " Merkel protege suggests reducing gas flow through Nord Stream 2 pipeline "}
    data = mongo.json_data(db='news', collection='reuters', query=example_query)
    return data

if __name__ == '__main__':
    app.run(debug=True)
