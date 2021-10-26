#from sqlalchemy import Column, String, Integer, Float, TIMESTAMP

from domain import db

#The Student class is equivalent to a table created in sql
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(256))

    def __repr__(self):
        return "<User(id='%s', username='%s')>" % (self.id, self.username)
