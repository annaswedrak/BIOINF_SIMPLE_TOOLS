'''A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.
Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.'''

import reverse_complement

def is_reverse_palidrome(seq):
    '''function checks if a seq is reverse palindrome'''
    if reverse_complement.reverse_complement(seq) == seq:
        return True

#print(is_reverse_palidrome("GCATGC"))
dna = "TCAATGCATGCGGGTCTATATGCAT"
positions_and_length = {}
for length in range(12,3,-1):
    for start in range(len(dna)-length+1):
        subseq = dna[start:start+length]

        if is_reverse_palidrome(subseq):
            position_and_length[start+1] = length

print(position_and_length)
