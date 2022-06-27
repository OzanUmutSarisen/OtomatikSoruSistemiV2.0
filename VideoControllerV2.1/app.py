import flask
from flask import Flask
import MongoDB_Dowload

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return flask.render_template("Index.html")


if __name__ == '__main__':
    app.run()
