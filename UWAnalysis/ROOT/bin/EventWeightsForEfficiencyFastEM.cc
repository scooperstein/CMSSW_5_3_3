#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"
#include "TF1.h"
#include <math.h> 
#include "TMath.h" 
#include <limits>




double efficiency(double m, double m0, double sigma, double alpha, double n, double norm)
 { 
   const double sqrtPiOver2 = 1.2533141373;
   const double sqrt2 = 1.4142135624;

   double sig = fabs((double) sigma);
   
   double t = (m - m0)/sig ;
   
   if (alpha < 0)
     t = -t;

   double absAlpha = fabs(alpha / sig);
   double a = TMath::Power(n/absAlpha,n)*exp(-0.5*absAlpha*absAlpha);
   double b = absAlpha - n/absAlpha;

   //   if (a>=std::numeric_limits<double>::max()) return -1. ;

   double ApproxErf ;
   double arg = absAlpha / sqrt2 ;
   if (arg > 5.) ApproxErf = 1 ;
   else if (arg < -5.) ApproxErf = -1 ;
   else ApproxErf = TMath::Erf(arg) ;

   double leftArea = (1 + ApproxErf) * sqrtPiOver2 ;
   double rightArea = ( a * 1/TMath::Power(absAlpha - b,n-1)) / (n - 1);
   double area = leftArea + rightArea;

   if ( t <= absAlpha ){
     arg = t / sqrt2 ;
     if (arg > 5.) ApproxErf = 1 ;
     else if (arg < -5.) ApproxErf = -1 ;
     else ApproxErf = TMath::Erf(arg) ;
     return norm * (1 + ApproxErf) * sqrtPiOver2 / area ;
   }
   else{
     return norm * (leftArea +  a * (1/TMath::Power(t-b,n-1) - 1/TMath::Power(absAlpha - b,n-1)) / (1 - n)) / area ;
   }
  
 }


void readdir(TDirectory *dir,optutl::CommandLineParser parser,char TreeToUse[]); 


float weightEMu(float pt1,float pt2) {
  float m0 =14.4751; float sigma = 0.120967; float alpha = 0.0226; float n = 4.3709; float norm=0.874294;


  m0=2.90901; sigma=22.4641;alpha=74.3622;n=3.72143;norm=0.976318;
  float dataMUID = efficiency(pt2,m0,sigma,alpha,n,norm);

  m0=1.74118; sigma=22.5399;alpha=52.1416;n=6.59594;norm=0.980176;
  float mcMUID = efficiency(pt2,m0,sigma,alpha,n,norm);
  

  m0=2.67899; sigma=21.9374;alpha=35.4;n=155.359;norm=0.977301;
  float eleid = efficiency(pt1,m0,sigma,alpha,n,norm);

  m0=-3.1459; sigma=27.0568;alpha=81.9479;n=2.21511;norm=0.974106;
  float mceleid = efficiency(pt1,m0,sigma,alpha,n,norm);



  return dataMUID*0.997841*eleid/(mcMUID*mceleid);
 

}


