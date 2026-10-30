from Bio.Seq import Seq

# Create a sequence object
my_dna = Seq("AGTACACTGGT")

print(f"DNA Sequence: {my_dna}")
print(f"Complement:   {my_dna.complement()}")
print(f"Reverse Comp: {my_dna.reverse_complement()}")