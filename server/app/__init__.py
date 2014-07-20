from flask import Flask

#Defining App
app = Flask(__name__)



#
#__all__ = ['views.py']
from . import views