# Adapt-Gen-Net: Identifying Local Adaptation Signals in *Boletus Edulis* Populations

## 📖 Project Overview

**Adapt-Gen-Net** is an end-to-end bioinformatics pipeline designed to detect signatures of local adaptation in *Boletus Edulis* populations. By integrating large-scale genomic variation data (SNPs) with high-resolution climatic variables, this pipeline employs Graph Neural Network (GNN) architectures to identify candidate genomic regions undergoing selection.

This project bridges the gap between environmental stressors and genomic evolution, providing a scalable framework for evolutionary biologists to prioritize candidate genes for downstream functional validation.

## 🔬 Scientific Workflow

The pipeline is structured into five modular stages to ensure transparency and reproducibility:

1. **Data Curation & Preprocessing:** Standardization of genomic metadata and cleaning of raw SNP datasets.
2. **Environmental Correlation:** Integration of climatic features (temperature/precipitation) to quantify environmental selection pressure.
3. **Functional Annotation:** Mapping SNPs to reference genomes to differentiate between **protein-coding** and **regulatory Intergenic regions**.
4. **Adaptive Modeling:** Deployment of GNNs to model genotype-environment associations, isolating variants that drive local adaptation.
5. **Statistical Validation:** Visualization and prioritization of genomic "hotspots" using Manhattan plots and gene frequency analysis.

## 🛠 Technical Stack

* **Modeling:** Graph Neural Networks (GNNs) for high-dimensional feature learning.
* **Core Libraries:** `pandas` (Data manipulation), `matplotlib` (Genomic visualization), `scikit-learn` (Modeling), `torch` (Deep Learning).
* **Environment:** Designed for modularity, allowing easy integration with standard bioinformatics file formats (GFF/GBFF).

## 📊 Key Results & Insights

* **Local Adaptation Mapping:** Identified clusters of SNPs within non-coding regulatory regions, suggesting potential enhancer-mediated adaptive responses in *Boletus Edulis* populations.
* **Visualization:** Custom Manhattan plots identify selection sweeps across the genome, facilitating the rapid identification of high-priority candidate genes.

## 🚀 Getting Started

To replicate the analysis or explore the pipeline architecture:

```bash
# Clone the repository
git clone [https://github.com/mahamtaqi3-cloud/Adapt-Gen-Net-Identifying-Local-Adaptation-Signals-in-Boletus-Populations.git](https://github.com/mahamtaqi3-cloud/Adapt-Gen-Net-Identifying-Local-Adaptation-Signals-in-Boletus-Populations.git)

# Install dependencies
pip install -r requirements.txt

# Run the analysis pipeline
python -m pipeline.summarize_findings
python -m pipeline.plot_manhattan

