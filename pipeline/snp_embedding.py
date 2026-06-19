import numpy as np
import pandas as pd
import allel
import os

def extract_snp_matrix(vcf_path, output_npy_path):
    print(f"📖 Loading VCF file from: {vcf_path}...")
    
    if not os.path.exists(vcf_path):
        raise FileNotFoundError(f"VCF file not found at {vcf_path}. Check your path!")

    # Read VCF file using scikit-allel
    vcf_data = allel.read_vcf(vcf_path, fields=['variants/CHROM', 'variants/POS', 'calldata/GT', 'samples'])
    
    if vcf_data is None:
        print("❌ Error: VCF data could not be read. File might be corrupted or empty.")
        return

    samples = vcf_data['samples']
    print(f"✅ Loaded {len(samples)} samples successfully: {list(samples)}")

    # Extract Genotype array
    gt_array = vcf_data['calldata/GT']
    print(f"🧬 Extracted genotype array with shape: {gt_array.shape}")

    print("🔄 Converting genotypes to numerical matrix (0, 1, 2)...")
    geno_array = allel.GenotypeArray(gt_array)
    dosage_matrix = geno_array.to_n_alt() # Converts to alternate allele counts

    # Handle missing data (replace -1 with 0)
    dosage_matrix = np.where(dosage_matrix < 0, 0, dosage_matrix)

    # Transpose for Deep Learning: (num_samples, num_features)
    final_matrix = dosage_matrix.T
    print(f"📊 Final numerical matrix shape for Deep Learning: {final_matrix.shape}")

    # Save the matrix as a numpy binary file
    np.save(output_npy_path, final_matrix)
    print(f"💾 Numerical SNP matrix successfully saved to: {output_npy_path}")
    
    pos = vcf_data['variants/POS']
    print(f"🎯 Total processed polymorphic loci: {len(pos)} variants across chromosomes.")

if __name__ == "__main__":
    VCF_INPUT = "data/final_combined_output.vcf"
    MATRIX_OUTPUT = "data/boletus_snp_matrix.npy"
    
    extract_snp_matrix(VCF_INPUT, MATRIX_OUTPUT)