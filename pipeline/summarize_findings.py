import pandas as pd
import numpy as np
import os

print("📊 --- Initializing Final Evolutionary Project Summary Generation ---")

report_path = "results/isolated_adaptation_genes_report.csv"

if not os.path.exists(report_path):
    raise FileNotFoundError(f"❌ Target report not found at {report_path}! Run isolation script first.")

# Load isolated variant parameters
df = pd.read_csv(report_path)

# Calculate diagnostic metrics
total_mined = len(df)
max_saliency = df['Adaptive_Saliency_Score'].max()
min_saliency = df['Adaptive_Saliency_Score'].min()
mean_saliency = df['Adaptive_Saliency_Score'].mean()

print("\n============================================================")
print("🌍            ADAPT-GEN-NET PIPELINE FINAL METRICS          ")
print("============================================================")
print(f"✅ Total Candidate Loci Mined and Ranked : {total_mined} elements")
print(f"✅ Maximum Activation Peak (Rank 1 SNP)   : {max_saliency:.6f}")
print(f"✅ Baseline Floor Signal (Rank 100 SNP)  : {min_saliency:.6f}")
print(f"✅ Mean Top-Tier Evolutionary Saliency   : {mean_saliency:.6f}")
print("============================================================")

print("\n🚀 Pipeline fully completed! Project is ready for structural presentation.")