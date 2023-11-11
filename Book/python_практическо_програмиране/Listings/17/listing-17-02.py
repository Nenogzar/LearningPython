from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
 
def get_config(filename='connect.ini', section='mysql'):
    # създаваме парсер и четем ini-файла
    parser = ConfigParser()
    parser.read(filename)
 
    # по подразбиране четем от секция  mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('Error while reading connect.ini')
 
    return db

def connect():
    db_config = get_config()

    try:
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')

if __name__ == '__main__':
    connect()
