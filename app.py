import json
import os
from flask import Flask, request, render_template, redirect, send_from_directory, url_for, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC'
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)


@app.route('/submit', methods=['POST', 'GET'])
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def submit():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        file = open("data/data.json", "w", encoding='utf-8')
        json.dump(data, file, indent=4, ensure_ascii=True)
        file.close()
        print("post : data => ", data)
        response = jsonify({"ok": True})

        return response


@app.route('/data/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    print(os.path.join(os.getcwd(), "data/"))
    print(filename)
    return send_from_directory("data", filename, as_attachment=True)


if __name__ == '__main__':
    app.run()
