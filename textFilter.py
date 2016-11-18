import document
import sentence

class TextFilter:
    def __init__(self,aDocument,aList):
        self.filtList=aList
        self.document=aDocument
        self.sentence=self.document._Document__sentence

    def normSpace(self):
        for s in range(len(self.sentence)):
            aList=self.sentence[s].sentence.split()
            newS=''
            for i in aList:
                newS+=i+' '
            
            self.sentence[s].sentence=newS[:-1]
            

    def normCase(self):
        for s in range(len(self.sentence)):
            self.sentence[s].sentence=self.sentence[s].sentence.lower()
            

    def deleteNull(self):
        for s in range(len(self.sentence)):
            #97,122 65,90 48,58
            sen=self.sentence[s].sentence
            newSen=''
            for i in range(len(sen)):
                if ord(sen[i]) in range(97,123) or ord(sen[i]) in range(65,91) or ord(sen[i]) in range(48,58) or ord(sen[i]) == 32:
                   newSen+=sen[i]
            self.sentence[s].sentence=newSen

    def stripNum(self):
        for s in range(len(self.sentence)):
            sen=self.sentence[s].sentence
            newSen=''
            for i in sen:
                #print(i,ord(i))
                if ord(i) not in range(48,58):
                    newSen+=i
            self.sentence[s].sentence=newSen

    def stripFile(self):
        '''
        Should be used after deleteNull and no need to strip space any more!
        '''
        file = open('filterwords.txt')
        text = file.read()
        wordList = text.split()
        for i in range(len(self.sentence)):
            sen = self.sentence[i].sentence
            words = sen.split()
            sen = ' '.join([ x for x in words if x not in wordList])
                

    
    def apply(self):
        for s in self.filtList:
            if s=='normSpace':
                self.normSpace()
                #print('1')
            elif s=='normCase':
                self.normCase()
                #print('2')
            elif s=='deleteNull':
                self.deleteNull()
                #print('3')
            elif s=='stripNum':
                self.stripNum()
                #print('4')
        return self.document
    
def main():
    filename='1.txt'
    a=document.Document(filename)
    a.generateWhole()
    #b=TextFilter(a,['normSpace','normCase','deleteNull','stripNum'])
    b=TextFilter(a,['stripFile'])
    b.apply()
    
    for i in a._Document__sentence:
        
        print(i.sentence)

  
main()
