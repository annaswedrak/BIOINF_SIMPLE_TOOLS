'''A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".
Given: A collection of k(k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)'''


from reading_multiple_gene_fasta import read_fasta

def longest_common_substring(fasta_file):
        genes = read_fasta(fasta_file) #extracting genes to dictionary
        sequences = list(genes.values()) #list of sequences
        def is_common(sequences, subsequence):
            '''function that checks if a given subsequence is common for collection of sequences'''
            for seq in sequences:
                if subsequence not in seq:
                    return False
                else:
                    continue
            return True

        shortest = min(sequences, key=len)
        for length in range(len(shortest),0,-1):
            for start in range(len(shortest) - length + 1):
                substring = shortest[start:start+length]
                if is_common(sequences,substring):
                    return substring
        return ""













print(longest_common_substring('genes_sample.fasta'))
