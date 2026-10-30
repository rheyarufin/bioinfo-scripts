dna = "AGCAGCCTGCAATCCTTCGGTCTGAGTTCGAGTGGCCGCAGCGATTCGGCAGGTTGTCGTTATGATCGGATGCTGGACCCAACTGAAGAGCCGGGCCATTACAATTCTTGCTTGGGCTACCGCCAGCGCATGTTGAGCTTATACGTTTTCGTGGCGGCCACGGCTTCGCTTCAACGAATGCGATGTGACTGACCGGACCATTTCATCGCTTCAACGATTGTTTTCAATAGCTGAAGCTAATGATGTGAGCTGGCAGGCTTGCTCGCTTGGAACGTGACTCTGGTTCCCGGTGATTTGTAACTGCGAACGTACAAAAGCTTTTCATAGACAAGATCCTAGCCTGGGCCGTAGCTCCTATTATGTGACTCTTCTACAGAACGTTCATGTCACTTACGAAA"
substring = "ACGTTTT"
d=3
def approximate_pattern_count(text, pattern, d):
 count = 0 
 total_seq=[]
 for i in range(0,(len(text)-len(pattern)+1)):
    seq=text[i:i+len(pattern)]
    for x,y in zip(seq,pattern):
      if(x!=y):
       count = count+1
    if(count<=d):
        total_seq.append(seq)
    count=0
 return total_seq
result=approximate_pattern_count(dna,substring,d)
print(" ".join(result))
print(len(result))