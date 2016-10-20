class TextFilter:
    def __init__(self,aDocument,aList):
        self.filtList=aList
        self.filename=aDocument.filename
        self.file=open(self.filename, 'r')
        self.data=self.file.read()

    def normSpace(self):
        pass

    def normCase(self):
        pass

    def deleteNull(self):
        pass

    def stripNum(self):
        pass


    def apply():
        if len(self.filtList)==0:
            return
        else:
            s=self.filtList[0]
            if s=='Normalize whitespace':
                normSpace()
            elif s=='Normalize case':
                normCase()
            elif s=='Strip null characters':
                deleteNull()
            elif s=='Strip numbers':
                stripNum()
                
