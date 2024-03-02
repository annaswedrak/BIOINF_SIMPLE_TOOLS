'''Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
Input: Strings Pattern and Text along with an integer d.
Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.'''

from hamming_distance import hamming_distance



def approx_substring_positions(s, t, d):
     """
     Find all positions where the substring t appears in the string s with at most d mismatches
     """
     positions = []
     for i in range(len(s) - len(t) + 1):
         if hamming_distance(s[i:i+len(t)],t) <= d:

             positions.append(i)
     return positions
