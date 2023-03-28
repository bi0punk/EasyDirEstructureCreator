from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
   return "<p>Hello World from FasT-FlasK!, Generated: 2023-03-27 23:56:22.730199 </p>"