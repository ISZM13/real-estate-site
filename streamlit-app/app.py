import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load the preprocessed dataset
df = pd.read_csv('modified_Housing_Data.csv')

# Streamlit title
st.title('Property Recommendation Engine')

# User input
suburb = st.selectbox('Select Suburb', df['Suburb_Target_Price'].unique())
rooms = st.number_input('Number of Rooms', min_value=1, max_value=10, value=1)
property_type = st.selectbox('Property Type', df['Type_Encoded'].unique())
price = st.number_input('Max Price', min_value=0, value=1000000)
distance = st.number_input('Distance from City (km)', min_value=0.0, value=10.0)
bedroom2 = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=1)
bathroom = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=1)
car = st.number_input('Number of Car Spaces', min_value=0, max_value=10, value=1)
landsize = st.number_input('Landsize (sqm)', min_value=0, value=500)
building_area = st.number_input('Building Area (sqm)', min_value=0, value=100)
year_built = st.number_input('Year Built', min_value=1900, max_value=2024, value=2000)

# Prepare user input DataFrame
user_input = pd.DataFrame({
    'Suburb_Target_Price': [suburb],
    'Rooms': [rooms],
    'Type_Encoded': [property_type],
    'Price': [price],
    'Distance': [distance],
    'Bedroom-to-bathroom Ratio': [bedroom2 / bathroom],
    'Land-to-building Ratio': [building_area / landsize],
    'Age of Building': [2024 - year_built],
    'Age of Building Log': [np.log(2024 - year_built) if 2024 - year_built > 0 else 0]  # Avoid log(0)
})

# Convert Distance to numeric and categorize
user_input['Distance'] = pd.to_numeric(user_input['Distance'], errors='coerce')
user_input['Distance_Category'] = pd.cut(user_input['Distance'], bins=[0, 5, 15, float('inf')], labels=['Near', 'Medium', 'Far'])

# Preprocess user input similar to the dataset
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df.drop(columns=['Price']))
user_input_scaled = scaler.transform(user_input.drop(columns=['Distance_Category']))

# Calculate cosine similarity
similarity_matrix = cosine_similarity(user_input_scaled, df_scaled)
similarities = similarity_matrix[0]

# Get top 10 similar properties
top_indices = similarities.argsort()[-10:][::-1]
recommendations = df.iloc[top_indices]

# Display recommendations
st.write("Top Recommendations:")
st.dataframe(recommendations[['Suburb_Target_Price', 'Rooms', 'Type_Encoded', 'Price', 'Distance_Category', 'Bedroom-to-bathroom Ratio', 'Land-to-building Ratio', 'Age of Building', 'Age of Building Log']].reset_index(drop=True))
