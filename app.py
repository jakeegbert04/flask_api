from flask import Flask, jsonify

import json

app = Flask(__name__)

f = open("MOCK_DATA.json")

data = json.load(f)

@app.route("/data")
def get_all_data():
    return jsonify(data) , 200

@app.route("/data/<id>")
def get_data_by_id(id):
    for user in data:
        if user["id"] == int(id):
            return jsonify(user), 200
    return jsonify("User Doesn't exist"), 404

if __name__=="__main__":
    app.run(port="8080", host="0.0.0.0")