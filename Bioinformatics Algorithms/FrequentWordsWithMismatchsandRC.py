dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
kk=4
dd=1
def FrequentWordsWithMismatchesAndRC(text, k, d):
    freqMap = {}
    n = len(text)

    for i in range(0, n - k + 1):
        pattern = text[i:i+k]
        neighbourhood = Neighbours(pattern, d)

        for neighbor in neighbourhood:
            rc = ReverseComplement(neighbor)

            if neighbor not in freqMap:
                freqMap[neighbor] = 0

            freqMap[neighbor] += 1

            # also count reverse complement
            if rc not in freqMap:
                freqMap[rc] = 0

            freqMap[rc] += 1

    m = max(freqMap.values())

    patterns = []
    for p in freqMap:
        if freqMap[p] == m:
            patterns.append(p)

    return patterns
print(FrequentWordsWithMismatchesAndRC(dna,kk,dd))