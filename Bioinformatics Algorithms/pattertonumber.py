def PatternToNumber(Pattern):#AT
    if not Pattern:
        return 0
    symbol=LastSymbol(Pattern)#T#A
    prefix=Prefix(Pattern)#A#""
    res=4*PatternToNumber(prefix)+SymbolToNumber(symbol)
    return res#
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
result=PatternToNumber("TT")
print(result)