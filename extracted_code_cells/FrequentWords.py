segments=[ ]
count = 0
max_count = 0
dna = "ACTGACTCCCACCCC"
for i in range(0,(len(dna)-2)):
    segments.append(dna[i:i+3])
print(segments)
for j in range(0,(len(segments))):
    for z in range(0,(len(dna))):
        if(dna[z:z+3]==segments[j]):
            count = count + 1
            if count>max_count:
              max_count = count
              max_seq = segments[j]
    count = 0
print(max_seq, " has been repeated the maximum of",  max_count)