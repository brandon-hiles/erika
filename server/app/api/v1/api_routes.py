import sys
import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import jsonify,json
from flask import request
from sqlalchemy import exc


from app.api.v1 import api
from app.api.v1.src.mongo import Mongo
from app.api.v1.src.user import User_Object

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
def store():
    # Store Users Endpoint

    # Initalize our user requested parameters
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')

    # Initialize our User Object
    user = User_Object(
     full_name=name,
     email=email,
     password=password)

    try:
        user.store()
        return jsonify({
        'Status' : 200,
        'Message' : 'User has been successfully added'
        })
    except exc.SQLAlchemyError:
        return jsonify({
        'Status' : 404,
        'Message' : 'User has already been added'
        })

@api.route('/db/user/check', methods=['GET'])
def check_user():
    # Check user endpoint

    # Initiate our user requested parameters
    email = request.args.get("email")
    password = request.args.get("password")

    # Initiate our User Object
    user = User_Object(full_name="",
    email=email,
    password=password)

   try:
        user.check()
        return jsonify({
        'Status' : 200,
        'Message' : 'User does exist in the database'
        })
    except exc.SQLAlchemyError:
        return jsonify({
        'Status' : 404,
        'Message' : 'User does NOT exist in the database'
        })

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

@api.route('/documentation', methods=['GET'])
def documentation():
    return 'documentation endpoint'
