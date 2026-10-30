dna = "CATTCCAGTACTTCATGATGGCGTGAAGA"
skew=[0]
for i in range(0,len(dna)):
    if(dna[i]=='C'):
        skew.append(skew[-1]-1)
    elif(dna[i]=='G'):
        skew.append(skew[-1]+1)
    else:
        skew.append(skew[-1])
print(skew)
