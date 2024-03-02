'''How many different 9-mers form (500,3)-clumps in the E. coli genome? (In other words, do not count a 9-mer more than once.)'''
from frequent_words import FrequencyTable



def FindClumps(text, k, L, t):
    patterns = set()
    for i in range(len(text)-L):
        window = text[i:i+L]
        freqMap = FrequencyTable(window,k)
        for s in freqMap:
            if freqMap[s] >= t:
                patterns.add(s)
    return len(patterns)
