from flask import Flask, request, render_template, jsonify, abort
from bson.objectid import ObjectId
from bson.errors import InvalidId

from src.api.mongo import Mongo
from src.api.aws import AWS

app = Flask(__name__) # Setup flask server

# Setup mongo init variables
host = 'localhost'
port = 27017

# Initiate Server Classes
mongo = Mongo(host=host, port=port, db="news")
aws = AWS(credentials='test')

@app.route('/')
def open():
    # Landing Page
    return render_template('base.html')

@app.route('/api/documentation/', methods=['GET'])
def documentation():
    # Documentation Endpoing
    return render_template('documentation.html')

@app.route('/api/db', methods=['GET'])
def database():
    return render_template('database.html')

@app.route('/api/db/<string:collection>/articles', methods=['GET'])
def articles(collection):
    # Database/Article Endpoint

    parm = request.args.get('topic')
    example_query = { '$text' : {'$search' : parm} }
    return mongo.article(collection=collection, query=example_query)

@app.route('/api/ai', methods=['GET'])
def ai():
    return render_template('ai.html')

@app.route('/api/data-mining', methods=['GET'])
def data_mining():
    return render_template('data-mining.html')

@app.route('/api/data-mining/<string:instance>/deploy', methods=['GET', 'POST'])
def deploy(instance):
    # Data Mining Deployment Endpoint

    # Deploy Data Mining Crawler
    aws.DeployEC2Instance(instance=instance)

    return '<h1> Data Mining Deployment Page: ' + instance + ' has been deployed </h1>'


if __name__ == '__main__':
    app.run(debug=True)
