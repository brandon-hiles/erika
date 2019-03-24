from flask import Flask, request, render_template, jsonify, abort
from bson.objectid import ObjectId
from bson.errors import InvalidId

from src.api.mongo import Mongo
from src.api.dashboard.main import loading_page

app = Flask(__name__) # Setup flask server

# Setup mongo init variables
host = 'localhost'
port = 27017

mongo = Mongo(host=host, port=port, db="news")

@app.route('/')
def open():
    return render_template('base.html')

@app.route('/api/db/<string:collection>/articles', methods=['GET'])
def articles(collection):
    # Article Endpoint

    parm = request.args.get('topic')
    example_query = { '$text' : {'$search' : parm} }
    return mongo.article(collection=collection, query=example_query)

@app.route('/documentation/', methods=['GET'])
def documentation():
    return render_template('documentation.html')

if __name__ == '__main__':
    app.run(debug=True)
