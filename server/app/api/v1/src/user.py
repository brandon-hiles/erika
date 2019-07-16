from flask import jsonify,json
from sqlalchemy import text
from sqlalchemy import exc

from app import db
from app.models import User

class User_Object(object):

    """
    User_Object is our User Controller, which contains all our
    logic in relation to user functionality. This class returns
    status codes, which represent the status of the event triggered.

    Status Codes:
    1: This means all database calls were completed as expected.
    0: This means that there was an issue with a database call and
    hence something went wrong.
    """

    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def store(self):
        user = User(full_name=self.full_name,
        email = self.email,
        password = self.password)

        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({
            'Status' : 1,
            'Message' : 'User has been successfully added'
            })
        except exc.SQLAlchemyError:
            return jsonify({
            'Status' : 0,
            'Message' : 'User has already been added'
            })

    def check(self):
        user = User(
        email=self.email,
        password=self.password)

        check = f"SELECT * FROM user WHERE email='{self.email}' and password='{self.password}'"
        result = db.engine.execute(SQL_check) # Executes SQL statement
        data = result.fetchall()

        if len(data) == 1:
            return jsonify({
            'Status' : 1,
            'Message' : "User does exist in the database"
            })
        else:
            return jsonify({
            'Status' : 0,
            'Message' : 'User does NOT exist in the database'
            })

    def update(self):
        user = User(full_name=self.full_name,
        email = self.email,
        password = self.password)

        update = f"<Insert Update SQL Statement"

        return jsonify({
        'Status' : 1,
        'Message' : 'User was updated successfully'
        })

    def delete(self):
        user = User(full_name=self.full_name,
        email=self.email,
        password=self.password)

        delete = f"<Insert Delete SQL Statement>"

        return jsonify({
        'Status' : 1,
        'Message' : 'User was deleted successfully'
        })
