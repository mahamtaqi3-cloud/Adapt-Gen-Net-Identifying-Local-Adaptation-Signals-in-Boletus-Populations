import pandas as pd
import os

def summarize():
    # Sahi file path: results folder mein annotated_snps.csv ko dhoondna
    file_path = os.path.join('results', 'annotated_snps.csv')
    
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} file nahi mili.")
        return

    df = pd.read_csv(file_path)
    print("\n--- 📊 Data Summary ---")
    print(df['gene_annotation'].value_counts().head(5))

    # Gene-based SNPs filtering
    genes = df[df['gene_annotation'] != 'Intergenic']
    
    if genes.empty:
        print("\n⚠️ Koi gene-based SNPs nahi mile.")
    else:
        print("\n--- 🏆 Top 10 Adaptive Genes ---")
        print(genes['gene_annotation'].value_counts().head(10))

if __name__ == "__main__":
    summarize()