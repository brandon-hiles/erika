# Pre-req: Run pip3 install virtualenv
# Before running this script, for optimal efficiency, make sure
# you are inside a virtualenv by running source env/bin/activate

echo "Download Backend Server Libraries"
pip3 install flask
pip3 install python-dotenv

echo "Download Database Libraries"
pip3 install SQLAlchemy
pip3 install flask-sqlalchemy
pip3 install flask-migrate

echo "Download AI Libraries"
pip3 install tensorflow
