from cxn import Connection
import os
from dotenv import load_dotenv

load_dotenv()
url = "http://api.travelpayouts.com/v2/prices/nearest-places-matrix?currency=usd&origin=SAN&destination=SFO&show_to_affiliates=true&token="
token = os.getenv('api-key')
connection = Connection(token, os.getenv('marker'))
response = connection.get(url+token)
with open ("response.json", "w") as f:
    f.write(response.text)