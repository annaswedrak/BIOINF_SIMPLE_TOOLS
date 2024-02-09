from nucleotides_count import counting_nucleotides


with open("vibrio_cholerae_ori.txt", "r") as file:
    for line in file:
        line = line.strip()
        genome = ""
        genome += line


a,c,g,t = counting_nucleotides(genome)

print(a,c,g,t)
print(f"Number of A: {a},\n number of C: {c},\n number of G {g},\n number of T: {t}")
