#!/usr/bin/env python3
# BioPython_seqio.py


import sys
from Bio import SeqIO
# takes two arguments from the command line
fasta_file = sys.argv[1]
new_fasta_file = sys.argv[2]
# Reads the file
data_file = SeqIO.parse(fasta_file, 'fasta')
# Outputs a new FASTA file whose contents are the reverse complements of the sequences from the original FASTA file.
rev_comp_seq = []

for seq in data_file:
    rev_comp = seq.reverse_complement()
    rev_comp_seq.append(rev_comp)

SeqIO.write(rev_comp_seq, new_fasta_file, 'fasta')
