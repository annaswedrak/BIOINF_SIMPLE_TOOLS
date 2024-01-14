
#function that reads fasta file and convert it to id-sequence dictionary
def read_fasta(file_path):
    with open(file_path,"r") as file:
        labels =[]
        sequences=[]
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                labels.append(line)
            else:
                sequences.append(line)
    dna_samples = dict(zip(labels,sequences))
    return dna_samples

#print(read_fasta('sample_data'))
