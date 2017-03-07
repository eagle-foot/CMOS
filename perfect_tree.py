#! /usr/bin/env python
#coding:UTF-8

__version__ = '1.0'
__date__ = '2016/11/30'
__author__ = 'Takashi Hanasaka'

"""
choose Xray event and make tree
  """

import pyfits
import numpy as np
from ROOT import gROOT,TTree,TFile,AddressOf
import sys

f = TFile( 'tree10.root', 'recreate' )
tr = TTree( 'tree', 'tree' )



#difine argvs
argvs = sys.argv

#file open
hdulist_back = pyfits.open(argvs[-1])
#define scidate
scidata_back = hdulist_back[0].data

#number_x = 2560, number_y = 2160, frame = 97
hdr = hdulist_back[0].header
number_x = hdr['NAXIS1']
number_y = hdr['NAXIS2']
frame = hdr['NUMKIN']

#buck mean
mean_back = np.average(scidata_back[:,:,:])
print 'back mean =%s' %mean_back

gROOT.ProcessLine(\
"struct MyStruct {\
   Int_t    Arg;\
   Int_t    Frame;\
   Int_t    Event_th;\
   Int_t    Split_th;\
   Int_t    X;\
   Int_t    Y;\
   Int_t    PH1;\
   Int_t    PH2;\
   Int_t    PH3;\
   Int_t    PH4;\
   Int_t    PH5;\
   Int_t    PH6;\
   Int_t    PH7;\
   Int_t    PH8;\
   Int_t    PH9;\
   Int_t    PH10;\
   Int_t    PH11;\
   Int_t    PH12;\
   Int_t    PH13;\
   Int_t    PH14;\
   Int_t    PH15;\
   Int_t    PH16;\
   Int_t    PH17;\
   Int_t    PH18;\
   Int_t    PH19;\
   Int_t    PH20;\
   Int_t    PH21;\
   Int_t    PH22;\
   Int_t    PH23;\
   Int_t    PH24;\
   Int_t    PH25;\
   Int_t    PH26;\
   Int_t    PH27;\
   Int_t    PH28;\
   Int_t    PH29;\
   Int_t    PH30;\
   Int_t    PH31;\
   Int_t    PH32;\
   Int_t    PH33;\
   Int_t    PH34;\
   Int_t    PH35;\
   Int_t    PH36;\
   Int_t    PH37;\
   Int_t    PH38;\
   Int_t    PH39;\
   Int_t    PH40;\
   Int_t    PH41;\
   Int_t    PH42;\
   Int_t    PH43;\
   Int_t    PH44;\
   Int_t    PH45;\
   Int_t    PH46;\
   Int_t    PH47;\
   Int_t    PH48;\
   Int_t    PH49;\
};" );




from ROOT import MyStruct
my = MyStruct()

tr.Branch('Arg', AddressOf(my,'Arg'), 'Arg/I');
tr.Branch('Frame', AddressOf(my,'Frame'), 'Frame/I');
tr.Branch('Event_th', AddressOf(my,'Event_th'), 'Event_th/I');
tr.Branch('Split_th', AddressOf(my,'Split_th'), 'Split_th/I');
tr.Branch('X', AddressOf(my,'X'), 'X/I');
tr.Branch('Y', AddressOf(my,'Y'), 'Y/I');
for i in range(1,50) :
    tr.Branch('PH%s' %i, AddressOf(my,'PH%s' %i), 'PH%s/I' %i);
#tr.Branch('PHEx', AddressOf(my,'PHEx'), 'PHEx/I');



for arg in range(41,51):
    print 'arg No.%s' %arg

    #hdulist_X = pyfits.open(argvs[arg])
    hdulist_X = pyfits.open('../data/20161116/20161116_16bit_kin_ex0.1_fra5_len97_roomtemp_55Fe%s.fits' %arg)
    scidata_X = hdulist_X[0].data
    scidata = scidata_X - mean_back
    print 'scidata done'

    mean = np.average(scidata[:,:,:])
    print 'mean = %s' %mean
    sigma = np.std(scidata[:,:,:])
    print 'sigma = %s' %sigma

    event_th = mean + 10*sigma
    split_th = mean + 3*sigma

    for fra in range(frame):
        print ('frame No.%s' %fra)

        for x in range (4,number_x-3):
            for y in range (4,number_y-3):
                if scidata[fra,y,x] > event_th :
                    if scidata[fra,y,x] > scidata[fra,y-1,x] and scidata[fra,y,x] > scidata[fra,y+1,x] \
                    and scidata[fra,y,x] > scidata[fra,y,x-1] and scidata[fra,y,x] > scidata[fra,y,x+1] \
                    and scidata[fra,y,x] > scidata[fra,y-1,x-1] and scidata[fra,y,x] > scidata[fra,y-1,x+1] \
                    and scidata[fra,y,x] > scidata[fra,y+1,x-1] and scidata[fra,y,x] > scidata[fra,y+1,x+1] :
                        my.Arg = arg
                        my.Frame = fra
                        my.Event_th = event_th
                        my.Split_th = split_th
                        my.X = x
                        my.Y = y
                        for j in range(-3,4) :
                            for i in range(-3,4) :
                                n = (i+4)+(7*((j+4)-1))
                                exec("my.PH%s = scidata[fra,y+j,x+i]" %n ) #not good
                        tr.Fill()


f.Write()
f.Close()

hdulist_back.close
hdulist_X.close



'''
import pyfits
import numpy as np
from ROOT import gROOT,TTree,TFile,AddressOf
import sys

f = TFile( '20161111+20161116_perfect_tree.root', 'update' )
tr = TTree( 'back', 'tree' )



#difine argvs
argvs = sys.argv

#file open
hdulist_back = pyfits.open(argvs[-1])
#define scidate
scidata_back = hdulist_back[0].data

#number_x = 2560, number_y = 2160, frame = 97
hdr = hdulist_back[0].header
number_x = hdr['NAXIS1']
number_y = hdr['NAXIS2']
frame = hdr['NUMKIN']

#buck mean
mean_back = np.average(scidata_back[:,:,:])
print 'back mean =%s' %mean_back

sigma_back = np.std(scidata_back[:,:,:])
print 'back sigma =%s' %sigma_back

gROOT.ProcessLine(\
"struct MyStruct {\
   Int_t    Arg;\
   Int_t    Frame;\
   Int_t    Event_th;\
   Int_t    Split_th;\
   Int_t    X;\
   Int_t    Y;\
   Int_t    Xray;\
};" );




from ROOT import MyStruct
my = MyStruct()

tr.Branch('Frame', AddressOf(my,'Frame'), 'Frame/I');
tr.Branch('Event_th', AddressOf(my,'Event_th'), 'Event_th/I');
tr.Branch('Split_th', AddressOf(my,'Split_th'), 'Split_th/I');
tr.Branch('X', AddressOf(my,'X'), 'X/I');
tr.Branch('Y', AddressOf(my,'Y'), 'Y/I');
tr.Branch('Xray', AddressOf(my,'Xray'), 'Xray/I');






event_th = mean_back + 10*sigma_back
split_th = mean_back + 3*sigma_back

for fra in range(frame):
    print ('frame No.%s' %fra)

    for x in range (number_x):
        for y in range (number_y):
            if scidata_back[fra,y,x] > split_th :
                my.Frame = fra
                my.Event_th = event_th
                my.Split_th = split_th
                my.X = x
                my.Y = y
                my.Xray = scidata_back[fra,y,x]
                tr.Fill()


f.Write()
f.Close()

hdulist_back.close
'''
