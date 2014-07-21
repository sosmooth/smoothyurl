from app import app
import flask
import requests

import pdb

TINY_API_URL = app.config['TINY_API_URL']
TINY_API_KEY = app.config['TINY_API_KEY']
TINY_API_PROVIDER = app.config['TINY_API_PROVIDER']
TINY_API_FORMAT = app.config['TINY_API_FORMAT']

@app.route('/api/v1.0/')
def smoothy():
    
    url = flask.request.args.get('url')
    if not url:
        return "Smoothy API v1.0"
    
    payload = {
        'apikey': TINY_API_KEY,
        'provider': TINY_API_PROVIDER,
        'format': TINY_API_FORMAT,
        'url': url,
    }
    response = requests.get(TINY_API_URL, params= payload)

    try:
        json = response.json()
        if 'shorturl' not in json:
            return flask.app.abort(404)
    except Exception, e:
        print e, response.text
    return flask.jsonify(response.json())
    