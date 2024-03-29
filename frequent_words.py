
'''A straightforward algorithm for finding the most frequent k-mers in a string Text checks all k-mers appearing in this string (there are |Text| − k + 1 such k-mers) and then computes how many times each k-mer appears in Text.'''
'''
1 approach:
 FrequentWords(Text, k)
    FrequentPatterns ← an empty set
    for i ← 0 to |Text| − k
        Pattern ← the k-mer Text(i, k)
        Count(i) ← PatternCount(Text, Pattern)
    maxCount ← maximum value in array Count
    for i ← 0 to |Text| − k
        if Count(i) = maxCount
            add Text(i, k) to FrequentPatterns
    remove duplicates from FrequentPatterns
    return FrequentPatterns'''


def frequent_words(text,k):
     frequent_patterns = set()
     counts = []
     patterns = []
     for i in range(len(text) - k + 1):

         pattern = text[i:i+k]
         patterns.append(pattern) #gaining all of the patterns in a list
         counts.append(patterns.count(pattern)) #counting frequency of each pattern

     for i in range(len(text)- k + 1):

         if counts[i] == max(counts): #checking if element from a list is equal to maximum frequency of a pettern
             frequent_patterns.add(text[i:i+k]) #adding the most frequent patterns to a set

     return frequent_patterns




'''
2 approach:
Given a map dict, we can access the value associated with a key key using the notation dict[key]. In the case of a frequency table called freq, we can access the value associated with some key string pattern using the notation freq[pattern]. The following pseudocode function takes a string text and an integer k as input and returns their frequency table as a map of string keys to integer values.'''

'''FrequencyTable(Text, k)
    freqMap ← empty map
    n ← |Text|
    for i ← 0 to n − k
        Pattern ← Text(i, k)
        if freqMap[Pattern] doesn't exist
            freqMap[Pattern]← 1
        else
           freqMap[pattern] ←freqMap[pattern]+1
    return freqMap'''


def FrequencyTable(text,k):
    freqMap = {}
    for i in range(len(text) - k +1):
        pattern = text[i:i+k]
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] += 1
    return freqMap




''' a function MaxMap that takes a map of strings to integers as an input and returns the maximum value of this map as output.'''

def MaxMap(map):
    return max(map.values())


'''BetterFrequentWords(Text, k)
    FrequentPatterns ← an array of strings of length 0
    freqMap ← FrequencyTable(Text, k)
    max ← MaxMap(freqMap)
    for all strings Pattern in freqMap
        if freqMap[pattern] = max
            append Pattern to frequentPatterns
    return frequentPatterns '''


def BetterFrequentWords(text,k):
    FrequentPatterns = []
    freqMap = FrequencyTable(text,k)
    max = MaxMap(freqMap)
    for pattern in freqMap:
        if freqMap[pattern] == max:
            FrequentPatterns.append(pattern)
    return FrequentPatterns

#example from course:
gene = 'GGGCTTCCGTGGCGAGTCGACCTGGCTGTTCTGTAATTCTGTCTTTCTGTCTGGGCTTCCGTGGGCTTCCGTTTCTGTCTGGGCTTCCGTTTCTGTCTTTCTGTAATTCTGTAATTCTGTAATTCTGTCTTTCTGTCTGGCGAGTCGGCGAGTCTTCTGTAATTCTGTCTGACCTGGCTGGGGCTTCCGTTTCTGTAAGGCGAGTCGACCTGGCTGGACCTGGCTGGGGCTTCCGTGACCTGGCTGTTCTGTAAGGCGAGTCTTCTGTCTGGCGAGTCGACCTGGCTGGGCGAGTCTTCTGTCTGACCTGGCTGTTCTGTAAGGCGAGTCGGGCTTCCGTTTCTGTCTTTCTGTAAGGCGAGTCGGCGAGTCGACCTGGCTGGACCTGGCTGGGGCTTCCGTGACCTGGCTGGGCGAGTCGGCGAGTCTTCTGTCTGGGCTTCCGTGGGCTTCCGTTTCTGTCTTTCTGTAAGACCTGGCTGTTCTGTCTTTCTGTAAGACCTGGCTGTTCTGTCTTTCTGTCTGACCTGGCTGTTCTGTCTGGCGAGTCGGCGAGTCTTCTGTCTTTCTGTCTGGGCTTCCGTTTCTGTAAGGCGAGTCGACCTGGCTGTTCTGTAAGACCTGGCTGTTCTGTAATTCTGTCTGGCGAGTCTTCTGTCTTTCTGTAATTCTGTAAGGGCTTCCGTGACCTGGCTGTTCTGTCTTTCTGTCTGGCGAGTCGACCTGGCTGGACCTGGCTGTTCTGTCTGACCTGGCTGTTCTGTCTGGGCTTCCGTTTCTGTAAGGCGAGTCTTCTGTCTTTCTGTCTGACCTGGCTGGGCGAGTCTTCTGTAAGACCTGGCTGGGGCTTCCGTGGGCTTCCGTGGCGAGTCGGGCTTCCGTGGCGAGTCGGCGAGTCGGGCTTCCGT'

kmer= 13
fr = BetterFrequentWords(gene,kmer)
print(" ".join(fr))
