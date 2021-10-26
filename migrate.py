#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

#from domain import Base

from domain.user import User
#from domain.book import Book

#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#engine = create_engine("sqlite:///test.db", echo=True)
#conn = engine.connect()

#DBSession = sessionmaker(bind=engine)
#session = DBSession()

#Base.metadata.create_all(engine)

#app = Flask('main')

#db_name = 'test.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_ECHO'] = True

#db = SQLAlchemy(app)

#with app.app_context():
#    db.create_all()

from domain import db

db.create_all()
