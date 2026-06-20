import pandas as pd
import os

def summarize():
    # Correct file path: find  annotated_snps.csv in folder
    file_path = os.path.join('results', 'annotated_snps.csv')
    
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} file not found.")
        return

    df = pd.read_csv(file_path)
    print("\n--- 📊 Data Summary ---")
    print(df['gene_annotation'].value_counts().head(5))

    # Gene-based SNPs filtering
    genes = df[df['gene_annotation'] != 'Intergenic']
    
    if genes.empty:
        print("\n⚠️ No gene-based SNPs found.")
    else:
        print("\n--- 🏆 Top Adaptive Genes ---")
        print(genes['gene_annotation'].value_counts().head(10))

if __name__ == "__main__":
    summarize()
