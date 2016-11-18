from sLink import *
import random

'''
def fixDown(wlist, hlist, i):
    if i * 2 >= len(hlist):
        return wlist,hlist

    if i * 2 + 1 == len(hlist) or hlist[i*2] >= hlist[i*2+1]:
        if hlist[i*2] > hlist[i]:
            value = hlist[i]
            string = wlist[i]
            hlist[i] = hlist[i*2]
            wlist[i] = wlist[i*2]
            hlist[i*2] = value
            wlist[i*2] = string
            return fixDown(wlist,hlist, i*2)
        else:
            return wlist,hlist

    elif hlist[i*2] < hlist[i*2+1]:
        if hlist[i*2+1] > hlist[i]:
            value = hlist[i]
            hlist[i] = hlist[i*2+1]
            hlist[i*2+1] = value
            string = wlist[i]
            wlist[i] = wlist[i*2+1]
            wlist[i*2+1] = string
            return fixDown(wlist,hlist, i*2+1)
        else:
            return wlist,hlist
'''

def parent(index):
    if index <= 1:
        return -1
    else:
        return index // 2

def leftChild(index):
    return 2 * index

def rightChild(index):
    return 2 * index + 1

def fixDown(wlist, hlist, i):
    if leftChild(i) >= len(wlist):        
        return wlist,hlist

    if leftChild(i) < len(wlist) and hlist[leftChild(i)] > hlist[i]:
        value = hlist[i]
        hlist[i] = hlist[leftChild(i)]
        hlist[leftChild(i)] = value
        string = wlist[i]
        wlist[i] = wlist[leftChild(i)]
        wlist[leftChild(i)] = string
        #print(wlist,hlist)

    if rightChild(i) >= len(wlist):
        return wlist, hlist
    
    if rightChild(i) < len(wlist) and hlist[rightChild(i)] > hlist[i]:
        value = hlist[i]
        hlist[i] = hlist[rightChild(i)]
        hlist[rightChild(i)] = value
        string = wlist[i]
        wlist[i] = wlist[rightChild(i)]
        wlist[rightChild(i)] = string
        #print(wlist,hlist)
    return wlist,hlist

def heapRemove(wlist, hlist):
    if 1 == len(hlist) - 1:
        hlist.pop()
        wlist.pop()
        return wlist,hlist
    print(wlist,hlist)
    hlist[1] = hlist.pop()
    wlist[1] = wlist.pop()
    for i in range(len(wlist)-1,0,-1):
        print(wlist,hlist)
        wlist, hlist = fixDown(wlist,hlist, i)
    return wlist,hlist

class BasicStats:
    """
    This class performs basic statistical analysis to the input list/dictionary.
    """
    def __init__(self):
        pass

    def slinkFreq(self, freqList):
        """
        This method takes in a list of words and returns a head of a linked list,
        whose data is a list of information, with the first one the word and the
        second one the number of that word.
        """
        '''
        Runtime of this method is O(n^2), where n is the length of freqList.
        '''
        freqDict = {}

        for keys in freqList:
            if freqDict.get(keys) == None:
                freqDict[keys] = freqList.count(keys)
        aSLink=SLink()
        for keys in freqDict:
            aSLink.add(keys)
        node=aSLink.head
        while node!=None:
            node.data.append(freqDict[node.data[0]])
            node=node.next
        
        return aSLink.head
    
    def createFreqMap(self, freqList):
        """
        This method takes in a list of words and returns a dictionary, whose
        keys are the unique words and values are the frequency of keys.
        """
        '''
        Runtime of this method is O(n^2), where n is the length of freqList.
        '''
        freqDict = {}

        for keys in freqList:
            if freqDict.get(keys) == None:
                freqDict[keys] = freqList.count(keys)

        return freqDict

    def topN(self, freqDict, n):
        """
        This method takes in a dictionary of word frequencies and returns another
        dictionary with the top n words and their frequencies.
        """
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

    def LLTopN(self,head,n):
        node=head
        aSlink=SLink()
        for i in range(n):
            aSlink.add(node.data[0])
            aSlink.head.data.append(node.data[1])
            node=node.next
        while node!=None:
            sNode=aSlink.head
            state=False
            while sNode!=None and state==False:
                if node.data[1]>sNode.data[1]:
                    aSlink.remove(sNode.data[0])
                    aSlink.add(node.data[0])
                    aSlink.head.data.append(sNode.data[1])
                    state=True
                else:
                    sNode=sNode.next
            node=node.next
        return aSlink.head

    def bottomN(self, freqDict, n):
        """
        This method takes in a dictionary of word frequencies and returns another
        dictionary with the bottom n words and their frequencies.
        """
        '''
        Runtime of this method is O(m*n),
        where m is the length of freqDict, and n is n.
        '''
        bottomDict = {}

        for keys in freqDict:
            if len(bottomDict) < n:
                bottomDict[keys] = freqDict[keys]
            else:
                maxKey = keys
                isBottom = False
                for keys2 in bottomDict:
                    if freqDict[keys] < bottomDict[keys2]:
                        isBottom = True
                        if freqDict[keys2] > freqDict[maxKey]:
                            maxKey = keys2
                if isBottom:
                    bottomDict[keys] = freqDict[keys]
                    del bottomDict[maxKey]
        return bottomDict




    def topNHeap(self, wordlist, n,):
        hlist = [0]
        wlist = [0]
        topNHlist = []
        topNWlist = []
        for word in wordlist:
            try:
                index = wlist.index(word)
                hlist[index] += 1
            except ValueError:
                wlist.append(word)
                hlist.append(1)
        for i in range(len(wlist)-1,0,-1):
            wlist, hlist = fixDown(wlist,hlist, i)
        for i in range(n):
            topNHlist.append(hlist[1])
            topNWlist.append(wlist[1])
            wlist,hlist = heapRemove(wlist,hlist)
        return topNWlist,topNHlist
            


    

    def bottomNHeap(self,heapList):
        pass




def main():
    wordList = []
    words = ['happy','sad','angry','blue','anxious']
    for i in range(10):
        word = random.choice(words)
        wordList.append(word)
    print(wordList)
    a = BasicStats()
    aList,bList = a.topNHeap(wordList,3)
    print(aList,bList)
main()




















    

"""
Better way to do both at the same time:
    I am thinking about do both comparasons at the same time, meaning that when
    looping through the elements of the dictionary, check if it is greater than
    the smallest element of the topN dictionary or smaller than the largest element
    of the bottomN dictionary. I haven't tried this out so am still not sure if
    this will produce a smaller runtime.
"""
