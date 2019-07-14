from app import db
from app.models import User

class User_Object(object):

    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def store(self):
        user = User(full_name=self.full_name,
        email = self.email,
        password = self.password)
        db.session.add(user)
        db.session.commit()

    def check(self):
        user = User(
        email=self.email,
        password=self.password)
        pass

    def update(self):
        pass

    def delete(self):
        pass