float weightMuTau(float pt1,float pt2,float eta1,float eta2) {


  float m0; float sigma; float alpha; float n; float norm;
  m0 = 18.52262128; sigma = 1.85879597; alpha = 3.48843815; n = 1.15491294; norm = 1.02489024; 
  float data1B = efficiency(pt2,m0,sigma,alpha,n,norm);

  m0 = 17.92648563; sigma = 1.96846742; alpha = 4.46406075; n = 1.02023992; norm = 1.52260575;
  float data2B = efficiency(pt2,m0,sigma,alpha,n,norm);

  float weighttauB=(0.14*data1B+0.86*data2B);

  m0 = 18.90119559; sigma = 0.14025596; alpha = 0.14482632; n = 1.56126508; norm = 0.81188198; 
  float data1E = efficiency(pt2,m0,sigma,alpha,n,norm);

  m0 = 18.59856420; sigma = 2.49132550; alpha = 10.99643595; n = 1.50651123; norm = 0.87952970;
  float data2E = efficiency(pt2,m0,sigma,alpha,n,norm);

  float weighttauE=(0.14*data1E+0.86*data2E);


  m0 = 15.99983195; sigma = -0.39072829; alpha = 0.28256338; n = 1.72861719; norm = 0.95769408;  
  float mu1B = efficiency(pt1,m0,sigma,alpha,n,norm);

  m0 = 17.21270264; sigma = 0.54997112; alpha = 1.02874912; n = 1.29646487; norm = 0.96724273;
  float mu2B = efficiency(pt1,m0,sigma,alpha,n,norm);

  float weightmuB=(0.14*mu1B+0.86*mu2B);

  m0 = 18.49754887; sigma = -0.16941614; alpha = 0.26076717; n = 1.05494469; norm = 1.53819978; 
  float mu1E = efficiency(pt1,m0,sigma,alpha,n,norm);

  m0 = 15.98037640; sigma = 0.12062946; alpha = 0.02183977; n = 2.84751010; norm = 0.83985656; 
  float mu2E = efficiency(pt1,m0,sigma,alpha,n,norm);

  float weightmuE=(0.14*mu1E+0.86*mu2E);

  float dataIdB20 = 0.961;
  float mcIdB20 = 0.970;
  float dataIdB30 = 0.962;
  float mcIdB30 = 0.973;

  float dataIdE20 = 0.951;
  float mcIdE20 = 0.970;
  float dataIdE30 = 0.955;
  float mcIdE30 = 0.966;
  
 
  
	if(fabs(eta2)<1.5&&pt2>20){
		if(pt1 < 30){
				if(fabs(eta1)<1.2)
					return dataIdB20*weighttauB*weightmuB/(mcIdB20);
				else
					return dataIdE20*weighttauB*weightmuE/(mcIdE20);
		}
		else{
				if(fabs(eta1)<1.2)
					return dataIdB30*weighttauB*weightmuB/(mcIdB30);
				else
					return dataIdE30*weighttauB*weightmuE/(mcIdE30); 
		}   		
	}	
	else if(fabs(eta2)>1.5&&pt2>20){
		if(pt1 < 30){
				if(fabs(eta1)<1.2)
					return dataIdB20*weighttauE*weightmuB/(mcIdB20);
				else
					return dataIdE20*weighttauE*weightmuE/(mcIdE20);
		}
		else{
				if(fabs(eta1)<1.2)
					return dataIdB30*weighttauE*weightmuB/(mcIdB30);
				else
					return dataIdE30*weighttauE*weightmuE/(mcIdE30); 
		}
	}
	else{
	   	return 1.0;		
	}	 	  
  	
// 	if(fabs(eta2)<1.5&&pt2>20){
// 		if(pt1 < 30){
// 				if(fabs(eta1)<1.2)
// 					return weighttauB*weightmuB;
// 				else
// 					return weighttauB*weightmuE;
// 		}
// 		else{
// 				if(fabs(eta1)<1.2)
// 					return weighttauB*weightmuB;
// 				else
// 					return weighttauB*weightmuE; 
// 		}   		
// 	}	
// 	else if(fabs(eta2)>1.5&&pt2>20){
// 		if(pt1 < 30){
// 				if(fabs(eta1)<1.2)
// 					return weighttauE*weightmuB;
// 				else
// 					return weighttauE*weightmuE;
// 		}
// 		else{
// 				if(fabs(eta1)<1.2)
// 					return weighttauE*weightmuB;
// 				else
// 					return weighttauE*weightmuE; 
// 		}
// 	}
// 	else{
// 	   	return 1.0;		
// 	}	

}



