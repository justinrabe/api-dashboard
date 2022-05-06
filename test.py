from cxn import Connection
from dotenv import load_dotenv
import os
import json
import mysql.connector
import python_mysql_dbconfig
load_dotenv()

def api_to_db():
    url = os.getenv('url')
    token = os.getenv('api-key')
    connection = Connection(token, os.getenv('marker'))
    response = connection.get(url+token)
    prices = connection.to_prices(response)
    filtered_columns = [{k: v for k, v in d.items() if k == 'price' or k == 'depart_date' or k == 'destination' or k == 'origin'} for d in prices]
    print(filtered_columns)
    python_mysql_dbconfig.insert(filtered_columns)

api_to_db()