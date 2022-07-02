
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC'
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)


@app.route('/submit', methods=['POST', 'GET'])
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def submit():
    if request.method == 'POST':
        data = request.data
        print("post : data => ", data)
        response = jsonify({})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/', methods=['POST', 'GET'])
def root():
    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()
