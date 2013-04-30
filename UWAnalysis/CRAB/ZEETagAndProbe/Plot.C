{
  //TFile *file = TFile::Open("analysis.root");
  TTree *tree = _file0->Get("tagAndProbeelectron2l2t17L/tagAndProbeTree");
  TH1F *hist = new TH1F("hist","hist",40,70,120);
  //tree->Draw("mass>>hist","abs(eta)>1.566&&abs(eta)<2.4&&matchPass==1&&MVAIDPass==1");
  tree->Draw("mass>>hist","abs(eta)<1.442&&matchPass==1&&MVAIDPass==1&&ISOPass==1&&hltPass==1");
}
