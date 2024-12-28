import pandas as pd
import numpy as np

# New store locations and products
store_locations = ['Hyderabad', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow']
products = ['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E']
num_records = 100

# Create new random data
new_data = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=num_records, freq='D'),
    'Product': np.random.choice(products, num_records),
    'Quantity': np.random.randint(5, 20, size=num_records),
    'CustomerID': np.random.randint(2000, 3000, size=num_records),
    'StoreLocation': np.random.choice(store_locations, num_records)
})

# Unit prices for the new products
unit_prices = {
    'Product_A': 150,
    'Product_B': 450,
    'Product_C': 350,
    'Product_D': 550,
    'Product_E': 250
}

# Calculate SalesAmount as Quantity * Unit Price
new_data['SalesAmount'] = new_data.apply(lambda row: row['Quantity'] * unit_prices[row['Product']], axis=1)

# Shuffle and reset index
new_data = new_data.sample(frac=1).reset_index(drop=True)

# Save the new dataset to a CSV file
new_file_path = r'C:\Users\jadha\OneDrive\Desktop\FDS PROJECT/india_sales_data_random2.csv'
new_data.to_csv(new_file_path, index=False)

print(new_file_path)
