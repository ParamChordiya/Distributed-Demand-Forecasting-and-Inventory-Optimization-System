# main.py

from data_ingestion import ingest_data_to_mongodb
from distributed_prediction import distributed_training
import threading
import generate_dummy_data

def start_api():
    """
    Starts the Flask API server.
    """
    from app import app
    app.run(debug=False, use_reloader=False)

def main():
    # Step 0: Generate dummy data
    generate_dummy_data.generate_dummy_sales_data('sales_data.csv')

    # Step 1: Ingest data into MongoDB
    csv_file = 'sales_data.csv'
    db_name = 'inventory_db'
    collection_name = 'sales_collection'
    ingest_data_to_mongodb(csv_file, db_name, collection_name)

    # Step 2: Distributed training of demand forecasting models
    product_ids = list(range(1, 11))  # Product IDs from 1 to 10
    model_files = distributed_training(product_ids)
    print(f"Trained models: {model_files}")

    # Step 3: Start the API server in a separate thread
    api_thread = threading.Thread(target=start_api)
    api_thread.start()
    print("API server is running...")

if __name__ == '__main__':
    main()
