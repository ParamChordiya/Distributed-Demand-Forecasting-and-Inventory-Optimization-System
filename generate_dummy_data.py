# generate_dummy_data.py

import pandas as pd
import numpy as np

def generate_dummy_sales_data(csv_file, num_records=1000, num_products=10):
    """
    Generate dummy sales data and save it to a CSV file.
    """
    np.random.seed(42)  # For reproducibility

    data = {
        'product_id': np.random.choice(range(1, num_products + 1), num_records),
        'feature1': np.random.uniform(0, 10, num_records),
        'feature2': np.random.uniform(0, 20, num_records),
        'demand': np.random.poisson(20, num_records)
    }

    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    print(f"Dummy sales data generated and saved to {csv_file}")

if __name__ == '__main__':
    generate_dummy_sales_data('sales_data.csv')
