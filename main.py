"""
    test a SQLite database connection locally
    assumes database file is in same location
    as this .py file
"""

from flask import Flask, request, jsonify
from flask_security.decorators import auth_token_required, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from domain.user import User, Role

from flask_security import Security, login_required, \
     SQLAlchemySessionUserDatastore

from flask_security.utils import hash_password, verify_password

app = Flask('main')

# DB config
db_name = 'test_security.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = 'initialD$619'

db = SQLAlchemy(app)

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db.session,
                                                User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    #first_user = user_datastore.create_user(email='admin',
    #           password=hash_password('super#283'))
    #user_datastore.toggle_active(first_user)
    db.session.commit()

# App routes
@app.route('/mylogin', methods = ['POST'])
def login():
    json_data = request.get_json(force=True)
    j_email = json_data['email']
    j_password = json_data['password']
    try:
        #user = User.query.filter_by(username= j_username).first()
        user = user_datastore.get_user(j_email)
        result = verify_password(j_password, user.password)
        return jsonify(id = user.id, result = result, token = user.get_auth_token())
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route('/test-auth')
@auth_token_required
def test_auth():
    print(current_user.id)

if __name__ == '__main__':
    app.run(debug=True)

