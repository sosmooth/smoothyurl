from flask import Flask

#Defining App
app = Flask(__name__)
app.config.from_object('config')
print(app.config)


#
#__all__ = ['views.py']
from . import views