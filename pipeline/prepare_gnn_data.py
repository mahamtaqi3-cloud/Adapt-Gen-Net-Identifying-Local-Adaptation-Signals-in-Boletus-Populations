import pandas as pd
import numpy as np
import torch
import os

# 1. Correct Path Setup
base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, 'final_adaptation_dataset.csv')

# 2. Load Data
df = pd.read_csv(data_path)
print(f"--- ✅ Data loaded! Rows: {len(df)} ---")

# --- DEBUG: Check real column names
print("These are the real names of your CSV Column. Copy anyone of them:")
print(df.columns.tolist())
# ---------------------------------------------

# 3.Paste correct name from list in 'target_col'
# Example: target_col = 'Adaptation_Score' 
# Old line (where is error): 
# target_col = 'Paste your correct column name'

# New line (write exactly):
target_col = 'Climate_Value'

# Features (Columns)
cols = ['CHELSA_bio01_1981-2010_V.2.1.tif', 
        'CHELSA_bio12_1981-2010_V.2.1.tif', 
        'CHELSA_bio15_1981-2010_V.2.1.tif']

# Check if target column exists
if target_col not in df.columns:
    print(f"\n❌ ERROR: '{target_col}' column's anme not found!")
    print("Paste correct name from the given list above.")
    exit()

X = df[cols].values
Y = df[target_col].values 

# 4. Tensors
X_tensor = torch.tensor(X, dtype=torch.float32)
Y_tensor = torch.tensor(Y, dtype=torch.float32).view(-1, 1)

print(f"\n--- 📊 Tensors Ready! ---")
print(f"X shape: {X_tensor.shape}, Y shape: {Y_tensor.shape}")
