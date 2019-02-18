from flask import Flask, request, render_template, jsonify, abort
from bson.objectid import ObjectId


from src.api.mongo import Mongo # Local DB
#from src.api.aws import *

app = Flask(__name__) # Setup flask server

# Setup mongo init variables
host = 'localhost'
port = 27017

mongo = Mongo(host=host, port=port)

@app.route('/')
def open():
    return '<h1> Erika Backend </h1>'

@app.route('/api/db/id/', methods=['GET', 'POST'])
def db():
	# Database Page used for searching for data
    _id = request.args.get('id')
    example_query = {"_id": ObjectId(_id)}
    data = mongo.json_data(db='news', collection='reuters', query=example_query)
    return data

if __name__ == '__main__':
    app.run(debug=True)
