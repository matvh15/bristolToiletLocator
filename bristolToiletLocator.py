

# Let's connect to the local mySQL server and pull the table BRISTOL_DATA.bristol_public_toilets into a df

# imports
import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv, find_dotenv
import os 

# Getting MySQL credentials
load_dotenv(find_dotenv())

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='BRISTOL_DATA',
                                         user=os.environ.get('secretUser'),
                                         password=os.environ.get('secretKey'))
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM bristol_public_toilets")
        bristol_toilet_data = mycursor.fetchall()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

