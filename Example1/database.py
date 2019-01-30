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

def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("CREATE TABLE if NOT EXISTS Lyrics(Id INT, Name TEXT)")
        conn.execute("INSERT INTO Lyrics Values(1, I am the very model of a modern Major General")
        conn.execute("INSERT INTO Lyrics Values(2, I am the very model of an Animated Character")

    except Error as e:
        print(e)
    finally:
        conn.close()

def destroy_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("DELETE TABLE IF EXISTS Lyrics")
    except Error as e:
        print(e)
    finally:
        conn.close()


