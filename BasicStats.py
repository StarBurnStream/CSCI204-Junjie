# Name: Junjie Jiang, Jingya Wu
# CSCI 204 02
# Professor. Joshua Booth


class BasicStats:
    def __init__(self):
        pass

    def createFreqMap(self, freqList):
        '''
        Runtime of this method is O(n^2), where n is the length of freqList.
        '''
        freqDict = {}

        for keys in freqList:
            if freqDict.get(keys) == None:
                freqDict[keys] = freqList.count(keys)

        return freqDict

    def topN(self, freqDict, n):
        '''
        Runtime of this method is O(m*n),
        where m is the length of freqDict, and n is n.
        '''

        topDict = {}

        for keys in freqDict:
            if len(topDict) < n:
                topDict[keys] = freqDict[keys]
            else:
                minKey = keys
                isTop = False
                for keys2 in topDict:
                    if freqDict[keys] > topDict[keys2]:
                        isTop = True
                        if freqDict[keys2] < freqDict[minKey]:
                            minKey = keys2
                if isTop:
                    topDict[keys] = freqDict[keys]
                    del topDict[minKey]
        return topDict

#Better way:
