from flask import Flask
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/get")
def text():
    return "text"


port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)