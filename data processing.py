import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Load the dataset
file_path = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\Space_Dataset.csv"
data = pd.read_csv(file_path)

print("Initial dataset loaded:")
print(data.head())

# Clean up column names by stripping leading/trailing spaces
data.columns = data.columns.str.strip()

# Clean the 'Rocket' column by removing commas and stripping spaces
data['Rocket'] = data['Rocket'].str.replace(',', '').str.strip().astype(float)

# Handle missing values by filling them with the median
data['Rocket'].fillna(data['Rocket'].median(), inplace=True)

# Convert 'DateTime' column to datetime format
data['DateTime'] = pd.to_datetime(data['DateTime'])

# Drop redundant columns
data.drop(columns=['Detail', 'Date', 'Time'], inplace=True)

# Encode categorical variables
label_encoders = {}
for column in ['Company Name', 'Location', 'Status Rocket', 'Status Mission', 'Country of Launch', 'Companys Country of Origin', 'Private or State Run']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

print("Categorical columns encoded:")
print(data.head())

# Normalize numerical features
scaler = StandardScaler()
data[['Rocket', 'Year', 'Month', 'Day']] = scaler.fit_transform(data[['Rocket', 'Year', 'Month', 'Day']])

print("Numerical columns normalized:")
print(data.head())

# Example of using nltk to process text data in the 'Location' column
def preprocess_text(text):
    if isinstance(text, str):
        tokens = word_tokenize(text)
        tokens = [word.lower() for word in tokens if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        return ' '.join(filtered_tokens)
    else:
        return ''

data['Location'] = data['Location'].apply(preprocess_text)

print("Text data in 'Location' column processed:")
print(data['Location'].head())

# Save the processed dataset to a new CSV file
processed_file_path = './Processed_Global_Space_Launches.csv'
data.to_csv(processed_file_path, index=False)
print(f"Processed data saved to {processed_file_path}")
