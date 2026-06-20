import pandas as pd
import os

def extract_positions():
    vcf_path = os.path.join('data', 'final_combined_output.vcf')
    output_path = os.path.join('results', 'snp_positions.csv')

    print("--- 🔍 Positions are being extracted from VCF file ... ---")

    # Skip comment lines in VCF file staring with '#' 
    # Defining 'names' is must because VCF header is always complex
    try:
        df = pd.read_csv(vcf_path, sep='\t', comment='#', header=None)
        # First coulumn in VCF format is 'CHROM' and second is 'POS' 
        df = df[[0, 1]] 
        df.columns = ['chrom', 'position']
        
        # Save the Result
        df.to_csv(output_path, index=False)
        print(f"--- ✅ Done! Positions are saved in '{output_path}' ---")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Tip: Check if header in VCF file is starting with '#' ")

if __name__ == "__main__":
    extract_positions()
