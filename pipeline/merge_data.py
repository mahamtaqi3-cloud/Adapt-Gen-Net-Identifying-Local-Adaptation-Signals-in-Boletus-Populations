import pandas as pd
import numpy as np
import os

# 1. Paths Setup
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_path, "data")

snp_matrix_path = os.path.join(data_path, "boletus_snp_matrix.npy")
climate_data_path = os.path.join(data_path, "integrated_climate_data.csv")
output_path = os.path.join(data_path, "final_combined_output.csv")

def merge_data():
    print("--- 🔄 Merging Genomic and Climate Data ---")
    
    # Load Genomic Matrix (Numpy array)
    snp_matrix = np.load(snp_matrix_path)
    
    # Load Climate/Metadata (CSV)
    climate_df = pd.read_csv(climate_data_path)
    
    # Check if rows match
    if snp_matrix.shape[0] != len(climate_df):
        print(f"⚠️ Warning: Row mismatch! Matrix: {snp_matrix.shape[0]}, CSV: {len(climate_df)}")
        return

    # Convert SNP matrix to DataFrame for merging
    snp_df = pd.DataFrame(snp_matrix)
    
    # Merge climate data with SNP data
    final_df = pd.concat([climate_df, snp_df], axis=1)
    
    # Save the combined dataset
    final_df.to_csv(output_path, index=False)
    print(f"--- ✅ Final combined data saved to: {output_path} ---")

if __name__ == "__main__":
    merge_data()