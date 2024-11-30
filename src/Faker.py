import random
from faker import Faker
import pandas as pd

# Initialize the Faker instance
fake = Faker()

# Function to generate random vehicle preferences
def generate_vehicle_preference():
    preferences = ['SUV', 'Sedan', 'Hatchback', 'Truck', 'Electric', 'Hybrid', 'Luxury']
    return random.choice(preferences)

# Function to generate random vehicle details
def generate_vehicle_type():
    vehicle_types = ['Gasoline', 'Electric', 'Hybrid', 'Diesel']
    return random.choice(vehicle_types)

# Function to simulate the user data
def generate_user_data(num_samples=500):
    data = []
    for _ in range(num_samples):
        user = {
            'Name': fake.name(),
            'Age': random.randint(18, 70),
            'Height': round(random.uniform(150, 200), 1),  # height in cm
            'Weight': round(random.uniform(50, 120), 1),  # weight in kg
            'Gender': random.choice(['Male', 'Female']),
            'Marital Status': random.choice(['Single', 'Married', 'Divorced']),
            'Occupation': fake.job(),
            'Annual Income': random.randint(20000, 100000),
            'Weekly Travel Distance': random.randint(10, 500),  # km
            'Preferred Vehicle Type': generate_vehicle_preference(),
            'Fuel Type': generate_vehicle_type(),
            'Has Purchased Vehicle': random.choice([True, False]),
            'Vehicle Purchase Year': random.choice([None, random.randint(2015, 2023)]),
        }
        data.append(user)
    return data

# Generate the data for 500 users
user_data = generate_user_data()

# Create a DataFrame for better visualization
df = pd.DataFrame(user_data)

# Show the first few rows
print(df.head())

# Optionally, save it to a CSV file
df.to_csv('simulated_user_data.csv', index=False)