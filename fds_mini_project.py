# -*- coding: utf-8 -*-
"""FDS_Mini Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ee9q-kLVc6DCAqfhmS0pP3GegUI-surN
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the IPL dataset
data = pd.read_csv('C:ipl_2023_dataset.csv')
print("-------------------------------------------------------------------------")


# Display the first few rows
print(data.head())
print("-------------------------------------------------------------------------")


# Check for missing values
print(data.isnull().sum())
print("-------------------------------------------------------------------------")

# Mean
mean_price = data['Cost in Rs. (CR)'].mean()
print(f'Mean Price: {mean_price:.2f} Crores')

# Standard Deviation
std_dev_price = data['Cost in Rs. (CR)'].std()
print(f'Standard Deviation: {std_dev_price:.2f} Crores')

# Variance
variance_price = data['Cost in Rs. (CR)'].var()
print(f'Variance: {variance_price:.2f} Crores')

# Range
price_range = data['Cost in Rs. (CR)'].max() - data['Cost in Rs. (CR)'].min()
print(f'Price Range: {price_range:.2f} Crores')

# Drop missing values if necessary
data.dropna(inplace=True)
print("-------------------------------------------------------------------------")

# Analyze top players by auction price
top_players = data.groupby('Player Name')['Cost in Rs. (CR)'].sum().sort_values(ascending=False).head(10)

# Plot the top players
plt.figure(figsize=(10, 7))
top_players.plot(kind='bar', color='orange', title='Top Players by Auction Price')
plt.xlabel('Player')
plt.ylabel('Price (in Crores)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
print("")
print("-------------------------------------------------------------------------")


# Team spending analysis (use '2023 Squad' instead of 'Team')
team_spending = data.groupby('2023 Squad')['Cost in Rs. (CR)'].sum()


# Plot spending by team
plt.figure(figsize=(10, 6))
team_spending.plot(kind='pie', autopct='%1.1f%%', title='Total Spending by Team', colors=sns.color_palette("Set2"))
plt.ylabel('')
plt.show()
print("")
print("-------------------------------------------------------------------------")


# Function to analyze top teams by average price
def average_team_spending(data):
    avg_team_spending = data.groupby('2023 Squad')['Cost in Rs. (CR)'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    avg_team_spending.plot(kind='bar', color='skyblue', title='Average Player Price by Team')
    plt.xlabel('Team')
    plt.ylabel('Average Price (in Crores)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Function to plot player price distribution
def plot_price_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Cost in Rs. (CR)'], bins=20, kde=True)
    plt.title('Distribution of Player Prices')
    plt.xlabel('Price (in Crores)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Function to analyze spending by player role (use 'Type' instead of 'Role')
def role_spending_analysis(data):
    role_spending = data.groupby('Type')['Cost in Rs. (CR)'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    role_spending.plot(kind='bar', color='lightgreen', title='Total Spending by Player Role')
    plt.xlabel('Role')
    plt.ylabel('Total Price (in Crores)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Function to save analysis results to CSV
def save_analysis_results(data):
    team_spending = data.groupby('2023 Squad')['Cost in Rs. (CR)'].sum()
    team_spending.to_csv('team_spending_analysis.csv', header=True)

# Call the functions to execute the analysis
average_team_spending(data)
print("")
print("-------------------------------------------------------------------------")
plot_price_distribution(data)
print("")
print("-------------------------------------------------------------------------")
role_spending_analysis(data)
print("")
print("-------------------------------------------------------------------------")
save_analysis_results(data)
