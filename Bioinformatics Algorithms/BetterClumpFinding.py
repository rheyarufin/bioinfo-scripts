def BetterClumpFinding(Genome,k,t,L):#AAGCAAAGGTGGGC,2,2,13
    FrequentPatterns=set()
    Clump=[0]*(4**k)
    Text=Genome[0:0+L]#AAGCAAAGGTGGGG
    FrequencyArray=ComputingFrequencies(Text,k)
    for i in range(0,(4**k)):#(0,16),15 iterations
       if(FrequencyArray[i]>=t):
           Clump[i]=1
    for i in range(1,(len(Genome)-L+1)):#14-13+1=2 iterations
        FirstPattern=Genome[i-1:(i-1)+k]#[0:2]=AA
        index=PatternToNumber(FirstPattern)#0
        FrequencyArray[index]=FrequencyArray[index]-1
        LastPattern=Genome[i+L-k:i+L-k+k]#[1+13-2:1+13-2+2]=[12:14]=GC
        index=PatternToNumber(LastPattern)
        FrequencyArray[index]=FrequencyArray[index]+1
        if FrequencyArray[index]>=t:
            Clump[index]=1
    for i in range(0,(4**k)):
        if Clump[i]==1:
            Pattern=NumberToPattern(i,k)
            FrequentPatterns.add(Pattern)
    return FrequentPatterns
def ComputingFrequencies(Text,k):#ATTGCCTCGG length=10, k=2
    FrequencyArray=[0]*(4**k)
    for i in range(0,(len(Text)-k)+1):#will loop over 0-8 times
        Pattern=Text[i:i+k]#AT
        j=PatternToNumber(Pattern)#3rd position
        FrequencyArray[j]=FrequencyArray[j]+1
    return FrequencyArray
def PatternToNumber(Pattern):#AT
    if not Pattern:
        return 0
    symbol=LastSymbol(Pattern)#T#A
    prefix=Prefix(Pattern)#A#""
    return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)#
def SymbolToNumber(LastChar):
    sym={'A':0,'C':1,'G':2,'T':3}
    for base in LastChar:
        code=sym[base]
    return code
def LastSymbol(Pattern):
    l=Pattern[len(Pattern)-1]
    return l
def Prefix(Pattern):
    p=Pattern[:len(Pattern)-1]
    return p
def NumberToPattern(index,k):
    if k==1:
         return NumberToSymbol(index)
    prefixIndex=index//4
    r=index%4
    symbol=NumberToSymbol(r)
    PrefixPattern=NumberToPattern(prefixIndex,k-1)
    return NumberToPattern(prefixIndex, k - 1) + symbol
def NumberToSymbol(no):
    sym={0:'A',1:'C',2:'G',3:'T'}
    res=sym[no]
    return res
result=BetterClumpFinding("AAGCAAAGGTGGGC",2,2,13)
print(result)