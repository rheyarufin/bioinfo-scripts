def FindingFrequentWordsBySorting(Text,k):# AAGCAAAGGTGG ,k=2
    FrequentPatterns=set()
    Count=[0]*(len(Text)-k+1)
    Index=[0]*(len(Text)-k+1)
    for i in range (0,(len(Text)-k+1)):
        Pattern=Text[i:i+k]
        Index[i]=PatternToNumber(Pattern)
        Count[i]=1
    SortedIndex=sorted(Index)
    for i in range (1,len(Text)-k+1):
        if SortedIndex[i]==SortedIndex[i-1]:
            Count[i]=Count[i-1]+1
        else:
            Count[i]=1
    maxCount=max(Count)
    for i in range (0,len(Text)-k+1):
        if(Count[i]==maxCount):
            Pattern=NumberToPattern(SortedIndex[i],k)
            FrequentPatterns.add(Pattern)
    return FrequentPatterns
def PatternToNumber(Pattern):#AT
    if not Pattern:
        return 0
    symbol=LastSymbol(Pattern)#T#A
    prefix=Prefix(Pattern)#A#""
    res=4*PatternToNumber(prefix)+SymbolToNumber(symbol)
    return res#
def SymbolToNumber(LastChar):
    sym={'A':0,'C':1,'G':2,'T':3}
    code=sym[LastChar]
    return code
def LastSymbol(Pattern):
    l=Pattern[-1]
    return l
def Prefix(Pattern):
    p=Pattern[:-1]
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
result=FindingFrequentWordsBySorting("AAGCAAAGGTGG",2)
print(result)