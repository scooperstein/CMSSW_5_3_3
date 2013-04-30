#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "PhysicsTools/Utilities/interface/Lumi3DReWeighting.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"

//Distribution from Fall 2011

std::vector<float> data;
std::vector<float> mc;
edm::Lumi3DReWeighting *LumiWeights;
edm::LumiReWeighting *LumiWeightsOld;

//2012 weights ICHEP Dataset
Double_t weights_[60] = { 
	1.767e-06, 
	2.849e-06, 
	6.885e-06, 
	3.718e-05, 
	9.818e-05, 
	4.248e-04, 
	2.173e-03, 
	5.640e-03, 
	1.149e-02, 
	1.999e-02, 
	3.176e-02, 
	4.584e-02, 
	5.890e-02, 
	7.020e-02, 
	8.011e-02, 
	8.519e-02, 
	8.038e-02, 
	6.914e-02, 
	5.864e-02, 
	5.120e-02, 
	4.586e-02, 
	4.147e-02, 
	3.745e-02, 
	3.362e-02, 
	2.990e-02, 
	2.625e-02, 
	2.270e-02, 
	1.930e-02, 
	1.613e-02, 
	1.323e-02, 
	1.065e-02, 
	8.414e-03, 
	6.519e-03, 
	4.952e-03, 
	3.689e-03, 
	2.694e-03, 
	1.928e-03, 
	1.353e-03, 
	9.303e-04, 
	6.269e-04, 
	4.139e-04, 
	2.677e-04, 
	1.696e-04, 
	1.052e-04, 
	6.391e-05, 
	3.801e-05, 
	2.212e-05, 
	1.261e-05, 
	7.028e-06, 
	3.834e-06, 
	2.047e-06, 
	1.069e-06, 
	5.461e-07, 
	2.730e-07, 
	1.334e-07, 
	6.381e-08, 
	2.985e-08, 
	1.366e-08, 
	6.111e-09, 
	2.674e-09, 
 }; 
    
//Summer12 MC
Double_t weightsMC_[60] = {
    2.344E-05,
    2.344E-05,
    2.344E-05,
    2.344E-05,
    4.687E-04,
    4.687E-04,
    7.032E-04,
    9.414E-04,
    1.234E-03,
    1.603E-03,
    2.464E-03,
    3.250E-03,
    5.021E-03,
    6.644E-03,
    8.502E-03,
    1.121E-02,
    1.518E-02,
    2.033E-02,
    2.608E-02,
    3.171E-02,
    3.667E-02,
    4.060E-02,
    4.338E-02,
    4.520E-02,
    4.641E-02,
    4.735E-02,
    4.816E-02,
    4.881E-02,
    4.917E-02,
    4.909E-02,
    4.842E-02,
    4.707E-02,
    4.501E-02,
    4.228E-02,
    3.896E-02,
    3.521E-02,
    3.118E-02,
    2.702E-02,
    2.287E-02,
    1.885E-02,
    1.508E-02,
    1.166E-02,
    8.673E-03,
    6.190E-03,
    4.222E-03,
    2.746E-03,
    1.698E-03,
    9.971E-04,
    5.549E-04,
    2.924E-04,
    1.457E-04,
    6.864E-05,
    3.054E-05,
    1.282E-05,
    5.081E-06,
    1.898E-06,
    6.688E-07,
    2.221E-07,
    6.947E-08,
    2.047E-08
};    

//2011 Weights
//   Double_t weightsMC_[50] = {
//     0.003388501,
//     0.010357558,
//     0.024724258,
//     0.042348605,
//     0.058279812,
//     0.068851751,
//     0.072914824,
//     0.071579609,
//     0.066811668,
//     0.060672356,
//     0.054528356,
//     0.04919354,
//     0.044886042,
//     0.041341896,
//     0.0384679,
//     0.035871463,
//     0.03341952,
//     0.030915649,
//     0.028395374,
//     0.025798107,
//     0.023237445,
//     0.020602754,
//     0.0180688,
//     0.015559693,
//     0.013211063,
//     0.010964293,
//     0.008920993,
//     0.007080504,
//     0.005499239,
//     0.004187022,
//     0.003096474,
//     0.002237361,
//     0.001566428,
//     0.001074149,
//     0.000721755,
//     0.000470838,
//     0.00030268,
//     0.000184665,
//     0.000112883,
//     6.74043E-05,
//     3.82178E-05,
//     2.22847E-05,
//     1.20933E-05,
//     6.96173E-06,
//     3.4689E-06,
//     1.96172E-06,
//     8.49283E-07,
//     5.02393E-07,
//     2.15311E-07,
//     9.56938E-08
//   };
  
  // 
