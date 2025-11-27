from flask import Flask
import os

app = Flask(__name__)

@app.route("/get")
def text():
    return "text"


port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)