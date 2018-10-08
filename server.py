from flask import Flask
from flask import jsonify
from flask_cors import CORS
from compute import get_scores
app = Flask(__name__)
CORS(app)
@app.route('/')
def get_data():
    return jsonify(get_scores())

if __name__ == "__main__":
    app.run(port=5000, debug=True)


