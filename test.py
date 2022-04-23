from cxn import Connection
from dotenv import load_dotenv
import os
import json
import mysql.connector

load_dotenv()
url = "http://api.travelpayouts.com/v2/prices/nearest-places-matrix?currency=usd&origin=SAN&destination=SFO&show_to_affiliates=true&token="
token = os.getenv('api-key')
connection = Connection(token, os.getenv('marker'))
response = connection.get(url+token)
jsonObject = json.loads(response.text)
prices = jsonObject["prices"]
filtered_columns = [{k: v for k, v in d.items() if k == 'price' or k == 'depart_date'} for d in prices]
print(type(filtered_columns[0]["depart_date"]))

