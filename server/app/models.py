from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), index=True)
    last_name = db.Column(db.String(25), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.email)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(140))
    article_source = db.Column(db.String(160))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
