dna = "AGCAGCCTGCAATCCTTCGGTCTGAGTTCGAGTGGCCGCAGCGATTCGGCAGGTTGTCGTTATGATCGGATGCTGGACCCAACTGAAGAGCCGGGCCATTACAATTCTTGCTTGGGCTACCGCCAGCGCATGTTGAGCTTATACGTTTTCGTGGCGGCCACGGCTTCGCTTCAACGAATGCGATGTGACTGACCGGACCATTTCATCGCTTCAACGATTGTTTTCAATAGCTGAAGCTAATGATGTGAGCTGGCAGGCTTGCTCGCTTGGAACGTGACTCTGGTTCCCGGTGATTTGTAACTGCGAACGTACAAAAGCTTTTCATAGACAAGATCCTAGCCTGGGCCGTAGCTCCTATTATGTGACTCTTCTACAGAACGTTCATGTCACTTACGAAA"
substring = "ACGTTTT"
total_seq=[]
d=3
def approximate_pattern_count(text, pattern, d):
 count = 0 
 for i in range(0,(len(dna)-len(substring)+1)):
    seq=dna[i:i+len(substring)]
    for x,y in zip(seq,substring):
      if(x!=y):
       count = count+1
    if(count<=d):
        total_seq.append(seq)
    count=0
 return total_seq
result=approximate_pattern_count(dna,substring,d)
print(" ".join(result))
print(len(result))