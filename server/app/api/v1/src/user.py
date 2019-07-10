from app import db
from app.models import User

class User_Obj(object):

    def __init__(self, username, email):
        self.user = User(username=username, email=email)

    def store(self):
        db.session.add(self.user)
        db.session.commit()
