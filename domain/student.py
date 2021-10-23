from sqlalchemy import Column, String, Integer, Float, TIMESTAMP

from domain import Base

#The Student class is equivalent to a table created in sql
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    sex = Column(String(2))
    clas = Column(String(20))
    grade = Column(Float(32))

    def __repr__(self):
        return "<Student(id='%s', name='%s', sex='%s',clas='%s',grade='%s')>" % (self.id, self.name, self.sex, self.clas, self.grade)