//  Double_t weights_[50] = {
//    0.00268287,
//    0.0111378,
//    0.0253649,
//    0.0426735,
//    0.0595703,
//    0.0727177,
//    0.0810381,
//    0.0842113,
//    0.0833151,
//    0.0795788,
//    0.0738552,
//    0.0672576,
//    0.0599305,
//    0.0522761,
//    0.0442358,
//    0.0370232,
//    0.030315,
//    0.0243174,
//    0.0189967,
//    0.0145095,
//    0.0107956,
//    0.00779958,
//    0.00555043,
//    0.00381755,
//    0.00257767,
//    0.00169383,
//    0.00108528,
//    0.000661581,
//    0.000409454,
//    0.000254036,
//    0.000151171,
//    8.96485e-05,
//    5.26011e-05,
//    2.82925e-05,
//    1.61978e-05,
//    9.68528e-06,
//    1.01147e-05,
//    0,
//    0,
//    0,
//    0,
//    0,
//    0,
//    0,
//    0,
//    0,
//    0,
//    0,
//    0,
//      0
//  };
// 


//68mb
//  Double_t weightsMC_[50] = {
//     0.00290212,
//     0.0123985,
//     0.0294783,
//     0.0504491,
//     0.0698525,
//     0.0836611,
//     0.0905799,
//     0.0914388,
//     0.0879379,
//     0.0817086,
//     0.073937,
//     0.0653785,
//     0.0565162,
//     0.047707,
//     0.0392591,
//     0.0314457,
//     0.0244864,
//     0.018523,
//     0.013608,
//     0.00970977,
//     0.00673162,
//     0.00453714,
//     0.00297524,
//     0.00189981,
//     0.00118234,
//     0.000717854,
//     0.00042561,
//     0.000246653,
//     0.000139853,
//     7.76535E-05,
//     4.22607E-05,
//     2.25608E-05,
//     1.18236E-05,
//     6.0874E-06,
//     6.04852E-06,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0,
//     0
//   };

void readdir(TDirectory *dir,optutl::CommandLineParser parser,float ev,int doPU,bool doRho,TH1F* puWeight,TH1F* rhoWeight); 



int main (int argc, char* argv[]) 
{
   optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
   parser.addOption("histoName",optutl::CommandLineParser::kString,"Counter Histogram Name","EventSummary");
   parser.addOption("weight",optutl::CommandLineParser::kDouble,"Weight to apply",1.0);
   parser.addOption("type",optutl::CommandLineParser::kInteger,"Type",0);
   parser.addOption("branch",optutl::CommandLineParser::kString,"Branch","__WEIGHT__");
   parser.addOption("doOneD",optutl::CommandLineParser::kInteger,"Do OneD",0);

   
   parser.parseArguments (argc, argv);
   

   //read PU info
   TH1F *puWeight=0;
   int doPU=0;
   TFile *fPU = new TFile("../puInfo.root");

   if(fPU!=0 && fPU->IsOpen()) {
     puWeight = (TH1F*)fPU->Get("weight");
     doPU=1;
     printf("ENABLING PU WEIGHTING USING VERTICES\n");

   }

   TFile *fPU2 = new TFile("../puInfo3D.root");
   TFile *fPU22 = new TFile("../puInfoMC3D.root");
   TFile *fPU3 = new TFile("../Weight3D.root");
   TFile *fPU4 = new TFile("Weight3D.root");

   if(fPU2!=0 && fPU2->IsOpen()&& fPU22!=0 && fPU22->IsOpen() && (!(fPU3!=0 && fPU3->IsOpen())) &&(!(fPU4!=0 && fPU4->IsOpen()))){
     doPU=2;
     printf("ENABLING PU WEIGHTING USING 3D- I HAVE TO CALCULATE WEIGHTS SORRY\n");
     LumiWeights = new edm::Lumi3DReWeighting("../puInfoMC3D.root","../puInfo3D.root","pileup","pileup","");
     LumiWeights->weight3D_init(1.0);
   }
   else  if(fPU3!=0 && fPU3->IsOpen()) {
     doPU=2;
     printf("ENABLING PU WEIGHTING USING 3D with ready distribution\n");
     fPU3->Close();
     LumiWeights = new edm::Lumi3DReWeighting(mc,data,"");
     LumiWeights->weight3D_init("../Weight3D.root");
   }
   else   if(fPU4!=0 && fPU4->IsOpen()) {

     //searxch in this folder
       doPU=2;
       printf("ENABLING PU WEIGHTING USING 3D with  distribution you just made\n");
       fPU4->Close();
       LumiWeights = new edm::Lumi3DReWeighting(mc,data,"");
       LumiWeights->weight3D_init("Weight3D.root");

   }
   else if(parser.integerValue("doOneD")) {
   

     doPU=3;
     
//     LumiWeightsOld = new edm::LumiReWeighting("weight.root","weight.root","mc","data");
     
     std::vector<float> mc;
     std::vector<float> data;

     for(unsigned int i=0;i<60;++i) {
       mc.push_back(weightsMC_[i]);
       data.push_back(weights_[i]);
     }


    LumiWeightsOld = new edm::LumiReWeighting(mc,data);

     
   }
   


   //read PU info
   TH1F *rhoWeight=0;
   bool doRho=false;
   TFile *fRho = new TFile("../rhoInfo.root");

   if(fRho!=0 && fRho->IsOpen()) {
     rhoWeight = (TH1F*)fRho->Get("weight");
     doRho=true;
     printf("ENABLING Rho WEIGHTING\n");

   }

 
   TFile *g = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");

   TH1F* evC  = (TH1F*)g->Get(parser.stringValue("histoName").c_str());
   float ev = evC->GetBinContent(1);
   
   g->Close();
   
   printf("Found  %f Events Counted\n",ev);
   
   TFile *f = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");   

   readdir(f,parser,ev,doPU,doRho,puWeight,rhoWeight);
   f->Close();
   if(fPU!=0 && fPU->IsOpen())
     fPU->Close();

   if(fPU2!=0 && fPU2->IsOpen())
     fPU2->Close();


} 


