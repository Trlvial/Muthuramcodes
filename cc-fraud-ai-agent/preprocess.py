import pandas as pd

# Load the dataset
data = pd.read_csv("dataset/AIML Dataset.csv")

# Show the first five rows
print("\nFirst 5 rows:")
print(data.head())

# Dataset information
print("\nDataset Info:")
print(data.info())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Show fraud counts
print("\nFraud Distribution:")
print(data["isFraud"].value_counts())
