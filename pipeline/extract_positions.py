import pandas as pd
import os

def extract_positions():
    vcf_path = os.path.join('data', 'final_combined_output.vcf')
    output_path = os.path.join('results', 'snp_positions.csv')

    print("--- 🔍 VCF file se positions extract ho rahi hain... ---")

    # VCF file mein comments wali lines '#' se start hoti hain, unhein skip karna zaroori hai
    # 'names' define karna zaroori hai kyunki VCF header aksar complex hota hai
    try:
        df = pd.read_csv(vcf_path, sep='\t', comment='#', header=None)
        # VCF format mein pehla column 'CHROM' aur dusra 'POS' hota hai
        df = df[[0, 1]] 
        df.columns = ['chrom', 'position']
        
        # Result save karein
        df.to_csv(output_path, index=False)
        print(f"--- ✅ Done! Positions '{output_path}' mein save ho gayi hain. ---")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Tip: Check karein agar VCF file mein header lines '#' se shuru ho rahi hain.")

if __name__ == "__main__":
    extract_positions()