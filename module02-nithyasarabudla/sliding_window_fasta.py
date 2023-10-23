#!/usr/bin/env python
# sliding_window_fasta.py

import sys
from Bio import SeqIO


def sliding_window(k, string):
    """sliding_window which takes 2 arguments, k (a k-mer size) and a string, and returns a list of all k-mers in the given
string, using the sliding window algorithm."""
    kmer = []
    end = len(string) - k + 1
    for i in range(0, end):
        kmer.append(string[i:i + k])
    return kmer


def gc_content(string):
    """ Returns [0, 1], the fraction of GCs in the given string"""

    string = string.lower()

    gc = 0
    for nucleotide in string:
        if nucleotide in ['g', 'c']:
            gc += 1

    return gc / len(string)


if __name__ == "__main__":

    k = int(sys.argv[1])
    fasta_file = sys.argv[2]
    # opening the file with SeqIO
    for sequence in SeqIO.parse(open(fasta_file),"fasta"):
        print(">"+sequence.description)
        string = sequence.seq
        kmers = sliding_window(int(k), string)

        for i in kmers:
            result = gc_content(i)
            print("{}\t{:.2f}".format(i, result))
