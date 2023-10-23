#!/usr/bin/env python
# Biopython_seq

from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
# Creating a SeqRecord object with the following parameters:
# seq: "aaaatgggggggggggccccgtt"
# id: "#12345"
# description: "example 1"
# molecule_type: "generic_dna"
seq = Seq("aaaatgggggggggggccccgtt")
seq_record = SeqRecord(seq, id="#12345", description="example 1", annotations={"molecule_type": "generic_dna"})
# Writing the object to a sequence file in GenBank format (you can call the file BioPython_seq.gb)
SeqIO.write(seq_record, "BioPython_seq.gb", "gb")


