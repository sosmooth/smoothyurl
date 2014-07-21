import os
from uuid import uuid4

basedir = os.path.abspath(os.path.dirname(__file__))

CSFR_ENABLED = True
SECRET_KEY = uuid4()

#TINY URL
TINY_API_URL = 'http://tiny-url.info/api/v1/create'
TINY_API_KEY = '8A6CIC8081B6BC5G5A07'