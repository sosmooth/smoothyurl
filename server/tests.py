import unittest
from app import app
import requests
import flask

import pdb

class ApiTest(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config_test')
        self.api_url = app.config['API_URL']
        self.test_app = app.test_client()
                
    def tearDown(self):
        pass

    def testApi(self, url):
    
        response = requests.get(self.api_url, params= {'url': url})
        response = response.json()
        pdb.set_trace()
        self.assertEquals(response['state'], 'ok')
        #self.assertEquals(response.['shorturl']

        return flask.jsonifiy(response)

class testApiTest(ApiTest):

    def requestApi(self,):
        self.testApi('http://josuebrunel.org')


if __name__ == '__main__':
    unittest.main()
    