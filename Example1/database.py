import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	"""Create a database connection to a SQLite db"""
	try:
		conn = sqlite3.connect(db_file)
		#Print something, to show connect success.
		print(sqlite3.version)
	except Error as e:
		print(e)
	finally:
		conn.close()

#Need to create db
#need to destroy db
#Need to pre-fill db
#CRUD = create, read, update, destroy

def prefill_database(db_file):
    """Prefills The database with the lyrics"""
    try:
        create_connection(db_file)
        #fills with the lyrics
    except Error as e:
        print(e)
    finally:
        conn.close()
