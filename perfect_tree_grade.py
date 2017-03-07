#! /usr/bin/env python
#coding:UTF-8

__version__ = '1.0'
__date__ = '2016/12/04'
__author__ = 'Takashi Hanasaka'

'''
make grade event tree
    '''


import pyfits
import numpy as np
from ROOT import gROOT,TTree,TFile,AddressOf,TCanvas,TH1F
import sys



f = TFile( '20161202_grade_test.root', 'recreate' )
tr2 = TTree( 'tree_grade2', 'tree' )
tr3 = TTree( 'tree_grade3', 'tree' )
tr4 = TTree( 'tree_grade4', 'tree' )
tr6 = TTree( 'tree_grade6', 'tree' )

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
my2 = MyStruct()
my3 = MyStruct()
my4 = MyStruct()
my6 = MyStruct()


tr2.Branch('Arg', AddressOf(my2,'Arg'), 'Arg/I');
tr2.Branch('Frame', AddressOf(my2,'Frame'), 'Frame/I');
tr2.Branch('Event_th', AddressOf(my2,'Event_th'), 'Event_th/I');
tr2.Branch('Split_th', AddressOf(my2,'Split_th'), 'Split_th/I');
tr2.Branch('X', AddressOf(my2,'X'), 'X/I');
tr2.Branch('Y', AddressOf(my2,'Y'), 'Y/I');
tr2.Branch('Xray', AddressOf(my2,'Xray'), 'Xray/I');
tr2.Branch('PH17', AddressOf(my2,'PH17'), 'PH17/I');
tr2.Branch('PH18', AddressOf(my2,'PH18'), 'PH18/I');
tr2.Branch('PH19', AddressOf(my2,'PH19'), 'PH19/I');
tr2.Branch('PH24', AddressOf(my2,'PH24'), 'PH24/I');
tr2.Branch('PH25', AddressOf(my2,'PH25'), 'PH25/I');
tr2.Branch('PH26', AddressOf(my2,'PH26'), 'PH26/I');
tr2.Branch('PH31', AddressOf(my2,'PH31'), 'PH31/I');
tr2.Branch('PH32', AddressOf(my2,'PH32'), 'PH32/I');
tr2.Branch('PH33', AddressOf(my2,'PH33'), 'PH33/I');

tr3.Branch('Arg', AddressOf(my3,'Arg'), 'Arg/I');
tr3.Branch('Frame', AddressOf(my3,'Frame'), 'Frame/I');
tr3.Branch('Event_th', AddressOf(my3,'Event_th'), 'Event_th/I');
tr3.Branch('Split_th', AddressOf(my3,'Split_th'), 'Split_th/I');
tr3.Branch('X', AddressOf(my3,'X'), 'X/I');
tr3.Branch('Y', AddressOf(my3,'Y'), 'Y/I');
tr3.Branch('Xray', AddressOf(my3,'Xray'), 'Xray/I');
tr3.Branch('PH17', AddressOf(my3,'PH17'), 'PH17/I');
tr3.Branch('PH18', AddressOf(my3,'PH18'), 'PH18/I');
tr3.Branch('PH19', AddressOf(my3,'PH19'), 'PH19/I');
tr3.Branch('PH24', AddressOf(my3,'PH24'), 'PH24/I');
tr3.Branch('PH25', AddressOf(my3,'PH25'), 'PH25/I');
tr3.Branch('PH26', AddressOf(my3,'PH26'), 'PH26/I');
tr3.Branch('PH31', AddressOf(my3,'PH31'), 'PH31/I');
tr3.Branch('PH32', AddressOf(my3,'PH32'), 'PH32/I');
tr3.Branch('PH33', AddressOf(my3,'PH33'), 'PH33/I');

