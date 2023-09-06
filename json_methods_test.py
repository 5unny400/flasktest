import json

from flask import jsonify

from app import app


# app = Flask(__name__)


# @app.route('/')
# def index():
#     return "index"


@app.route('/demo1')
def demo1():
    dict1 = {"name": "monkey", "age": 23}
    json_str = json.dumps(dict1)
    print(type(json_str))
    return json_str


@app.route('/demo2')
def demo2():
    dict1 = {"name": "monkey", "age": 23}
    return jsonify(dict1)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

