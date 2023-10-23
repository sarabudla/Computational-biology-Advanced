# hamming, which takes 2 strings and returns the hamming distance between those strings.
# Then, create an if __name__ == "__main__" block. That block should allow the user to pass two strings. Then,
# it should print the two strings and the hamming distance between them, separated by tabs.
# should match the nucleotides
# string with same length

import sys


def hamming(string1, string2):
    """hamming, which takes 2 strings and returns the hamming distance between those strings."""
    distance = 0
    l = len(string1)
    for i in range(l):
        if string1[i] != string2[i]:
            distance += 1
    return distance


# print(hamming("ATGCAT", "AAGCTT"))

if __name__ == "__main__":
    string1 = sys.argv[1]
    string2 = sys.argv[2]
    distance = hamming(string1, string2)
    print(string1 + "\t" + string2 + "\t" + str(distance))
