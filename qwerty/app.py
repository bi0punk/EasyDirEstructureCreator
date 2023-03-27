from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
   return "<p>Hello World from FasT-FlasK!, generated 2023-03-26 23:34:29.471670</p>"