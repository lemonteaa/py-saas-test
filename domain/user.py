from sqlalchemy import Column, String, Integer, Float, TIMESTAMP

from domain import Base

#The Student class is equivalent to a table created in sql
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(256))

    def __repr__(self):
        return "<User(id='%s', username='%s')>" % (self.id, self.username)
