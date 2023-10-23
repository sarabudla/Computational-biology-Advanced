# sliding_window which takes 2 arguments, k (a k-mer size) and a string, and returns a list of all k-mers in the given
# string, using the sliding window algorithm.
import sys


def sliding_window(k, string):
    """sliding_window which takes 2 arguments, k (a k-mer size) and a string, and returns a list of all k-mers in the given
string, using the sliding window algorithm."""
    kmer = []
    end = len(string) - k + 1
    for i in range(0, end):
        kmer.append(string[i:i + k])
    return kmer


# gc_content which takes a single string and returns it's GC content (as a fraction between 0 and 1,
# where 0 represents no G or C bases and 1 represents only G and C bases).

def gc_content(string):
    """ Returns [0, 1], the fraction of GCs in the given string"""

    string = string.lower()

    #Count the number of g's and c's
    gc = 0
    for nucleotide in string:
        if nucleotide in ['g', 'c']:
            gc += 1

    return gc / len(string)


# Then, create an if __name__ == "__main__" block. That block should allow for two command line arguments: a k-mer
# size and a string. On each line, it should then print out a k-mer followed by a tab, followed by the GC content of
# that k-mer, rounded to two decimal places.


if __name__ == "__main__":
    k = int(sys.argv[1])
    string = sys.argv[2]
    kmers = sliding_window(k, string)
    for i in kmers:
        result = gc_content(i)
        print("{}\t{:.2f}".format(i, result))
