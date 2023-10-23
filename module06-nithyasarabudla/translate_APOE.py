#!/usr/bin/env python
from Bio.Seq import Seq
from Bio import SeqIO

# Open input and output files
input_file = "APOE_refseq_transcript.fasta"
output_file = "apoe_aa.fasta"
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    # Loop over each sequence in the input file
    for record in SeqIO.parse(infile, "fasta"):
        # Translate the RNA sequence to amino acids
        rna_seq = Seq(str(record.seq))
        amino_acid_seq = rna_seq.translate()

        # Write the translated sequence to the output file with the same header
        header = record.description
        outfile.write(">" + header + "\n")
        outfile.write(str(amino_acid_seq) + "\n")

