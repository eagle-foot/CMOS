#include <iostream>

//header ROOT
#include <TROOT.h>
#include <TFile.h>
#include <TH1.h>
#include <TTree.h>
#include <TCanvas.h>

using namespace std;

void test()
{
  //gROOT -> Reset();
  TCanvas *c1 = new TCanvas("c1", "c1", 700, 500);
  c1 -> SetGrid();
  c1 -> SetTicky();
  TH1D *h1 = new TH1D("", "", 1000, 2000, 4000);
  h1 -> GetXaxis() -> SetTitle("PHA[ch]");
  h1 -> GetYaxis() -> SetTitle("counts");
  h1 -> GetXaxis() -> CenterTitle();
  h1 -> GetYaxis() -> CenterTitle();

  TFile *root = new TFile("20161202_perfect_tree2.root");
  TTree *tree = (TTree*)root -> Get("tree_single");
  int Xray ;
  tree -> SetBranchAddress("Xray", &Xray);
  int entry;
  entry = tree -> GetEntries();



  int i;
  for (i = 0; i < entry; i++)
  {
    tree -> GetEntry(i);
    cout << "entry = " << i << endl;
    if (Xray > 2000 )
    {
      h1 -> Fill(Xray);
    }
  }

  h1->Draw();

  return;

}
