from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from pp import cl_ascii


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('list', type=list,location='json')

@app.route('/', methods=['GET'])
def index_page():
    response = jsonify('Hello World!!!')
    response.status_code = 200

    return response

@app.route('/convertir',methods = ['POST', 'GET'])
def get():
    args = parser.parse_args()
    f=cl_ascii() 
    return jsonify(f.read_ascii(args['list']))

if __name__ == "__main__":
    app.run(debug=True)