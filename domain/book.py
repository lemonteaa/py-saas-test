from sqlalchemy import Column, String, Integer, Float, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from sqlalchemy.sql.schema import ForeignKey

from domain import Base

from domain.student import Student

class Book(Base):
    __tablename__ = 'book'
    bid = Column(Integer, primary_key=True)
    bname = Column(String(20))
    price = Column(Float(32))
    #Create foreign key student? ID
    student_id = Column(Integer, ForeignKey(Student.id))
    #Tell ORM to associate book class with Student class
    student = relationship(Student)
    insert_time = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    def __repr__(self):
        return "<Book(bid='%s', bname='%s', price='%s',student_id='%s')>" % (
        self.bid, self.bname, self.price, self.student_id)
