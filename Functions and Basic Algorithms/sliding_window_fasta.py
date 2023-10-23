# It has the same functions and output format as sliding_window.py but, instead of taking a k-mer size and a string,
#  it takes a k-mer size and a fasta input file.
#  It should run separately for each header, printing the header name on one line, and then each k-mer from that fasta
#  entry followed by a tab, followed by the GC content of that k-mer, rounded to two decimal places.

import sys


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
    string = ''
    with open(fasta_file, "r") as f:
        for line in f:
            if line[0] == ">":
                header = line.strip()
                print(header)
            else:
                string += line.strip()
    kmers = sliding_window(k, string)

    for i in kmers:
        result = gc_content(i)
        print("{}\t{:.2f}".format(i, result))
