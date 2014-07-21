from flask import Flask

#Defining App
app = Flask(__name__)
app.config.from_object('config')

#
#__all__ = ['views.py']
from . import views
from . import api