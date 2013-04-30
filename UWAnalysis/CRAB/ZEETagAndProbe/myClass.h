//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Jul 11 12:25:09 2012 by ROOT version 5.32/00
// from TTree tagAndProbeTree/
// found on file: /scratch/stephane/ZEETP_long_data-myTP/myTP-output_100_1_KHt/analysis.root
//////////////////////////////////////////////////////////

#ifndef myClass_h
#define myClass_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class myClass {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Int_t           MVAIDPass;
   Int_t           MVAIDPass;
   Int_t           vertices;
   Float_t         BXminus;
   Float_t         BX0;
   Float_t         BXplus;
   Int_t           ISOPass;
   Int_t           ISOPass;
   Int_t           vertices;
   Float_t         BXminus;
   Float_t         BX0;
   Float_t         BXplus;
   Int_t           hltPass;
   Int_t           matchPass;
   Float_t         mass;
   Float_t         pt;
   Float_t         eta;
   Float_t         massHi;
   Float_t         massLo;

   // List of branches
   TBranch        *b_MVAIDPass;   //!
   TBranch        *b_MVAIDPass;   //!
   TBranch        *b_vertices;   //!
   TBranch        *b_BXminus;   //!
   TBranch        *b_BX0;   //!
   TBranch        *b_BXplus;   //!
   TBranch        *b_ISOPass;   //!
   TBranch        *b_ISOPass;   //!
   TBranch        *b_vertices;   //!
   TBranch        *b_BXminus;   //!
   TBranch        *b_BX0;   //!
   TBranch        *b_BXplus;   //!
   TBranch        *b_hltPass;   //!
   TBranch        *b_matchPass;   //!
   TBranch        *b_mass;   //!
   TBranch        *b_pt;   //!
   TBranch        *b_eta;   //!
   TBranch        *b_massHi;   //!
   TBranch        *b_massLo;   //!

   myClass(TTree *tree=0);
   virtual ~myClass();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef myClass_cxx
myClass::myClass(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/scratch/stephane/ZEETP_long_data-myTP/myTP-output_100_1_KHt/analysis.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/scratch/stephane/ZEETP_long_data-myTP/myTP-output_100_1_KHt/analysis.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("/scratch/stephane/ZEETP_long_data-myTP/myTP-output_100_1_KHt/analysis.root:/tagAndProbeelectron2l2t17L");
      dir->GetObject("tagAndProbeTree",tree);

   }
   Init(tree);
}

myClass::~myClass()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t myClass::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t myClass::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void myClass::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("MVAIDPass", &MVAIDPass, &b_MVAIDPass);
//    fChain->SetBranchAddress("MVAIDPass", &MVAIDPass, &b_MVAIDPass);
   fChain->SetBranchAddress("vertices", &vertices, &b_vertices);
   fChain->SetBranchAddress("BXminus", &BXminus, &b_BXminus);
   fChain->SetBranchAddress("BX0", &BX0, &b_BX0);
   fChain->SetBranchAddress("BXplus", &BXplus, &b_BXplus);
   fChain->SetBranchAddress("ISOPass", &ISOPass, &b_ISOPass);
//    fChain->SetBranchAddress("ISOPass", &ISOPass, &b_ISOPass);
//    fChain->SetBranchAddress("vertices", &vertices, &b_vertices);
//    fChain->SetBranchAddress("BXminus", &BXminus, &b_BXminus);
//    fChain->SetBranchAddress("BX0", &BX0, &b_BX0);
//    fChain->SetBranchAddress("BXplus", &BXplus, &b_BXplus);
   fChain->SetBranchAddress("hltPass", &hltPass, &b_hltPass);
   fChain->SetBranchAddress("matchPass", &matchPass, &b_matchPass);
   fChain->SetBranchAddress("mass", &mass, &b_mass);
   fChain->SetBranchAddress("pt", &pt, &b_pt);
   fChain->SetBranchAddress("eta", &eta, &b_eta);
   fChain->SetBranchAddress("massHi", &massHi, &b_massHi);
   fChain->SetBranchAddress("massLo", &massLo, &b_massLo);
   Notify();
}

Bool_t myClass::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void myClass::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t myClass::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef myClass_cxx
