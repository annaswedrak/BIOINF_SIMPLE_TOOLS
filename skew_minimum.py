'''Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.
Input: A DNA string Genome.
Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
Code Challenge: Solve the Minimum Skew Problem'''

from skew import skew_list

def minimum_skew(genome):
    '''Find a position in a genome where the skew diagram attains a minimum'''
    skews = skew_list(genome)
    min_skew = min(skews)
    min_position = []
    for i in range(len(skews)):
        if skews[i] == min_skew:
            min_position.append(i)
    return min_position
