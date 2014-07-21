import os
from uuid import uuid4

basedir = os.path.abspath(os.path.dirname(__file__))

CSFR_ENABLED = True
SECRET_KEY = uuid4().hex
API_URL = 'http://0.0.0.0:5000/api/v1.0/'
