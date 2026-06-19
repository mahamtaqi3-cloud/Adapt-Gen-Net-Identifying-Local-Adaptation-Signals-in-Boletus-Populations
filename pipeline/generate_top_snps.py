import torch
import pandas as pd
import os

def generate_top_snps():
    # Paths set karein
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(base_dir, 'results')
    data_dir = os.path.join(base_dir, 'data')
    
    model_path = os.path.join(results_dir, 'adapt_gen_model.pth')
    metadata_path = os.path.join(base_dir, 'sample_metadata.csv')
    
    # 1. Model Load karein
    from pipeline.gnn_model import AdaptGenNet
    # Input dimension 3 hai (aapke climate features ke hisaab se)
    model = AdaptGenNet(input_dim=3) 
    model.load_state_dict(torch.load(model_path))
    model.eval()

    # 2. Metadata Load karein (Jahan SNPs ki list hai)
    # Hum maan rahe hain ki is file mein 'position' column hai
    metadata = pd.read_csv(metadata_path)
    
    # 3. Model Weights se Importance nikalein
    # Hum pehli layer ke weights ko SNPs ki importance maan rahe hain
    weights = model.fc1.weight.data.abs().mean(dim=0).numpy()
    
    # 4. Data frame banayein
    # Yahan hum assume kar rahe hain ki metadata mein SNPs aur model weights match ho rahe hain
    snp_df = metadata.copy()
    snp_df['importance'] = weights[:len(snp_df)] # Weights ko SNPs ke saath map karna
    
    # 5. Top SNPs filter karein (Threshold: Importance > Mean)
    threshold = snp_df['importance'].mean()
    top_snps = snp_df[snp_df['importance'] > threshold]
    
    # 6. Save karein
    output_path = os.path.join(results_dir, 'top_adaptive_snps.csv')
    top_snps.to_csv(output_path, index=False)
    
    print(f"--- ✅ 'top_adaptive_snps.csv' generate ho gayi! ({len(top_snps)} SNPs milay) ---")

if __name__ == "__main__":
    generate_top_snps()