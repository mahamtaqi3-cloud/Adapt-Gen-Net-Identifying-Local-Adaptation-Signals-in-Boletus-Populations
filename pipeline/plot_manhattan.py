import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_manhattan():
    file_path = os.path.join('results', 'annotated_snps.csv')
    
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} file nahi mili.")
        return

    df = pd.read_csv(file_path)
    
    # Check karein ki data mein 'position' column sahi hai
    if 'position' not in df.columns:
        print("❌ Error: CSV file mein 'position' column nahi hai.")
        return

    plt.figure(figsize=(12, 6))
    
    # Points ko thoda jitter (spread) dein taake wo ek line na dikhein
    plt.scatter(df['position'], df.index, alpha=0.3, c='teal', s=5)
    
    plt.title('Manhattan Plot: SNP Distribution across Genome')
    plt.xlabel('Genomic Position')
    plt.ylabel('SNP Index (Spread)')
    
    output_path = os.path.join('results', 'manhattan_plot.png')
    plt.savefig(output_path)
    print(f"✅ Manhattan plot save ho gaya: {output_path}")
    plt.show()

if __name__ == "__main__":
    plot_manhattan()