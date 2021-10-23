from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain import Base

from domain.student import Student

engine = create_engine("sqlite:///test_migrate.db", echo=True)
#conn = engine.connect()

#DBSession = sessionmaker(bind=engine)
#session = DBSession()

Base.metadata.create_all(engine)
