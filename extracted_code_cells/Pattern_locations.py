genome = "ATGACTTCGCTGTTACGCGC"
pattern = "CGC"
for i in range(0,(len(genome)-len(pattern)+1)):
    if(pattern==genome[i:i+len(pattern)]):
        print(i, end = " ")
