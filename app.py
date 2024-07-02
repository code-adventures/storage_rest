from flask import Flask
from flask import jsonify
import storage

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(storage.get_shopping_lists())

if __name__ == '__main__':
    app.run()

