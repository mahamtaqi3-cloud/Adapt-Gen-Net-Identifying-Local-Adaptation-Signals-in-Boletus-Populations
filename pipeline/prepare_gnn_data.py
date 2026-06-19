import pandas as pd
import numpy as np
import torch
import os

# 1. Sahi Path Setup
base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, 'final_adaptation_dataset.csv')

# 2. Data Load karein
df = pd.read_csv(data_path)
print(f"--- ✅ Data load hua! Rows: {len(df)} ---")

# --- DEBUG: Asli column naam check karein ---
print("Yeh rahe aapki CSV file ke column names. Inmein se koi ek copy karein:")
print(df.columns.tolist())
# ---------------------------------------------

# 3. Yahan 'target_col' mein list mein se sahi naam paste karein
# Example: target_col = 'Adaptation_Score' 
# Purani line (jahan error aa raha hai): 
# target_col = 'Yahan_Apna_Sahi_Column_Naam_Paste_Karein'

# Nayi line (ye exact likhein):
target_col = 'Climate_Value'

# Features (Columns)
cols = ['CHELSA_bio01_1981-2010_V.2.1.tif', 
        'CHELSA_bio12_1981-2010_V.2.1.tif', 
        'CHELSA_bio15_1981-2010_V.2.1.tif']

# Check agar target column exist karta hai
if target_col not in df.columns:
    print(f"\n❌ ERROR: '{target_col}' naam ka column nahi mila!")
    print("Upar di gayi list mein se sahi naam copy karke code mein update karein.")
    exit()

X = df[cols].values
Y = df[target_col].values 

# 4. Tensors
X_tensor = torch.tensor(X, dtype=torch.float32)
Y_tensor = torch.tensor(Y, dtype=torch.float32).view(-1, 1)

print(f"\n--- 📊 Tensors Tayyar! ---")
print(f"X shape: {X_tensor.shape}, Y shape: {Y_tensor.shape}")