# distributed_prediction.py

import os
from multiprocessing import Pool
from pymongo import MongoClient
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_model_for_product(product_id):
    """
    Train a demand forecasting model for a specific product.
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['inventory_db']
    collection = db['sales_collection']

    # Retrieve data for the specific product
    data = pd.DataFrame(list(collection.find({'product_id': product_id})))

    # Check if data is sufficient
    if data.shape[0] < 2:
        client.close()
        return None

    # Features and target variable
    X = data[['feature1', 'feature2']]
    y = data['demand']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Ensure the models directory exists
    os.makedirs('models', exist_ok=True)

    # Save the model to a file
    model_file = f'models/model_product_{product_id}.pkl'
    with open(model_file, 'wb') as f:
        pickle.dump(model, f)

    client.close()
    return model_file

def distributed_training(product_ids):
    """
    Train models for multiple products in parallel.
    """
    with Pool() as pool:
        model_files = pool.map(train_model_for_product, product_ids)
    return [mf for mf in model_files if mf is not None]
