def NumberToPattern(index,k):
    if k==1:
         return NumberToSymbol(index)#
    prefixIndex=index//4#3
    r=index%4#1
    symbol=NumberToSymbol(r)#C
    return NumberToPattern(prefixIndex, k - 1) + symbol
def NumberToSymbol(no):
    sym={0:'A',1:'C',2:'G',3:'T'}
    res=sym[no]
    return res
result=NumberToPattern(13,2)
print(result)