tr4.Branch('Arg', AddressOf(my4,'Arg'), 'Arg/I');
tr4.Branch('Frame', AddressOf(my4,'Frame'), 'Frame/I');
tr4.Branch('Event_th', AddressOf(my4,'Event_th'), 'Event_th/I');
tr4.Branch('Split_th', AddressOf(my4,'Split_th'), 'Split_th/I');
tr4.Branch('X', AddressOf(my4,'X'), 'X/I');
tr4.Branch('Y', AddressOf(my4,'Y'), 'Y/I');
tr4.Branch('Xray', AddressOf(my4,'Xray'), 'Xray/I');
tr4.Branch('PH17', AddressOf(my4,'PH17'), 'PH17/I');
tr4.Branch('PH18', AddressOf(my4,'PH18'), 'PH18/I');
tr4.Branch('PH19', AddressOf(my4,'PH19'), 'PH19/I');
tr4.Branch('PH24', AddressOf(my4,'PH24'), 'PH24/I');
tr4.Branch('PH25', AddressOf(my4,'PH25'), 'PH25/I');
tr4.Branch('PH26', AddressOf(my4,'PH26'), 'PH26/I');
tr4.Branch('PH31', AddressOf(my4,'PH31'), 'PH31/I');
tr4.Branch('PH32', AddressOf(my4,'PH32'), 'PH32/I');
tr4.Branch('PH33', AddressOf(my4,'PH33'), 'PH33/I');

tr6.Branch('Arg', AddressOf(my6,'Arg'), 'Arg/I');
tr6.Branch('Frame', AddressOf(my6,'Frame'), 'Frame/I');
tr6.Branch('Event_th', AddressOf(my6,'Event_th'), 'Event_th/I');
tr6.Branch('Split_th', AddressOf(my6,'Split_th'), 'Split_th/I');
tr6.Branch('X', AddressOf(my6,'X'), 'X/I');
tr6.Branch('Y', AddressOf(my6,'Y'), 'Y/I');
tr6.Branch('Xray', AddressOf(my6,'Xray'), 'Xray/I');
tr6.Branch('PH17', AddressOf(my6,'PH17'), 'PH17/I');
tr6.Branch('PH18', AddressOf(my6,'PH18'), 'PH18/I');
tr6.Branch('PH19', AddressOf(my6,'PH19'), 'PH19/I');
tr6.Branch('PH24', AddressOf(my6,'PH24'), 'PH24/I');
tr6.Branch('PH25', AddressOf(my6,'PH25'), 'PH25/I');
tr6.Branch('PH26', AddressOf(my6,'PH26'), 'PH26/I');
tr6.Branch('PH31', AddressOf(my6,'PH31'), 'PH31/I');
tr6.Branch('PH32', AddressOf(my6,'PH32'), 'PH32/I');
tr6.Branch('PH33', AddressOf(my6,'PH33'), 'PH33/I');


argvs = sys.argv
root = TFile(argvs[-1])

