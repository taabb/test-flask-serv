from flask import Flask

app = Flask(__name__)

@app.route("/get")
def text():
    return "text"


if __name__ == '__main__':
    app.run()