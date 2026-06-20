import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import os

# 1. Model Structure (That should be the one as in train_model.py)
model = nn.Sequential(
    nn.Linear(128, 128),
    nn.ReLU(),
    nn.Linear(128, 3)
)

# 2. Load the model
if os.path.exists('trained_model.pth'):
    model.load_state_dict(torch.load('trained_model.pth', map_location='cpu'), strict=False)
    model.eval()
    print("✅ Model loaded!")

    # 3. Take importance out of weights
    #  Model[0] will access the first layer (Linear layer)
    weights = model[0].weight.data.numpy()
    importance = np.mean(np.abs(weights), axis=0)

    # 4. Top 10 Indices
    top_indices = np.argsort(importance)[-10:][::-1]
    print("🌟 TOP 10 ADAPTIVE SNP INDICES:")
    print(top_indices)

    # 5. Save results
    pd.DataFrame({'SNP_Index': top_indices}).to_csv('top_adaptive_snps.csv', index=False)
    print("✅ Result 'top_adaptive_snps.csv' are saved!")

else:
    print("❌ ERROR: 'trained_model.pth' not found. Run train_model.py first.")
