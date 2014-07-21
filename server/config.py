import os
from uuid import uuid4

basedir = os.path.abspath(os.path.dirname(__file__))

CSFR_ENABLED = True
SECRET_KEY = uuid4()

#SHORTENER SERVICE SETTINGS
TINY_API_URL = 'http://tiny-url.info/api/v1/create'
TINY_API_KEY = '8A6CIC8081B6BC5G5A07'
TINY_API_PROVIDER = 'go_ly'
TINY_API_FORMAT = 'json'

#LOGS SETTINGS
LOG_FOLDER = 'logs'
LOG_FILENAME = 'smoothyurl.log'
LOG_INFO = 'Smoothy url startup'