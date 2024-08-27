import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import NearestNeighbors
import joblib
import streamlit as st


# URL to download the file
url = 'https://drive.google.com/file/d/183NSodNdbgNBKeNsTtb5wbqfpBz1vB0L/view?usp=drive_link'

# Read the CSV file directly from the link
df = pd.read_csv(url)

# Proceed with your operations on the dataframe


# Handle NaN or Inf values
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

# Streamlit app layout
st.title('Property Recommendation System')

# Load the trained model and scaler
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')
label_encoders = joblib.load('label_encoders.joblib')

# Function to preprocess user input
def preprocess_user_input(user_input):
    # Ensure column names match
    user_input = user_input.rename(columns={
        'Bedroom-to-Bathroom Ratio': 'Bedroom-to-bathroom Ratio',
        'Land-to-Building Ratio': 'Land-to-building Ratio'
    })
    
    # Handle unseen labels in categorical columns
    for column, le in label_encoders.items():
        if column in user_input.columns:
            # Add new categories to the encoder if needed
            existing_labels = set(le.classes_)
            user_labels = set(user_input[column].unique())
            new_labels = user_labels - existing_labels
            if new_labels:
                # Print or log the new labels (you can choose to handle this differently)
                print(f"New labels detected for {column}: {new_labels}")
                
                # Map new labels to a default value, such as the most frequent label
                default_value = le.transform([le.classes_[0]])[0]
                user_input[column] = user_input[column].apply(lambda x: le.transform([x])[0] if x in existing_labels else default_value)
            else:
                user_input[column] = le.transform(user_input[column])
    
    # Ensure user input data is of type float
    user_input = user_input.astype(float)
    
    # Scale the user input
    user_input_scaled = scaler.transform(user_input)
    
    return user_input_scaled

# Function to get recommendations
def get_recommendations(user_input):
    # Ensure the columns match the training data
    expected_columns = df_features.columns
    # Ensure all required columns are present
    user_input = user_input[expected_columns]
    
    user_input_scaled = preprocess_user_input(user_input)
    distances, indices = model.kneighbors(user_input_scaled)
    top_indices = indices[0]  # Get indices of nearest neighbors
    return df.iloc[top_indices]

# User input form
st.sidebar.header('User Input')
user_rooms = st.sidebar.number_input('Rooms', min_value=1, value=3)
user_car = st.sidebar.number_input('Car', min_value=0, value=1)
user_region = st.sidebar.selectbox('Region', df['Regionlabel'].unique())
user_suburb_target_price = st.sidebar.number_input('Suburb Target Price', value=0)
user_council_area = st.sidebar.selectbox('Council Area', df['Council_Area_Encoded'].unique())
user_type = st.sidebar.selectbox('Type', df['Type_Encoded'].unique())
user_method = st.sidebar.selectbox('Method', df['Method_Encoded'].unique())
user_bedroom_bathroom_ratio = st.sidebar.number_input('Bedroom-to-Bathroom Ratio', value=1.0)
user_land_building_ratio = st.sidebar.number_input('Land-to-Building Ratio', value=1.0)
user_age_building = st.sidebar.number_input('Age of Building', value=10)
user_distance_category = st.sidebar.selectbox('Distance Category', df['Distance_Category'].unique())
user_age_building_log = st.sidebar.number_input('Age of Building Log', value=2.0)

# Create a DataFrame from user input
user_input = pd.DataFrame({
    'Rooms': [user_rooms],
    'Car': [user_car],
    'Regionlabel': [user_region],
    'Suburb_Target_Price': [user_suburb_target_price],
    'Council_Area_Encoded': [user_council_area],
    'Type_Encoded': [user_type],
    'Method_Encoded': [user_method],
    'Bedroom-to-bathroom Ratio': [user_bedroom_bathroom_ratio],
    'Land-to-building Ratio': [user_land_building_ratio],
    'Age of Building': [user_age_building],
    'Distance_Category': [user_distance_category],
    'Age of Building Log': [user_age_building_log]
})

# Get recommendations
recommendations = get_recommendations(user_input)

# Display recommendations
st.write('Top 10 Property Recommendations:')
st.write(recommendations)
