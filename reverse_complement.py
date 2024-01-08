'''In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc
 of s'''
complement = {"A":"T","C":"G","G":"C","T":"A"}

def reverse_complement(seq):
    complement_seq = ""
    for nucleotide in seq[::-1]:
        complement_seq += complement[nucleotide]
    return complement_seq

s = "AAAACCCGGT"

print(reverse_complement(s))
