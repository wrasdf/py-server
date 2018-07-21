from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models import db
import resources
import config
# import routes

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db.init_app(app)

# for blueprint in vars(routes).values():
#     if isinstance(blueprint, Blueprint):
#         server.register_blueprint(
#             blueprint,
#             url_prefix=config.APPLICATION_ROOT
#         )
#

api = Api(app)
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
