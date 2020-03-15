'''create the application object as an instance of class Flask imported from the flask package'''
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
