from pymongo import MongoClient
import pandas as pd

def ingest_data_to_mongodb(csv_file, db_name, collection_name):
    """
    Ingest data from a CSV file into MongoDB collection.
    """
    # Connect to MongoDB (adjust host and port as needed)
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]

    # Read data from CSV file
    data = pd.read_csv(csv_file)

    # Convert DataFrame to dictionary and insert into MongoDB
    collection.insert_many(data.to_dict('records'))

    # Close the connection
    client.close()
