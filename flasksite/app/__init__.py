# hello_world.py
from flask import Flask

app = Flask(__name__)

from app import routes


#
# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'