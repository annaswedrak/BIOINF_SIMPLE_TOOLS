'''Function that computes occurences of a pattern(short fragment) in a larger text(long fragment) '''

def counting_pattern(pattern,text):
    count = 0
    for start in range(len(text) - len(pattern) +1):
        if text[start:start+len(pattern)] == pattern:
            count += 1
    return count





#examples of use
gene = "ACAACTATGCATACTATCGGGAACTATCCT"
motif = "ACTAT"
#finding number of motif occurences in gene
print(counting_pattern(motif, gene))
