import json
import os
import urllib
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
from flask import Flask, request, render_template, redirect, send_from_directory, url_for, jsonify
from bson import json_util

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC'
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)
load_dotenv()

username = urllib.parse.quote_plus(os.getenv('USERNAME'))
password = urllib.parse.quote_plus(os.getenv('PASSWORD'))
server = "mongo"  # "127.0.0.1"  # mongo
client = MongoClient('mongodb://%s:%s@%s:27017' % (username, password, server))
db = client["app"]
collection = db["data"]


@app.route('/submit', methods=['POST', 'GET'])
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def submit():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        file = open("data/data.json", "w", encoding='utf-8')
        json.dump(data, file, indent=4, ensure_ascii=True)
        file.close()
        collection.insert_one(data)
        print("post successfully!")
        response = jsonify({"ok": True})
        return response


@app.route('/data/<path:filename>', methods=['GET'])
def download(filename):
    print(os.path.join(os.getcwd(), "data/"))
    print(filename)
    return send_from_directory("data", filename, as_attachment=True)


@app.route('/data')
def query():
    return json.loads(json_util.dumps(list(collection.find())[-1]))


if __name__ == '__main__':
    app.run()
