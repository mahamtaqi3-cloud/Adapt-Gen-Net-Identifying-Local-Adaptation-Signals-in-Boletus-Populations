import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_manhattan():
    file_path = os.path.join('results', 'annotated_snps.csv')
    
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} file nahi mili.")
        return

    df = pd.read_csv(file_path)
    
    # Check whether the 'position' column in the data is correct.
    if 'position' not in df.columns:
        print("❌ Error: CSV file does not contain a 'position' column..")
        return

    plt.figure(figsize=(12, 6))
    
    # Add a slight jitter (spread) to the points so they don't appear in a single line.
    plt.scatter(df['position'], df.index, alpha=0.3, c='teal', s=5)
    
    plt.title('Manhattan Plot: SNP Distribution across Genome')
    plt.xlabel('Genomic Position')
    plt.ylabel('SNP Index (Spread)')
    
    output_path = os.path.join('results', 'manhattan_plot.png')
    plt.savefig(output_path)
    print(f"✅ Manhattan plot has been saved: {output_path}")
    plt.show()

if __name__ == "__main__":
    plot_manhattan()
