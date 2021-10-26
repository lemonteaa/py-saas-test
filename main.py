"""
    test a SQLite database connection locally
    assumes database file is in same location
    as this .py file
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from domain.user import User, Role

from flask_security import Security, login_required, \
     SQLAlchemySessionUserDatastore

app = Flask('main')

# DB config
db_name = 'test_security.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db.session,
                                                User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    user_datastore.create_user(email='foo@bar.com', password='hello-world123')
    db.session.commit()

# App routes
@app.route('/login', methods = ['POST'])
def login():
    json_data = request.get_json(force=True)
    j_username = json_data['username']
    j_password = json_data['password']
    try:
        user = User.query.filter_by(username= j_username).first()
        return jsonify(id = user.id)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)

