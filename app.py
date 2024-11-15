# app.py

import os
from flask import Flask, request, jsonify
from optimization import optimize_inventory
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict demand based on input features.
    """
    # Extract product_id and features from the request
    product_id = request.json['product_id']
    features = np.array(request.json['features']).reshape(1, -1)

    # Load the corresponding model
    model_file = f'models/model_product_{product_id}.pkl'
    try:
        with open(model_file, 'rb') as f:
            model = pickle.load(f)
    except FileNotFoundError:
        return jsonify({'error': 'Model not found for the specified product_id'}), 404

    # Predict demand
    demand_forecast = model.predict(features).tolist()

    return jsonify({'demand_forecast': demand_forecast})
