store = [ ]
segments=[ ]
dna = "ACTGACTCCCACCCC"
for i in range(0,(len(dna)-2)):
    store = (dna[i:i+3])
    segments.append(store)
print(segments)