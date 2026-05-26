# importing libraries
import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path

np.random.seed(42)
Faker.seed(42)
fake = Faker()

num_records = 1000

# SYNTHETIC DATASET GENERATION

data = {
    "customer_id": range(1, num_records + 1),
    
    "age": np.random.randint(18, 65, num_records),
    
    "gender": np.random.choice(
        ["Male", "Female"],
        num_records
    ),
    
    "country": np.random.choice(
        ["Ghana", "Nigeria", "Kenya", "South Africa"],
        num_records
    ),
    
    "device_type": np.random.choice(
        ["Mobile", "Desktop", "Tablet"],
        num_records
    ),
    
    "session_duration": np.random.randint(
        1, 120, num_records
    ),
    
    "pages_visited": np.random.randint(
        1, 50, num_records
    ),
    
    "products_viewed": np.random.randint(
        1, 30, num_records
    ),
    
    "cart_additions": np.random.randint(
        0, 15, num_records
    ),
    
    "purchases": np.random.randint(
        0, 10, num_records
    ),
    
    "total_spent": np.round(
        np.random.uniform(10, 5000, num_records),
        2
    ),
    
    "last_purchase_days": np.random.randint(
        1, 365, num_records
    ),
    
    "membership_status": np.random.choice(
        ["Basic", "Premium"],
        num_records
    ),
    
    "discount_used": np.random.choice(
        ["Yes", "No"],
        num_records
    )
}

df = pd.DataFrame(data)

# Create churn column
df["churn"] = np.where(
    (
        (df["last_purchase_days"] > 180) &
        (df["purchases"] < 3)
    ),
    1,
    0
)

print("Dataset generated successfully")


# Save to CSV
df.to_csv("./data/ecommerce_customers.csv", index=False)

print("Dataset saved successfully")
