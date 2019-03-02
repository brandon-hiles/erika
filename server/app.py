from flask import Flask, request, render_template, jsonify, abort
from bson.objectid import ObjectId
from bson.errors import InvalidId

from src.api.mongo import Mongo
from src.api.dashboard.main import loading_page

app = Flask(__name__) # Setup flask server

# Setup mongo init variables
host = 'localhost'
port = 27017

mongo = Mongo(host=host, port=port)

@app.route('/')
def open():
    return render_template('base.html')

@app.route('/api/db/id/', methods=['GET', 'POST'])
def db():
	# Database Page used for searching for data
    _id = request.args.get('id')
    try:
        example_query = {"_id": ObjectId(_id)}
        data = mongo.json_data(db='news', collection='reuters', query=example_query)
        return render_template('dashboard.html', data=data.json['data'][0])
    except InvalidId:
        return render_template('error.html')

@app.route('/documentation/', methods=['GET'])
def documentation():
    return render_template('documentation.html')

if __name__ == '__main__':
    app.run(debug=True)
