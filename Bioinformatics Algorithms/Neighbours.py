def NewHammingDistance(p,q):#Call stack
 count=0
 for i,j in zip(p,q):
    if(i!=j):
        count=count+1
 return count
def Neighbours(pattern, d):
    if d==0:
        return [pattern]
    if len(pattern)==1:
        return['A','C','G','T']
    neighbourhood=[]
    suffix_neighbours=Neighbours(pattern[1:],d)
    for text in suffix_neighbours:
        if NewHammingDistance(pattern[1:],text)<d:
            for x in ['A','C','G','T']:
                neighbourhood.append(x+text)
        else:
            neighbourhood.append(pattern[0]+text)
    return neighbourhood
seq="ATT"
dd=2
print(" ".join(Neighbours(seq,1)))