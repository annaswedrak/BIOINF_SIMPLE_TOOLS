''' we can compute Skewi+1(Genome) from Skewi(Genome) according to the nucleotide in position i of Genome. If this nucleotide is G, then Skewi+1(Genome) = Skewi(Genome) + 1; if this nucleotide is C, then Skewi+1(Genome)= Skewi(Genome) – 1; otherwise, Skewi+1(Genome) = Skewi(Genome).'''

def skew_list(genome):
    skew = 0
    skew_positions = [0]
    for i in range(len(genome)):
        if genome[i] == "G":
            skew += 1
            skew_positions.append(skew)
        elif genome[i] == "C":
            skew -= 1
            skew_positions.append(skew)
        else:
            skew_positions.append(skew)
    return skew_positions
