from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Auth(Resource):
    def get(self, subpath):
        return 'Subpath %s' % subpath

api.add_resource(HelloWorld, '/')
api.add_resource(Auth, '/auth/<path:subpath>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
