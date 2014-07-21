import os
from uuid import uuid4

basedir = os.path.abspath(os.path.dirname(__file__))

CSFR_ENABLED = True
SECRET_KEY = uuid4()

#TINY URL
TINY_URL = 'http://tinyurl.com/api-create.php'