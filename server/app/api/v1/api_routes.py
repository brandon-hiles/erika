import sys
import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import jsonify,json
from flask import request
from sqlalchemy import exc


from app.api.v1 import api
from app.api.v1.src.mongo import Mongo
from app.api.v1.src.user import User_Obj

# Grab environment variables
dotenv_path = sys.path[0] + '/.env'
print(dotenv_path)

# Setup mongo init variables
mongo_host = os.environ.get("MONGO_SERVER")
mongo_port = int(os.environ.get("MONGO_PORT"))

# Initiate Server Classes (Uncomment when fixing mongo issue)
mongo = Mongo(host=mongo_host, port=mongo_port, db="news")

# Validations
data_souces = ['reuters', 'wsj', 'nyt']

@api.route('/db/user/store', methods=['POST'])
def store_user():
    username = request.args.get('username')
    email = request.args.get('email')

    user = User_Obj(username=username, email=email)
    try:
        user.store()
        return jsonify({'Status' : 200, 'Message' : 'User has been successfully added'})
    except exc.SQLAlchemyError:
        return jsonify({'Status' : 404, 'Message' : 'User has already been added'})

# CRUD Endpoints for database
@api.route('/db/store', methods=['POST'])
def create_database_table():
    # Create Endpoint (C)
    database = request.args.get('database')
    table = request.args.get('table')

    if db_type == 'SQL':
        return f"CREATE: You've slected {db_type} type"
    elif db_type == 'NOSQL':
        return f"CREATE: You've selected {db_type} type"
    else:
        return "Please enter a valid service"

@api.route('/db/<db_type>/<database>/<table>', methods=['GET'])
def read_database_response(db_type, database, table):
    # Read Endpoint (R)

    if db_type == 'SQL':
        return f"READ: You've selected {db_type} type"
    elif db_type == 'NOSQL':
        return f"READ: You've selected {db_type} type"
    else:
        return 'Please enter a valid service'

@api.route('/db/<db_type>/<database>/<table>/update', methods=['PUT'])
def update_database(db_type, database, table):
    # Update Endoint (U)

    if db_type == 'SQL':
        return f"UPDATE: You've selected {db_type} type"
    elif db_type == 'NOSQL':
        return f"UPDATE: You've selected {db_type} type"
    else:
        return "Please enter a valid service"

@api.route('/db/<db_type>/<database>/<table>/delete', methods=['DELETE'])
def delete_database(db_type, database, table):
    # Delete Endpoint (D)

    if db_type == 'SQL':
        return f"DELETE: You've selected {db_type} type"
    elif db_type == 'NOSQL':
        return f"DELETE: You've selected {db_type} type"
    else:
        return "Please enter a valid service"

# AI Endpoints
@api.route('/ai/train', methods=['GET'])
def train():
    data = request.args.get('data')
    return jsonify({'train' : True, 'location' : data})

# Data-Mining Endpoints
@api.route('/data-mining/get', methods=['GET'])
def get_data():
    source = request.args.get('source')
    results = int(request.args.get('results'))
    if source in data_souces:
        data = mongo.return_all(collection=source)
        filter_data = []
        for idx in range(0, results):
            filter_data.append(data[idx])
        return jsonify({'articles' : filter_data})
    else:
        return jsonify({'Status' : 404, 'Message' : 'Please enter a valid source'})

@api.route('/data-mining/<string:instance>/deploy', methods=['GET'])
def deploy(instance):
    # Data Mining Deployment Endpoint
    if instance == "reuters":
        instance_id = os.environ.get("AWS_REUTERS_ID")
    elif instance == "wsj":
        instance_id = os.environ.get("AWS_WSJ_ID")
    elif instance == "nyt":
        instance_id = os.environ.get("AWS_NYT_ID")
    else:
        instance_id = "Please enter valid variable"

    # Check that your source is valid
    status = False
    if instance_id != "Please enter valid variable":
        status = True
    ec2_list = []
    ec2_dict = { 'EC2_Machine' : instance_id, 'EC2_Status' : status}
    ec2_list.append(ec2_dict)
    json_string = json.dumps(ec2_list)
    return jsonify(AWS=json_string)
