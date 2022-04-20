from cxn import Connection
url = "http://api.travelpayouts.com/v2/prices/nearest-places-matrix?currency=usd&origin=BCN&destination=HKT&show_to_affiliates=true&token=f4f79296899cf9cb265edc4d040344b8"

connection = Connection("f4f79296899cf9cb265edc4d040344b8", "359944")
response = connection.get(url)
print (response)