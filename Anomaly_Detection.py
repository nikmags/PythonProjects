# The purpose of this program is to identify anomalous data metrics/data within a data set and visualize it via a graphical format.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the provided CSV file
file_path = '' # input file path here
data = pd.read_csv(file_path)

# Specify the columns to visualize
columns_to_visualize = [
    'Total Fraud',
    'Total Fraud Attempt Rate',
    'Total Fraud Capture Rate'
    # Add any other columns you want to visualize
]

# Function to calculate Z-scores for a given column
"""
The Z-score is a statistical measurement that describes a value's relationship to the mean of a group of values. It is measured in terms of standard deviations from the mean. 
Z-scores are particularly useful for anomaly detection because they standardize different datasets to a common scale.
1. Standardization: Z-scores transform data to a scale where the mean of the data is 0 and the standard deviation is 1. 
This makes it easier to identify values that are significantly different from the mean.
2. Outlier Detection: Values with high absolute Z-scores (typically above 3 or below -3) can be considered outliers or anomalies. 
These values are far from the mean and can indicate unusual or suspicious behavior.

Outlier Detection: Values with high absolute Z-scores (typically above 3 or below -3) can be considered outliers or anomalies. 
hese values are far from the mean and can indicate unusual or suspicious behavior.
"""
def calculate_z_scores(df, column):
    mean = df[column].mean()
    std = df[column].std()
    z_scores = (df[column] - mean) / std
    return z_scores

# Define a threshold for identifying anomalies (e.g., Z-score > 3)
threshold = 3

# List to store anomalies for all columns
all_anomalies = pd.DataFrame()

# Iterate over each specified column and calculate anomalies
for column in columns_to_visualize:
    data[f'{column} Z-Score'] = calculate_z_scores(data, column)
    anomalies = data[abs(data[f'{column} Z-Score']) > threshold]
    if not anomalies.empty:
        all_anomalies = pd.concat([all_anomalies, anomalies])

# Removing duplicate anomalies
all_anomalies = all_anomalies.drop_duplicates()

# Display the anomalies dataframe
print("Anomalies in Fraud Data:")
print(all_anomalies)

# Function to plot time series data with anomalies
def plot_anomalies(df, column, anomalies, title):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Week'], df[column], label=column, color='blue')
    plt.scatter(anomalies['Week'], anomalies[column], color='red', label='Anomalies')
    plt.xlabel('Week')
    plt.ylabel(column)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=90)
    plt.show()

# Plotting anomalies for each specified column
for column in columns_to_visualize:
    plot_anomalies(data, column, all_anomalies, f'{column} with Anomalies')
