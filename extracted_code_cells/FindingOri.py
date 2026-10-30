dna = "CATTCCAGTACTTCATGATGGCGTGAAGA"
skew=[0]
for i in range(0,len(dna)):
    if(dna[i]=='C'):
        skew.append(skew[-1]-1)
    elif(dna[i]=='G'):
        skew.append(skew[-1]+1)
    else:
        skew.append(skew[-1])
minima=min(skew)
print(minima)
for x in range(0,len(skew)):
    if(skew[x]==minima):
        print(x, end=" ")