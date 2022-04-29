from configparser import ConfigParser
from mysql.connector import MySQLConnection, Error

def read_db_config(filename='mysql.env', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


def insert(data):
    try:
      
        dbconfig = read_db_config()
        db = MySQLConnection(**dbconfig)
        cursor = db.cursor()
        query = 'INSERT INTO prices (origin, destination, price, depart_date) VALUES (%(origin)s, %(destination)s,%(price)s,%(depart_date)s)'
        cursor.executemany(query, data)
        db.commit()

    except Error as e:
        print(e)

    finally:
        db.close()
        cursor.close()
        
