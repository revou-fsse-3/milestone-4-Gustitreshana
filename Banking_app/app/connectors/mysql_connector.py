from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# Get the database credentials from the environment variables
username = os.getenv('DATABASE_USERNAME')
password = os.getenv('DATABASE_PASSWORD')
host = os.getenv('DATABASE_URL')
database = os.getenv('DATABASE_NAME')

try:
    # Connect to the database
    print(f'Connecting to the database at {host}...')
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database}')
    connection = engine.connect()
    Session = sessionmaker(connection)
    
    # If the connection is successful
    print(f'Connected to the database at {host}...')

except Exception as e:
    # If there is an error connecting to the database
    print(f'Error connecting to the database: {e}')
