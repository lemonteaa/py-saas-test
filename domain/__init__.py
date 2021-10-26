#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('main')

# DB config
db_name = 'test_security.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

