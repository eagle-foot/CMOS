#! /usr/bin/env python
#coding:UTF-8

__version__ = '1.0'
__date__ = '2016/12/09'
__author__ = 'Takashi Hanasaka'

"""

  """

import pyfits
import numpy as np
from ROOT import gROOT,TH1F,TCanvas,TF1,TFile,TTree,TH2F
import sys




argvs = sys.argv
root = TFile(argvs[-1])


array_X = np.array([])
array_Y = np.array([])
array_Xray = np.array([])


tree = root.Get('tree_single3')
entry = tree.GetEntries()
for j in range(entry) :
    tree.GetEntry(j)
    print 'entry = %s' %j
    if tree.Xray >= 2000 :
        array_X = np.append(array_X, tree.X)
        array_Y = np.append(array_Y, tree.Y)
        array_Xray = np.append(array_Xray, tree.Xray)
array = np.array()
