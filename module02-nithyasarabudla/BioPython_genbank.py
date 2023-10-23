#!/usr/bin/env python
# BioPython_genbank.py

from Bio import Entrez
from Bio import SeqIO

Entrez.email = "sarabudla.n@northeastern.edu"

# Retrieve the sequence by gi (id)
with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="515056") as handle1:
    record1 = SeqIO.read(handle1, "gb")

# Retrieve the sequence by accession (id)
with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id="J01673.1") as handle2:
    record2 = SeqIO.read(handle2, "gb")

# Create the list with the two Seq objects
sequence = [record1, record2]

# Print out the sequences from the list
for seq in sequence:
    print(seq.seq)

# Print out the type, location, and strand of each feature
print("Type\t\t"" Location\t\t""Strand")
for seq in sequence:
    for i in seq.features:
        print(i.type, "\t\t", i.location, "\t\t", i.strand)
