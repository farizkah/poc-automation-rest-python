from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}

    def put(self):
        return {'iam': 'back'}

if __name__ == '__main__':
    app.run(debug=True)
