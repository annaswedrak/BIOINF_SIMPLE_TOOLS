

'''pseudocode:
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

'''A straightforward algorithm for finding the most frequent k-mers in a string Text checks all k-mers appearing in this string (there are |Text| − k + 1 such k-mers) and then computes how many times each k-mer appears in Text.'''


def frequent_words(text,k):
     frequent_patterns = []
     count = []
     for i in range(len(text) - k +1):
         pattern = text[i:i+k]

         count.append(text.count(pattern))
     maxcount = max(count)
     for i in range(len(text) - k + 1):
          if count[i] == maxcount:
              if text[i:i+k] not in frequent_patterns:

                  frequent_patterns.append(text[i:i+k])
     return frequent_patterns


dna = 'ACTGACTCCCACCCC'
k = 3



print(frequent_words(dna,k))
