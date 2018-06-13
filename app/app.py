from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models import db
import resources
import config


app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db.init_app(app)
# ModelManager(db)

api = Api(app)
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
