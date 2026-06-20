import torch
import pandas as pd
import os

def generate_top_snps():
    # Set the Paths 
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(base_dir, 'results')
    data_dir = os.path.join(base_dir, 'data')
    
    model_path = os.path.join(results_dir, 'adapt_gen_model.pth')
    metadata_path = os.path.join(base_dir, 'sample_metadata.csv')
    
    # 1. Load the Model 
    from pipeline.gnn_model import AdaptGenNet
    # Input dimension is 3 (according to climate features)
    model = AdaptGenNet(input_dim=3) 
    model.load_state_dict(torch.load(model_path))
    model.eval()

    # 2. Load the Metadata (Where SNPs list is present)
    # We are accepting that this file has 'position' column 
    metadata = pd.read_csv(metadata_path)
    
    # 3. Extract importance from Model Weights 
    # We are accepting weights of first layer as importance of SNPs 
    weights = model.fc1.weight.data.abs().mean(dim=0).numpy()
    
    # 4. Make a Data frame 
    # Here, we assume that the SNPs in the metadata correspond to the model weights.
    snp_df = metadata.copy()
    snp_df['importance'] = weights[:len(snp_df)] # Mapping the weights to the SNPs.
    
    # 5. Filter Top SNPs (Threshold: Importance > Mean)
    threshold = snp_df['importance'].mean()
    top_snps = snp_df[snp_df['importance'] > threshold]
    
    # 6. Save 
    output_path = os.path.join(results_dir, 'top_adaptive_snps.csv')
    top_snps.to_csv(output_path, index=False)
    
    print(f"--- ✅ 'top_adaptive_snps.csv' are generated! ({len(top_snps)} SNPs found) ---")

if __name__ == "__main__":
    generate_top_snps()
