'''Exercise Break: Return a space-separated list of starting positions (in increasing order) where CTTGATCAT appears as a substring in the Vibrio cholerae genome.'''

from pattern_matching_count import find_substring_positions
with open("Vibrio_cholerae.txt", "r") as file:
    genome = ""
    for line in file:
        line = line.strip()
        genome += line
substring = "CTTGATCAT"

print(find_substring_positions(genome,substring))
