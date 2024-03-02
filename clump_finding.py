'''Clump Finding Problem: Find patterns forming clumps in a string.
     Input: A string Genome, and integers k, L, and t.
     Output: All distinct k-mers forming (L, t)-clumps in Genome.'''

#k - length of a pattern
#L - "window" where we find patterns
#t - how many times a pattern occurs in a given L
#genome - a given string
'''FindClumps(Text, k, L, t)
    Patterns ← an array of strings of length 0
    n ← |Text|
    for every integer i between 0 and n − L
        Window ← Text(i, L)
        freqMap ← FrequencyTable(Window, k)
        for every key s in freqMap
            if freqMap[s] ≥ t
                append s to Patterns
    remove duplicates from Patterns
    return Patterns'''

from frequent_words import FrequencyTable
def FindClumps(text, k, L, t):
    patterns = set()
    for i in range(len(text)-L):
        window = text[i:i+L]
        freqMap = FrequencyTable(window,k)
        for s in freqMap:
            if freqMap[s] >= t:
                patterns.add(s)
    return " ".join(patterns)
