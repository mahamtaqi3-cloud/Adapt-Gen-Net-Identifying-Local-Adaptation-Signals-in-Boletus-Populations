import torch
import pandas as pd
import os

# 1. Setup paths
base_path = os.path.dirname(os.path.abspath(__file__))
results_path = os.path.join(os.path.dirname(base_path), 'results', 'adapt_gen_model.pth')

# 2. Model Load Karein
from pipeline.gnn_model import AdaptGenNet
from pipeline.prepare_gnn_data import X_tensor # Tensors ki shape ke liye

model = AdaptGenNet(input_dim=X_tensor.shape[1])
model.load_state_dict(torch.load(results_path))
model.eval()

# 3. Weights Extract Karein
# Hum pehli layer (fc1) ke weights ko dekh rahe hain
weights = model.fc1.weight.data.abs().mean(dim=0).numpy()

# 4. Features ke saath map karein
feature_names = ['CHELSA_bio01', 'CHELSA_bio12', 'CHELSA_bio15']
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': weights})

# 5. Sort aur Save karein
importance_df = importance_df.sort_values(by='Importance', ascending=False)
print("\n--- 🧬 Feature Importance (Top Genes/Features) ---")
print(importance_df)

importance_df.to_csv('results/feature_importance.csv', index=False)
print("\n--- ✅ Results 'results/feature_importance.csv' mein save ho gaye! ---")