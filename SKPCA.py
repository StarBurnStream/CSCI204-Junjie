"""This file contains the starting block for PCA in scikit
    You will need to add functions/methods to convert data into needed format,
    See treedemo.py
"""

import pandas as pd
import numpy as np
from sklearn import decomposition

class SKPCA

    def __init__(self):
        self.pca_h = None
        self.ncomp = 0
        self.labels = None
        self.X = None

    def train(self, data, labels, ncomp):
        """Data is a 2d data list.
           Each row in the 2dlist is sample (all samples probably of a word)
           The first column is the label idenity the sample ("A")
           labels are where the sample came frome, such as from JamesJoyce sisters
        """
        self.ncomp = ncomp
        self.labels = labels

        #Strip the first column
        x = [None]*len(data)
        y = [None]*len(data)
        
         for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t


        self.pca_h = decomposition.PCA(ncomp)
        self.pca_h.fit(x)
        self.X = self.pca_h.transform(x)

        
        
