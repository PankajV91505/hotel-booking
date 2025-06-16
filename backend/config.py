# File: config.py
import os
from flask import Flask

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///hotelbooking.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__, template_folder='templates', static_folder='static')
