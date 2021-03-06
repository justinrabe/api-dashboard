import requests
import json
from urllib.parse import urlencode


class Connection:
    def __init__(self, token, marker):
        self.token = token
        self.marker = marker
        self.default_headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Content-Type': 'application/json',
            'X-Access-Token': self.token
        }
    #TODO add gets for airport data, parameterize so that we can change destination and arrival
    def get(self, url, params=None):
        full_url = url + '?' + urlencode(params) if params else url
        return requests.get(full_url, headers=self.default_headers)
    
    def to_prices(self, response):
        json_object = json.loads(response.text)
        return json_object["prices"]
        


