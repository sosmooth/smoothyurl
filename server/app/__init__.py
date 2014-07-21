from flask import Flask

#Defining App
app = Flask(__name__)
app.config.from_object('config')

#App Logs
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(app.config['LOG_FOLDER']+'/'+app.config['LOG_FILENAME'], 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info(app.config['LOG_INFO'])


from . import views
from . import api