for i in range(1,7) :
    print 'tree = %s' %i
    tree = root.Get('tree%s' %i)
    entry = tree.GetEntries()

    for j in range(entry) :
        tree.GetEntry(j)
        print 'entry = %s' %j

        Xray2 = 0
        Xray3 = 0
        Xray4 = 0
        Xray6 = 0

        if tree.PH9 < 9.279 and tree.PH10 < 9.279 and tree.PH11 < 9.279 and tree.PH12 < 9.279 \
        and tree.PH13 < 9.279 and tree.PH16 < 9.279 and tree.PH20 < 9.279 and tree.PH23 < 9.279 \
        and tree.PH27 < 9.279 and tree.PH30 < 9.279 and tree.PH34 < 9.279 and tree.PH37 < 9.279 \
        and tree.PH38 < 9.279 and tree.PH39 < 9.279 and tree.PH40 < 9.279 and tree.PH41 < 9.279 :
            #grade2
            if tree.PH32 > 9.279 and tree.PH17 < 9.279 and tree.PH18 < 9.279 and tree.PH19 < 9.279 and tree.PH24 < 9.279 and tree.PH26 < 9.279 and tree.PH31 < 9.279 and tree.PH33 < 9.279 \
            and tree.PH38 < 9.279 and tree.PH39 < 9.279 and tree.PH40 < 9.279 :
                Xray2 = tree.PH25 + tree.PH32
                if Xray2 > 3400 :
                    print "(Arg,frame,x,y,Xray) = (%s,%s,%s,%s,%s)" %(tree.Arg,tree.Frame,tree.X,tree.Y,Xray2)

                my2.Arg = tree.Arg
                my2.Frame = tree.Frame
                my2.Event_th = tree.Event_th
                my2.Split_th = 9.279
                my2.X = tree.X
                my2.Y = tree.Y
                my2.Xray = Xray2
                my2.PH17 = tree.PH17
                my2.PH18 = tree.PH18
                my2.PH19 = tree.PH19
                my2.PH24 = tree.PH24
                my2.PH25 = tree.PH25
                my2.PH26 = tree.PH26
                my2.PH31 = tree.PH31
                my2.PH32 = tree.PH32
                my2.PH33 = tree.PH33

                tr2.Fill()

            elif tree.PH18 > 9.279 and tree.PH17 < 9.279 and tree.PH19 < 9.279 and tree.PH24 < 9.279 and tree.PH26 < 9.279 and tree.PH31 < 9.279 and tree.PH32 < 9.279 and tree.PH33 < 9.279 \
            and tree.PH10 < 9.279 and tree.PH11 < 9.279 and tree.PH12 < 9.279 :
                Xray2 = tree.PH25 + tree.PH18
                if Xray2 > 3400 :
                    print "(Arg,frame,x,y,Xray) = (%s,%s,%s,%s,%s)" %(tree.Arg,tree.Frame,tree.X,tree.Y,Xray2)

                my2.Arg = tree.Arg
                my2.Frame = tree.Frame
                my2.Event_th = tree.Event_th
                my2.Split_th = 9.279
                my2.X = tree.X
                my2.Y = tree.Y
                my2.Xray = Xray2
                my2.PH17 = tree.PH17
                my2.PH18 = tree.PH18
                my2.PH19 = tree.PH19
                my2.PH24 = tree.PH24
                my2.PH25 = tree.PH25
                my2.PH26 = tree.PH26
                my2.PH31 = tree.PH31
                my2.PH32 = tree.PH32
                my2.PH33 = tree.PH33
                tr2.Fill()

            #grade3
            elif tree.PH24 > 9.279-20 and tree.PH17 < 9.279 and tree.PH18 < 9.279 and tree.PH19 < 9.279 and tree.PH26 < 9.279 and tree.PH31 < 9.279 and tree.PH32 < 9.279 and tree.PH33 < 9.279 \
            and tree.PH16 < 9.279 and tree.PH23 < 9.279 and tree.PH30 < 9.279 :
                Xray3 = tree.PH25 + tree.PH24
                if Xray3 > 3400 :
                    print "(Arg,frame,x,y,Xray) = (%s,%s,%s,%s,%s)" %(tree.Arg,tree.Frame,tree.X,tree.Y,Xray3)

                my3.Arg = tree.Arg
                my3.Frame = tree.Frame
                my3.Event_th = tree.Event_th
                my3.Split_th = 9.279
                my3.X = tree.X
                my3.Y = tree.Y
                my3.Xray = Xray3
                my3.PH17 = tree.PH17
                my3.PH18 = tree.PH18
                my3.PH19 = tree.PH19
                my3.PH24 = tree.PH24
                my3.PH25 = tree.PH25
                my3.PH26 = tree.PH26
                my3.PH31 = tree.PH31
                my3.PH32 = tree.PH32
                my3.PH33 = tree.PH33
                tr3.Fill()

            #grade4
            elif tree.PH26 > 9.279 and tree.PH17 < 9.279 and tree.PH18 < 9.279 and tree.PH19 < 9.279 and tree.PH24 < 9.279 and tree.PH31 < 9.279 and tree.PH32 < 9.279 and tree.PH33 < 9.279 \
            and tree.PH20 < 9.279 and tree.PH27 < 9.279 and tree.PH34 < 9.279 :
                Xray4 = tree.PH25 + tree.PH26
                if Xray4 > 3400 :
                    print "(Arg,frame,x,y,Xray) = (%s,%s,%s,%s,%s)" %(tree.Arg,tree.Frame,tree.X,tree.Y,Xray4)

                my4.Arg = tree.Arg
                my4.Frame = tree.Frame
                my4.Event_th = tree.Event_th
                my4.Split_th = 9.279
                my4.X = tree.X
                my4.Y = tree.Y
                my4.Xray = Xray4
                my4.PH17 = tree.PH17
                my4.PH18 = tree.PH18
                my4.PH19 = tree.PH19
                my4.PH24 = tree.PH24
                my4.PH25 = tree.PH25
                my4.PH26 = tree.PH26
                my4.PH31 = tree.PH31
                my4.PH32 = tree.PH32
                my4.PH33 = tree.PH33
                tr4.Fill()

            #grade6 up and right
            elif tree.PH32 > 9.279 and tree.PH26 > 9.279 and tree.PH31 < 9.279 and tree.PH24 < 9.279 and tree.PH17 < 9.279 and tree.PH18 < 9.279 and tree.PH19 < 9.279 :
                if tree.PH33 < 9.279 :
                    Xray6 = tree.PH25 + tree.PH32 + tree.PH26

                    my6.Arg = tree.Arg
                    my6.Frame = tree.Frame
                    my6.Event_th = tree.Event_th
                    my6.Split_th = 9.279
                    my6.X = tree.X
                    my6.Y = tree.Y
                    my6.Xray = Xray6
                    my6.PH17 = tree.PH17
                    my6.PH18 = tree.PH18
                    my6.PH19 = tree.PH19
                    my6.PH24 = tree.PH24
                    my6.PH25 = tree.PH25
                    my6.PH26 = tree.PH26
                    my6.PH31 = tree.PH31
                    my6.PH32 = tree.PH32
                    my6.PH33 = tree.PH33
                    tr6.Fill()

                elif tree.PH33 > 9.279 :
                    Xray6 = tree.PH25 + tree.PH32 + tree.PH26 + tree.PH33

                    my6.Arg = tree.Arg
                    my6.Frame = tree.Frame
                    my6.Event_th = tree.Event_th
                    my6.Split_th = 9.279
                    my6.X = tree.X
                    my6.Y = tree.Y
                    my6.Xray = Xray6
                    my6.PH17 = tree.PH17
                    my6.PH18 = tree.PH18
                    my6.PH19 = tree.PH19
                    my6.PH24 = tree.PH24
                    my6.PH25 = tree.PH25
                    my6.PH26 = tree.PH26
                    my6.PH31 = tree.PH31
                    my6.PH32 = tree.PH32
                    my6.PH33 = tree.PH33
                    tr6.Fill()

            #grade6 bottom and right
            elif tree.PH18 > 9.279 and tree.PH26 > 9.279 and tree.PH17 < 9.279 and tree.PH24 < 9.279 and tree.PH31 < 9.279 and tree.PH32 < 9.279 and tree.PH33 < 9.279 :
                if tree.PH19 < 9.279 :
                    Xray6 = tree.PH25 + tree.PH18 + tree.PH26

                    my6.Arg = tree.Arg
                    my6.Frame = tree.Frame
                    my6.Event_th = tree.Event_th
                    my6.Split_th = 9.279
                    my6.X = tree.X
                    my6.Y = tree.Y
                    my6.Xray = Xray6
                    my6.PH17 = tree.PH17
                    my6.PH18 = tree.PH18
                    my6.PH19 = tree.PH19
                    my6.PH24 = tree.PH24
                    my6.PH25 = tree.PH25
                    my6.PH26 = tree.PH26
                    my6.PH31 = tree.PH31
                    my6.PH32 = tree.PH32
                    my6.PH33 = tree.PH33
                    tr6.Fill()

                elif tree.PH19 > 9.279 :
                    Xray6 = tree.PH25 + tree.PH18 + tree.PH26 + tree.PH19

                    my6.Arg = tree.Arg
                    my6.Frame = tree.Frame
                    my6.Event_th = tree.Event_th
                    my6.Split_th = 9.279
                    my6.X = tree.X
                    my6.Y = tree.Y
                    my6.Xray = Xray6
                    my6.PH17 = tree.PH17
                    my6.PH18 = tree.PH18
                    my6.PH19 = tree.PH19
                    my6.PH24 = tree.PH24
                    my6.PH25 = tree.PH25
                    my6.PH26 = tree.PH26
                    my6.PH31 = tree.PH31
                    my6.PH32 = tree.PH32
                    my6.PH33 = tree.PH33
                    tr6.Fill()

            #grade6 left and bottom
            elif tree.PH24 > 9.279 and tree.PH18 > 9.279 and tree.PH31 < 9.279 and tree.PH32 < 9.279 and tree.PH33 < 9.279 and tree.PH26 < 9.279 and tree.PH19 < 9.279 :
                if tree.PH17 < 9.279 :
                    Xray6 = tree.PH25 + tree.PH24 + tree.PH18

                    my6.Arg = tree.Arg
                    my6.Frame = tree.Frame
                    my6.Event_th = tree.Event_th
                    my6.Split_th = 9.279
                    my6.X = tree.X
                    my6.Y = tree.Y
                    my6.Xray = Xray6
                    my6.PH17 = tree.PH17
                    my6.PH18 = tree.PH18
                    my6.PH19 = tree.PH19
                    my6.PH24 = tree.PH24
                    my6.PH25 = tree.PH25
                    my6.PH26 = tree.PH26
                    my6.PH31 = tree.PH31
                    my6.PH32 = tree.PH32
                    my6.PH33 = tree.PH33
                    tr6.Fill()

                elif tree.PH17 > 9.279 :
                    Xray6 = tree.PH25 + tree.PH24 + tree.PH18 + tree.PH17

                    my6.Arg = tree.Arg
                    my6.Frame = tree.Frame
                    my6.Event_th = tree.Event_th
                    my6.Split_th = 9.279
                    my6.X = tree.X
                    my6.Y = tree.Y
                    my6.Xray = Xray6
                    my6.PH17 = tree.PH17
                    my6.PH18 = tree.PH18
                    my6.PH19 = tree.PH19
                    my6.PH24 = tree.PH24
                    my6.PH25 = tree.PH25
                    my6.PH26 = tree.PH26
                    my6.PH31 = tree.PH31
                    my6.PH32 = tree.PH32
                    my6.PH33 = tree.PH33
                    tr6.Fill()

            #grade6 left and up
            elif tree.PH24 > 9.279 and tree.PH32 > 9.279 and tree.PH17 < 9.279 and tree.PH18 < 9.279 and tree.PH19 < 9.279 and tree.PH26 < 9.279 and tree.PH33 < 9.279 :
                if tree.PH31 < 9.279 :
                    Xray6 = tree.PH25 + tree.PH24 + tree.PH32

                    my6.Arg = tree.Arg
                    my6.Frame = tree.Frame
                    my6.Event_th = tree.Event_th
                    my6.Split_th = 9.279
                    my6.X = tree.X
                    my6.Y = tree.Y
                    my6.Xray = Xray6
                    my6.PH17 = tree.PH17
                    my6.PH18 = tree.PH18
                    my6.PH19 = tree.PH19
                    my6.PH24 = tree.PH24
                    my6.PH25 = tree.PH25
                    my6.PH26 = tree.PH26
                    my6.PH31 = tree.PH31
                    my6.PH32 = tree.PH32
                    my6.PH33 = tree.PH33
                    tr6.Fill()

                elif tree.PH31 > 9.279 :
                    Xray6 = tree.PH25 + tree.PH24 + tree.PH32 + tree.PH31

                    my6.Arg = tree.Arg
                    my6.Frame = tree.Frame
                    my6.Event_th = tree.Event_th
                    my6.Split_th = 9.279
                    my6.X = tree.X
                    my6.Y = tree.Y
                    my6.Xray = Xray6
                    my6.PH17 = tree.PH17
                    my6.PH18 = tree.PH18
                    my6.PH19 = tree.PH19
                    my6.PH24 = tree.PH24
                    my6.PH25 = tree.PH25
                    my6.PH26 = tree.PH26
                    my6.PH31 = tree.PH31
                    my6.PH32 = tree.PH32
                    my6.PH33 = tree.PH33
                    tr6.Fill()

f.Write()
f.Close()
