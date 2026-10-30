def ComputingFrequencies(Text,k):#ATTGCCTCGG length=10, k=2
    FrequencyArray=[0]*(4**k)
    for i in range(0,(len(Text)-k)+1):#will loop over 0-8 times
        Pattern=Text[i:i+k]#AT
        j=PatternToNumber(Pattern)#3rd position
        FrequencyArray[j]=FrequencyArray[j]+1
    return FrequencyArray
def FasterFrequentWords(Text,k):
    FrequentPatterns=set()
    FrequencyArray=ComputingFrequencies(Text,k)
    maxarray=max(FrequencyArray)
    for i in range(0,(4**k)):
        if FrequencyArray[i]==maxarray:
            Pattern=NumberToPattern(i,k)
            FrequentPatterns.add(Pattern)
    return FrequentPatterns
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
result=FasterFrequentWords("ACACGTCAGT",2)
print(result)



