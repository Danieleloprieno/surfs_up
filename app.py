# import flask
from flask import Flask

# create instance
app = Flask(__name__)

# create route
@app.route('/')
def hello_world():
    return 'Hello world'