#Hamming distance
dna1="CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT"
dna2="CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"
def NewHammingDistance(p,q):
 count=0
 for i,j in zip(p,q):
    if(i!=j):
        count=count+1
 return count
print(NewHammingDistance(dna1,dna2))