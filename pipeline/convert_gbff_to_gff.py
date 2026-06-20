from Bio import SeqIO

def convert_gbff_to_gff(input_file, output_file):
    # Convert using BioPython
    with open(output_file, "w") as out_handle:
        for record in SeqIO.parse(input_file, "genbank"):
            for feature in record.features:
                if feature.type == "gene":
                    # Write in GFF format
                    start = feature.location.start + 1
                    end = feature.location.end
                    gene_name = feature.qualifiers.get("gene", ["unknown"])[0]
                    out_handle.write(f"{record.id}\tgenbank\tgene\t{start}\t{end}\t.\t+\t.\tattribute={gene_name}\n")
    print("--- ✅ GBFF to GFF conversion done! ---")

# Run this
convert_gbff_to_gff('data/genomic.gbff', 'data/genome.gff')
