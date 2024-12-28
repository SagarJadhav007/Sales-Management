import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the sales dataset (replace 'sales_data' with the path to your file)
data = pd.read_csv(r'C:\Users\jadha\OneDrive\Desktop\FDS PROJECT\india_sales_data_random2.csv')

# Display the first few rows of the dataset
print(data.head())

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Check for missing values
print(data.isnull().sum())

# Optionally, drop rows with missing values or handle them accordingly
data.dropna(inplace=True)

# Create new features: Year, Month, Day of the week
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day_name()

# Check the updated dataset
print(data.head())

# Group sales by month and year to observe monthly sales trends
monthly_sales = data.groupby(data['Date'].dt.to_period('M'))['SalesAmount'].sum()

# Plot the monthly sales trends
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o',markercolor='yellow', color='blue', title='Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Group by 'Product' to get total sales for each product
top_products = data.groupby('Product')['SalesAmount'].sum().sort_values(ascending=False).head(10)

# Plot the top 5 products by sales amount
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='green', title='Top 5 Selling Products')
plt.xlabel('Product')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Group by 'StoreLocation' to get total sales for each location
sales_by_region = data.groupby('StoreLocation')['SalesAmount'].sum()

# Plot sales by region using a pie chart
plt.figure(figsize=(8, 8))
sales_by_region.plot(kind='pie', autopct='%1.1f%%', title='Sales by Region', colors=sns.color_palette("Set2"))
plt.ylabel('')  # Remove the default y-label
plt.show()

# Group by 'CustomerID' to get the average order value and total sales for each customer
customer_sales = data.groupby('CustomerID').agg({
    'SalesAmount': ['mean', 'sum']
}).reset_index()

customer_sales.columns = ['CustomerID', 'AvgOrderValue', 'TotalSales']

# Display top customers based on total sales
top_customers = customer_sales.sort_values(by='TotalSales', ascending=False).head(10)
print(top_customers)

# Extract the hour from the Date column
data['Hour'] = data['Date'].dt.hour

# Pivot table to calculate total sales for each day and hour
sales_heatmap = data.pivot_table(index='Day', columns='Hour', values='SalesAmount', aggfunc='sum')

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(sales_heatmap, cmap='Blues', linewidths=0.5, annot=True, fmt='.0f')
plt.title('Sales Heatmap by Day of the Week and Hour of the Day')
plt.show()

# Group sales by Month and Product
monthly_sales_by_product = data.groupby(['Month', 'Product'])['SalesAmount'].sum().unstack()

# Filter the data to include only the first four months (January to April)
monthly_sales_by_product = monthly_sales_by_product.loc[1:4]

# Plot a grouped bar chart with Month names on the x-axis and Products as the bars
plt.figure(figsize=(12, 8))
monthly_sales_by_product.plot(kind='bar', stacked=False, width=0.8, colormap='tab20')

# Manually define month names for January to April
month_names = ['January', 'February', 'March', 'April']
plt.xticks(ticks=range(4), labels=month_names, rotation=45)

plt.title('Monthly Sales Analysis by Product (Jan-Apr)')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.show()

