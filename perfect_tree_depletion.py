#! /usr/bin/env python
#coding:UTF-8

__version__ = '1.0'
__date__ = '2016/12/04'
__author__ = 'Takashi Hanasaka'


'''
make depletion event tree
    '''

import pyfits
import numpy as np
from ROOT import gROOT,TTree,TFile,AddressOf
import sys

f = TFile( '20161202_depletion.root', 'update' )
tr = TTree( 'tree_de_2pixel', 'tree' )

gROOT.ProcessLine(\
"struct MyStruct {\
   Int_t    Arg;\
   Int_t    Frame;\
   Int_t    Event_th;\
   Int_t    Split_th;\
   Int_t    X;\
   Int_t    Y;\
   Int_t    Xray;\
   Int_t    count;\
};" );


from ROOT import MyStruct
my = MyStruct()

tr.Branch('Arg', AddressOf(my,'Arg'), 'Arg/I');
tr.Branch('Frame', AddressOf(my,'Frame'), 'Frame/I');
tr.Branch('Event_th', AddressOf(my,'Event_th'), 'Event_th/I');
tr.Branch('Split_th', AddressOf(my,'Split_th'), 'Split_th/I');
tr.Branch('X', AddressOf(my,'X'), 'X/I');
tr.Branch('Y', AddressOf(my,'Y'), 'Y/I');
tr.Branch('Xray', AddressOf(my,'Xray'), 'Xray/I');
tr.Branch('count', AddressOf(my,'count'), 'count/I');


argvs = sys.argv
root = TFile(argvs[-1])

for i in range(1,7) :
    print 'tree = %s' %i
    tree = root.Get('tree%s' %i)
    entry = tree.GetEntries()

    for j in range(entry) :
        tree.GetEntry(j)
        print 'entry = %s' %j

        array_PH = np.array([tree.PH17,tree.PH18,tree.PH19,tree.PH24,tree.PH25,tree.PH26,tree.PH31,tree.PH32,tree.PH33])
        Xray_PH = 0
        count = 0
        if tree.PH9 < 9.5 and tree.PH10 < 9.5 and tree.PH11 < 9.5 and tree.PH12 < 9.5 \
        and tree.PH13 < 9.5 and tree.PH16 < 9.5 and tree.PH20 < 9.5 and tree.PH23 < 9.5 \
        and tree.PH27 < 9.5 and tree.PH30 < 9.5 and tree.PH34 < 9.5 and tree.PH37 < 9.5 \
        and tree.PH38 < 9.5 and tree.PH39 < 9.5 and tree.PH40 < 9.5 and tree.PH41 < 9.5 :

            for i in range(9) :
                if array_PH[i] > 9.5 :
                    Xray_PH += array_PH[i]
                    count += 1
            if count == 2 :
                print "count = %s" %count
                my.Arg = tree.Arg
                my.Frame = tree.Frame
                my.Event_th = tree.Event_th
                my.Split_th = 9.5
                my.X = tree.X
                my.Y = tree.Y
                my.Xray = Xray_PH
                my.count = count
                tr.Fill()

        array_PH = np.array([])


f.Write()
f.Close()
