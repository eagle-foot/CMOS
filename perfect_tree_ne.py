#! /usr/bin/env python
#coding:UTF-8

__version__ = '1.0'
__date__ = '2016/12/04'
__author__ = 'Takashi Hanasaka'
'''
make gate tree
    '''


import pyfits
import numpy as np
from ROOT import gROOT,TTree,TFile,AddressOf
import sys

f = TFile( '20161202_gate.root', 'recreate' )
tr = TTree( 'tree_ne', 'tree' )

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
        Xray_PH = 0
        count = 0
        if tree.PH17 > 9.279 and tree.PH18 > 9.279 and tree.PH19 > 9.279 and tree.PH24 > 9.279 \
        and tree.PH25 > 9.279 and tree.PH26 > 9.279 and tree.PH31 > 9.279 and tree.PH32 > 9.279 and tree.PH33 > 9.279 :
            array_PH = np.array([tree.PH1,tree.PH2,tree.PH3,tree.PH4,tree.PH5,tree.PH6,tree.PH7,tree.PH8,tree.PH9,tree.PH10,tree.PH11,tree.PH12,tree.PH13,tree.PH14,tree.PH15,tree.PH16,tree.PH17,tree.PH18,tree.PH19,tree.PH20,tree.PH21,tree.PH22,tree.PH23,tree.PH24,tree.PH25,tree.PH26,tree.PH27,tree.PH28,tree.PH29,tree.PH30,tree.PH31,tree.PH32,tree.PH33,tree.PH34,tree.PH35,tree.PH36,tree.PH37,tree.PH38,tree.PH39,tree.PH40,tree.PH41,tree.PH42,tree.PH43,tree.PH44,tree.PH45,tree.PH46,tree.PH47,tree.PH48,tree.PH49])
            for i in range(49) :
                if array_PH[i] > 9.279 :
                    Xray_PH += array_PH[i]
                    count += 1
            print 'count = %s' %count
            my.Arg = tree.Arg
            my.Frame = tree.Frame
            my.Event_th = tree.Event_th
            my.Split_th = 9.279
            my.X = tree.X
            my.Y = tree.Y
            my.Xray = Xray_PH
            my.count = count
            tr.Fill()
        array_PH = np.array([])

f.Write()
f.Close()
