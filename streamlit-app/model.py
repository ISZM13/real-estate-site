import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import NearestNeighbors
import joblib

# Load and preprocess the dataset
df = pd.read_csv('datasets/modified_Housing_Data.csv')

# Check for and handle NaN or Inf values
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Initialize encoders
label_encoders = {}
categorical_columns = ['Distance_Category']

# Encode categorical columns
for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Prepare features and target
df_features = df.drop(columns=['Suburb_Target_Price'])  # Drop the target variable
df_features = df_features.astype(float)

# Scale the features
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_features)

# Train NearestNeighbors model
model = NearestNeighbors(n_neighbors=10)  # Find top 10 nearest neighbors
model.fit(df_scaled)

# Save the model and scaler
joblib.dump(model, 'model.joblib')
joblib.dump(scaler, 'scaler.joblib')
joblib.dump(label_encoders, 'label_encoders.joblib')
