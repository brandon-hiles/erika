from flask import Flask, request

from src.api.mongo import Mongo # Local DB
#from src.api.aws import *

app = Flask(__name__) # Setup flask server

# Setup mongo init variables
host = 'localhost'
port = 27017

mongo = Mongo(host=host, port=port)

@app.route('/')
def main():
    # Standard Opening page
    return '<h1>Erika Backend</h1>'

@app.route('/db')
def db():
	# Database Page used for searching for data
    example_query = {"title" : " Merkel protege suggests reducing gas flow through Nord Stream 2 pipeline "}
    table = mongo.generate_table_html(query=example_query)
    return table

if __name__ == '__main__':
    app.run(debug=True)
