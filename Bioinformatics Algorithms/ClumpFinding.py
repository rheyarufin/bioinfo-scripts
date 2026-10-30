def ClumpFinding(Genome,k,t,L):
    FrequentPatterns=set()
    Clump=[0]*(4**k)
    for i in range(0,len(Genome)-L+1):
        Text=Genome[i:i+L]
        FrequencyArray=ComputingFrequencies(Text,k)
        for index in range(0,4**k):
            if FrequencyArray[index]>=t:
                Clump[index]=1
    for i in range(0,4**k):
        if Clump[i]==1:
            Pattern=NumberToPattern(i,k)
            FrequentPatterns.add(Pattern)
    return FrequentPatterns
def ComputingFrequencies(Text,k):#ATTGCCTCGG length=10, k=2
    FrequencyArray=[0]*(4**k)
    for i in range(0,(len(Text)-k)+1):#will loop over 0-8 times
        Pattern=Text[i:i+k]#AT
        j=PatternToNumber(Pattern)#3rd position alphanumerically
        FrequencyArray[j]=FrequencyArray[j]+1#will add plus 1 in that position
    return FrequencyArray
def PatternToNumber(Pattern):
    if not Pattern:
        return 0
    symbol=LastSymbol(Pattern)
    prefix=Prefix(Pattern)
    return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)
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
         return NumberToSymbol(index)#
    prefixIndex=index//4
    r=index%4
    symbol=NumberToSymbol(r)#C
    return NumberToPattern(prefixIndex, k - 1) + symbol
def NumberToSymbol(no):
    sym={0:'A',1:'C',2:'G',3:'T'}
    res=sym[no]
    return res
result=ClumpFinding("GATCACACACAGGTA",3,3,9)
print(result)
