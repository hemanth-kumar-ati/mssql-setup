from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

def create_db_engine():
    engine = create_engine(f'mssql+pymssql://sa:YourStrong!Passw0rd@localhost:1433/master')
    with engine.connect() as conn:
        # Wrap the raw SQL query in a text() object
        conn.execute(text("IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'DBTest') CREATE DATABASE DBTest;"))
    engine = create_engine(f'mssql+pymssql://sa:YourStrong!Passw0rd@localhost:1433/DBTest')
    Base.metadata.create_all(bind=engine)
    return engine

def test_connection(engine):
    try:
        with engine.connect() as conn:
            return "Connection successful!"
    except Exception as e:
        return f"Connection failed: {str(e)}"

def get_database_names(engine):
    try:
        with engine.connect() as conn:
            query = text("SELECT name FROM sys.databases WHERE database_id > 4")
            result = conn.execute(query)
            databases = [row[0] for row in result]
            return databases
    except Exception as e:
        return f"Failed to get databases: {str(e)}"