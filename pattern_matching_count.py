'''Pattern Matching Problem: Find all occurrences of a pattern in a string.

Input: Strings Pattern and Genome.
Output: All starting positions in Genome where Pattern appears as a substring.'''

def find_substring_positions(s, t):
     """
     Find all positions where the substring t appears in the string s.
     """
     positions = []
     for i in range(len(s) - len(t) + 1):
         if s[i:i+len(t)] == t:

             positions.append(str(i))
     return " ".join(positions)
