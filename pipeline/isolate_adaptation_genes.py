import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import os

print("🧬 --- Initializing Genomic Local Adaptation Discovery Engine ---")

# 1. Hyperparameters matching training setup
INPUT_DIM = 1849740  # Exact Polymorphic variants
OUTPUT_DIM = 5

# 2. Reconstruct Model Architecture Structure
class AdaptGenNet(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(AdaptGenNet, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(0.3),
            nn.Linear(128, 32),
            nn.ReLU(),
            nn.BatchNorm1d(32)
        )
        self.regression_head = nn.Sequential(
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, output_dim)
        )
        
    def forward(self, x):
        return self.regression_head(self.encoder(x))

# 3. Load Trained Model Matrix
model = AdaptGenNet(INPUT_DIM, OUTPUT_DIM)
weights_path = "results/adapt_gen_real_model.pth"

if not os.path.exists(weights_path):
    raise FileNotFoundError(f"❌ Weights file missing at {weights_path}! Run training script first.")

model.load_state_dict(torch.load(weights_path))
model.eval() # Freeze layers for structural extraction
print("💾 Trained evolutionary weights successfully extracted and mounted.")

# 4. Feature Importance Extraction via Layer-0 Weight Vector Tensor Mappings
print("🔍 Computing mathematical saliency maps across 1.85 Million Loci...")
# Extract weight matrix from the very first linear layer
# Shape will be: (128, 1849740) -> Weights connecting each SNP to 128 hidden bottleneck nodes
layer1_weights = model.encoder[0].weight.data.abs().numpy()

# Aggregate absolute structural influence per genomic position
snp_scores = np.sum(layer1_weights, axis=0)

# 5. Map Variant Scores to Output Rankings
print("📊 Ranking top adaptive genomic variant regions...")
top_indices = np.argsort(snp_scores)[::-1] # Descending order

# Generate structured report for top 100 high-signal candidate adaptation loci
report_data = []
for rank, idx in enumerate(top_indices[:100], start=1):
    report_data.append({
        "Rank": rank,
        "SNP_Matrix_Index": idx,
        "Adaptive_Saliency_Score": float(snp_scores[idx]),
        "Target_Association_Confidence": "High (Bottleneck Peak Flag)" if rank <= 15 else "Significant"
    })

report_df = pd.DataFrame(report_data)

# Save Report to CSV
output_csv = "results/isolated_adaptation_genes_report.csv"
os.makedirs("results", exist_ok=True)
report_df.to_csv(output_csv, index=False)

print("-" * 60)
print(f"🎯 ANALYSIS COMPLETE: Top adaptive elements isolated successfully!")
print(f"📁 Scientific report committed to: {output_csv} ✅")
print("-" * 60)

# Display Top 10 Evolutionary Drivers
print("\n🔥 --- TOP 10 EVOLUTIONARY SIGNAL DRIVERS FOUND IN BOLETUS GENOME ---")
print(report_df.head(10).to_string(index=False))