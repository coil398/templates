import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def pepper():
    data = json.loads(request.data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=8000)
