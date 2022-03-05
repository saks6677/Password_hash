#use only once
import sqlite3

try:
    sqliteConnection = sqlite3.connect('Username_password_test.db')
    sqlite_create_table_query = '''CREATE TABLE Username_password (
                                
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                mobile text NOT NULL UNIQUE,
                                password text NOT NULL ,
                                gender text NOT NULL,
                                country NOT NULL,
                                hashedpassword NOT NULL);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")