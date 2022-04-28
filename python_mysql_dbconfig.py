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

def fetch_sql():
    try:
      
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT question, name, isCorrect FROM questions q join answers a on q.id = a.questionID")

        row = cursor.fetchone()

        ##for each entry in questions, there is a list of answers. 
        while row is not None:
            if row[0] in qaTotal.keys():
                #question exists
                qaTotal[row[0]].append({row[1]: row[2]})
            else:
                #new question, insert new dictionary entry with answer as list of size 
                qaTotal[row[0]] = [{row[1]: row[2]}]
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