float weightETau(float pt1,float pt2,float eta1,float eta2) {


  float m0; float sigma; float alpha; float n; float norm;
  
  m0 = 18.84658959; sigma = 0.25958704; alpha = 0.17300958; n = 2.43491208; norm = 0.85872017;
  float data1 = efficiency(pt2,m0,sigma,alpha,n,norm);

  m0 = 18.48663118; sigma = 1.63417147; alpha = 20.25695815; n = 138.55422224; norm = 0.89456038;
  float data2 = efficiency(pt2,m0,sigma,alpha,n,norm);

  float weighttau=(0.14*data1+0.86*data2);


  m0 = 20.97643939; sigma = 1.15196354; alpha = 2.27544602; n = 1.01743868; norm = 2.04391816;
  float Ele1B = efficiency(pt1,m0,sigma,alpha,n,norm);

  m0 = 22.90752344; sigma = 1.32376429; alpha = 2.17813319; n = 1.03674051; norm = 2.15454768;
  float Ele2B = efficiency(pt1,m0,sigma,alpha,n,norm);

  float weightEleB=(0.14*Ele1B+0.86*Ele2B);


  m0 = 20.59874300; sigma = 1.25425435; alpha = 1.61098921; n = 1.00146962; norm = 60.35067579; 
  float Ele1E = efficiency(pt1,m0,sigma,alpha,n,norm);

  m0 = 22.14553261; sigma = 1.19913124; alpha = 1.75642067; n = 1.00826962; norm = 9.04331617;
  float Ele2E = efficiency(pt1,m0,sigma,alpha,n,norm);

  float weightEleE=(0.14*Ele1E+0.86*Ele2E);

  float dataIdB20 = 0.733;
  float mcIdB20 = 0.795;
  float dataIdB30 = 0.876;
  float mcIdB30 = 0.908;

  float dataIdE20 = 0.389;
  float mcIdE20 = 0.433;
  float dataIdE30 = 0.592;
  float mcIdE30 = 0.617;

  
	if(true){
		if(pt1 < 30){
				if(fabs(eta1)<1.5)
					return dataIdB20*weighttau*weightEleB/(mcIdB20);
				else
					return dataIdE20*weighttau*weightEleE/(mcIdE20);
		}
		else{
				if(fabs(eta1)<1.5)
					return dataIdB30*weighttau*weightEleB/(mcIdB30);
				else
					return dataIdE30*weighttau*weightEleE/(mcIdE30); 
		}   		
	}	

// 	if(true){
// 		if(pt1 < 30){
// 				if(fabs(eta1)<1.5)
// 					return weighttau*weightEleB;
// 				else
// 					return weighttau*weightEleE;
// 		}
// 		else{
// 				if(fabs(eta1)<1.5)
// 					return weighttau*weightEleB;
// 				else
// 					return weighttau*weightEleE; 
// 		}   		
// 	}	


}



int main (int argc, char* argv[]) 
{
   optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
   parser.addOption("branch",optutl::CommandLineParser::kString,"Branch","__CORR__");
   parser.parseArguments (argc, argv);
   
   char TreeToUse[80]="first" ;
   
   TFile *f = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");
   readdir(f,parser,TreeToUse);
   f->Close();

} 


void readdir(TDirectory *dir, optutl::CommandLineParser parser, char TreeToUse[]) 
{
  TDirectory *dirsav = gDirectory;
  TIter next(dir->GetListOfKeys());
  TKey *key;
  char stringA[80]="first";
  
  while ((key = (TKey*)next())) {
  
	printf("Found key=%s \n",key->GetName());
	if(!strcmp(stringA,TreeToUse)) sprintf(TreeToUse,"%s",key->GetName());
	printf("Strings %s %s \n",TreeToUse,stringA);
	TObject *obj = key->ReadObj();

    if (obj->IsA()->InheritsFrom(TDirectory::Class())) {
      dir->cd(key->GetName());
      TDirectory *subdir = gDirectory;
      readdir(subdir,parser,TreeToUse);
      dirsav->cd();
    }
    else if(obj->IsA()->InheritsFrom(TTree::Class())) {
      TTree *t = (TTree*)obj;
      float weight = 1.0;
      TBranch *newBranch = t->Branch(parser.stringValue("branch").c_str(),&weight,(parser.stringValue("branch")+"/F").c_str());

      float pt1;
      float eta1;
      float pt2;
      float eta2;


      t->SetBranchAddress("pt1",&pt1);
      t->SetBranchAddress("eta1",&eta1);
      t->SetBranchAddress("pt2",&pt2);
      t->SetBranchAddress("eta2",&eta2);
      

      printf("Found tree -> weighting\n");
      for(Int_t i=0;i<t->GetEntries();++i)
	{
	  t->GetEntry(i);
	  weight=1.0;
	  if(std::string(TreeToUse).find("muTauEventTree")!= std::string::npos){
	    weight=weightMuTau(pt1,pt2,eta1,eta2);
	  }
	  else if(std::string(TreeToUse).find("eleTauEventTree")!= std::string::npos){
	    weight=weightETau(pt1,pt2,eta1,eta2);
	  }
	  

	  newBranch->Fill();
	}

	t->Write("",TObject::kOverwrite);
	strcpy(TreeToUse,stringA) ;
    }
  }
}
