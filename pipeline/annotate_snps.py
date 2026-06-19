import pandas as pd
import os

def annotate_snps():
    # Paths set karein
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    snp_path = os.path.join(base_dir, 'results', 'snp_positions.csv')
    gff_path = os.path.join(base_dir, 'data', 'genome.gff')
    output_path = os.path.join(base_dir, 'results', 'annotated_snps.csv')

    if not os.path.exists(snp_path) or not os.path.exists(gff_path):
        print("❌ Error: Input files nahi mili. Check karein snp_positions.csv aur genome.gff wahan hain.")
        return

    print("--- 🚀 Loading data for fast annotation... ---")
    snps = pd.read_csv(snp_path)
    # GFF file load karein
    gff = pd.read_csv(gff_path, sep='\t', header=None, names=['seqname','source','feature','start','end','score','strand','frame','attribute'])
    
    # Sirf 'gene' features lein
    genes = gff[gff['feature'] == 'gene'].copy()
    
    # Numeric conversion (Error handling ke liye)
    genes['start'] = pd.to_numeric(genes['start'], errors='coerce')
    genes['end'] = pd.to_numeric(genes['end'], errors='coerce')
    genes = genes.dropna(subset=['start', 'end'])
    
    # IntervalIndex banayein (Fast Search)
    intervals = pd.IntervalIndex.from_arrays(genes['start'], genes['end'], closed='both')
    
    def fast_find(pos):
        # Position check karein
        try:
            # get_loc se index dhoondein
            idx = intervals.get_loc(pos)
            if isinstance(idx, int):
                return genes.iloc[idx]['attribute']
            return "Intergenic"
        except:
            return "Intergenic"

    print("--- ⚡ Mapping SNPs to Genes (Fast Mode)... ---")
    snps['gene_annotation'] = snps['position'].apply(fast_find)
    
    # Save karein
    snps.to_csv(output_path, index=False)
    print(f"--- ✅ Done! Results saved at: {output_path} ---")

if __name__ == "__main__":
    annotate_snps()