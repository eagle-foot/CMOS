#! /usr/bin/env python
#coding:UTF-8

__version__ = '1.0'
__date__ = '2016/12/04'
__author__ = 'Takashi Hanasaka'

'''
make single event tree
    '''


import pyfits
import numpy as np
from ROOT import gROOT,TTree,TFile,AddressOf,TCanvas,TH1F
import sys



f = TFile( '20161111+20161116_perfect_tree2.root', 'recreate' )
tr = TTree( 'tree_single', 'tree' )

gROOT.ProcessLine(\
"struct MyStruct {\
   Int_t    Arg;\
   Int_t    Frame;\
   Int_t    Event_th;\
   Int_t    Split_th;\
   Int_t    X;\
   Int_t    Y;\
   Int_t    Xray;\
   Int_t    PH17;\
   Int_t    PH18;\
   Int_t    PH19;\
   Int_t    PH24;\
   Int_t    PH25;\
   Int_t    PH26;\
   Int_t    PH31;\
   Int_t    PH32;\
   Int_t    PH33;\
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
tr.Branch('PH17', AddressOf(my,'PH17'), 'PH17/I');
tr.Branch('PH18', AddressOf(my,'PH18'), 'PH18/I');
tr.Branch('PH19', AddressOf(my,'PH19'), 'PH19/I');
tr.Branch('PH24', AddressOf(my,'PH24'), 'PH24/I');
tr.Branch('PH25', AddressOf(my,'PH25'), 'PH25/I');
tr.Branch('PH26', AddressOf(my,'PH26'), 'PH26/I');
tr.Branch('PH31', AddressOf(my,'PH31'), 'PH31/I');
tr.Branch('PH32', AddressOf(my,'PH32'), 'PH32/I');
tr.Branch('PH33', AddressOf(my,'PH33'), 'PH33/I');

argvs = sys.argv
root = TFile(argvs[-1])


for i in range(1,11) :
    print 'tree = %s' %i
    tree = root.Get('tree%s' %i)
    entry = tree.GetEntries()

    for j in range(entry) :
        tree.GetEntry(j)
        print 'entry = %s' %j
        if tree.PH17 < 9.279 and tree.PH18 < 9.279 and tree.PH19 < 9.279 and tree.PH24 < 9.279 \
        and tree.PH26 < 9.279 and tree.PH31 < 9.279 and tree.PH32 < 9.279 and tree.PH33 < 9.279 :

            my.Arg = tree.Arg
            my.Frame = tree.Frame
            my.Event_th = tree.Event_th
            my.Split_th = 9.279
            my.X = tree.X
            my.Y = tree.Y
            my.Xray = tree.PH25
            my.PH17 = tree.PH17
            my.PH18 = tree.PH18
            my.PH19 = tree.PH19
            my.PH24 = tree.PH24
            my.PH25 = tree.PH25
            my.PH26 = tree.PH26
            my.PH31 = tree.PH31
            my.PH32 = tree.PH32
            my.PH33 = tree.PH33

            tr.Fill()

f.Write()
f.Close()

'''
if __name__ == '__main__':
    rep = ''
    while not rep in [ 'q', 'Q' ]:
        rep = raw_input( 'enter "q" to quit: ' )
        if 1 < len(rep):
            rep = rep[0]
'''