void readdir(TDirectory *dir,optutl::CommandLineParser parser,float ev,int doPU,bool doRho,TH1F *puWeight,TH1F *rhoWeight) 
{
  TDirectory *dirsav = gDirectory;
  TIter next(dir->GetListOfKeys());
  TKey *key;
  while ((key = (TKey*)next())) {
    printf("Found key=%s \n",key->GetName());
    TObject *obj = key->ReadObj();

    if (obj->IsA()->InheritsFrom(TDirectory::Class())) {
      dir->cd(key->GetName());
      TDirectory *subdir = gDirectory;
      readdir(subdir,parser,ev,doPU,doRho,puWeight,rhoWeight);
      dirsav->cd();
    }
    else if(obj->IsA()->InheritsFrom(TTree::Class())) {
      TTree *t = (TTree*)obj;
      float weight = parser.doubleValue("weight")/(ev);
      int   type = parser.integerValue("type");


      TBranch *newBranch = t->Branch(parser.stringValue("branch").c_str(),&weight,(parser.stringValue("branch")+"/F").c_str());
      TBranch *typeBranch = t->Branch("TYPE",&type,"TYPE/I");
      int vertices;
      float bxm=0;
      float bx=0;
      float bxp=0;

      if(doPU==1)
	t->SetBranchAddress("vertices",&vertices);
      else if(doPU==2) {
	t->SetBranchAddress("puBXminus",&bxm);
	t->SetBranchAddress("puBX0",&bx);
	t->SetBranchAddress("puBXplus",&bxp);
      }
      else if( doPU==3 ){
      t->SetBranchAddress("puTruth",&bx);
      }

      float rho=0.0;
      if(doRho)
	t->SetBranchAddress("Rho",&rho);

      printf("Found tree -> weighting\n");
      for(Int_t i=0;i<t->GetEntries();++i)
	{
	  t->GetEntry(i);
	  weight = parser.doubleValue("weight")/(ev);
	  if(doPU==1) {
	    int bin=puWeight->FindBin(vertices);
	    if(bin>puWeight->GetNbinsX())
	      {
		printf("Overflow using max bin\n");
		bin = puWeight->GetNbinsX();
	      }
	    weight*=puWeight->GetBinContent(bin);
	    if(i==1)
	      printf("PU WEIGHT = %f\n",puWeight->GetBinContent(puWeight->FindBin(vertices)));

	  }
	  else if(doPU==2) {
	   float w = LumiWeights->weight3D( bxm,bx,bxp);
	    if(i==1)
	      printf("PU WEIGHT = %f\n",w);
	    weight*=w;
	  }
	  else if(doPU==3) {
	    weight*=LumiWeightsOld->weight(bx);
	  }
	  if(doRho) {
	    weight*=rhoWeight->GetBinContent(rhoWeight->FindBin(rho));
	    if(i==1)
	      printf("RHO WEIGHT = %f\n",rhoWeight->GetBinContent(rhoWeight->FindBin(rho)));
	  }

	  newBranch->Fill();
	  typeBranch->Fill();
	}
      t->Write("",TObject::kOverwrite);
    }
//     else if(obj->IsA()->InheritsFrom(TH1F::Class())) {
//       TH1F *h = (TH1F*)obj;
//       h->Sumw2();
//       printf("scaling histogram with %f entries\n",h->Integral());
//       float weight = parser.doubleValue("weight")/(ev);
//       h->Sumw2();
//       for( int i=1;i<=h->GetNbinsX();++i)
// 	h->SetBinContent(i,h->GetBinContent(i)*weight);
 
//       TDirectory *tmp = gDirectory;
//       h->SetDirectory(gDirectory);
//       h->Write("resultsWeighted");
//     }


  }

}

