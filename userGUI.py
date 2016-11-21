#from tkinter import Tk, Label, Button, Entry, END, W, E
import document, matPlotPloter, basicStats, commandLinePloter
import tkinter


class UserGUI:
    def __init__(self, master):
        self.master = master
        master.title("UserGUI")

        self.introGUI()

    def introGUI(self):
        self.label = tkinter.Label(self.master, text="Number of documents to be analyzed:")
        self.entry = tkinter.Entry(self.master)

        self.label.grid(row=0, column=0)
        self.entry.grid(row=1, column=0)

        self.button = tkinter.Button(self.master, text="Confirm", command=lambda: self.mainGUI(int(self.entry.get())))

        self.button.grid(row=2, column=0)

    def mainGUI(self, num):
        self.label.destroy()
        self.entry.destroy()
        self.button.destroy()

        self.nameLabel = tkinter.Label(self.master, text="Document Names:")
        self.charLabel = tkinter.Label(self.master, text="Characteristics:")
        self.filterLabel = tkinter.Label(self.master, text="Text Filters:")
        self.statLabel = tkinter.Label(self.master, text="Statistical Method:")
        self.trainLabel = tkinter.Label(self.master, text="  For training?  ")
        self.predictLabel = tkinter.Label(self.master, text="  For predicting?  ")
        self.resultLabel = tkinter.Label(self.master, text="  RESULTS:    ")

        self.nameEntry = []
        self.charEntry = []
        self.filterEntry = []
        self.statEntry = []
        self.trainBox = []
        self.predictBox = []

        for i in range(num):
            self.nameEntry.append(tkinter.Entry(self.master))
            self.charEntry.append(tkinter.Entry(self.master))
            self.filterEntry.append(tkinter.Entry(self.master))
            self.statEntry.append(tkinter.Entry(self.master))

            self.trainBox.append(tkinter.Checkbutton(self.master))
            self.predictBox.append(tkinter.Checkbutton(self.master))

            self.nameEntry[i].grid(row=i+1, column=0)
            self.charEntry[i].grid(row=i+1, column=1)
            self.filterEntry[i].grid(row=i+1, column=2)
            self.statEntry[i].grid(row=i+1, column=3)

            self.trainBox[i].grid(row=i+1, column=4)
            self.predictBox[i].grid(row=i+1, column=5)

        self.run_button = tkinter.Button(self.master, text="Run", command=lambda: self.update())

        # LAYOUT

        self.nameLabel.grid(row=0, column=0, sticky=tkinter.W)
        self.charLabel.grid(row=0, column=1, sticky=tkinter.W)
        self.filterLabel.grid(row=0, column=2, sticky=tkinter.W)
        self.statLabel.grid(row=0, column=3, sticky=tkinter.W)
        self.trainLabel.grid(row=0, column=4)
        self.predictLabel.grid(row=0, column=5)
        self.resultLabel.grid(row=0, column=6, sticky=tkinter.W)

        self.run_button.grid(row=num+1, column=0,columnspan=6)


    def update(self):
        filenames = []

        for i in range(len(self.nameEntry)):
            filenames.append(self.nameEntry[i].get())

        doc = document.Document(filename)
        doc.generateWhole()
        doc.getWordCount()

        wordList = doc._Document__wordList

        stats = basicStats.BasicStats()
        top10Dict = stats.topN(stats.createFreqMap(wordList), 10)

        top10Freq = []
        top10Words = []

        print('Top 10 words and their frequencies:')

        for word in top10Dict:
            top10Words.append(word)
            top10Freq.append(top10Dict[word])
            print(word + ':' + str(top10Dict[word]), end = '  ')

        print('\n\n')

        '''
        graph = commandLinePloter.CommandLinePloter()
        graph.twoDBar(top10Freq)
        graph.twoDScatter(top10Freq)
        '''

        #docS = documentStream.DocumentStream(filename)
        #docS.writeWhole(doc)

        print(top10Dict)

        matGraph = matPlotPloter.MatPlotPloter()
        matGraph.twoDScatter(top10Freq)
        matGraph.twoDBarChart(top10Freq)


root = tkinter.Tk()
my_gui = UserGUI(root)
root.mainloop()
