from dotenv import load_dotenv
import pyodbc
import os

load_dotenv()

def create_connection(): 
    
    connection = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=tcp:neptune-db.database.windows.net,1433;"
    "DATABASE=neptune-db;"
    f'UID={os.getenv("DB_USERNAME")};'
    f'PWD={os.getenv("DB_PASSWORD")};'
    "ENCRYPT=yes;"
    "TRUSTSERVERCERTIFICATE=no;"
    "CONNECTION TIMEOUT=30;"
    )
    
    return connection