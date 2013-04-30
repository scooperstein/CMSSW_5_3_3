{
   gROOT->ProcessLine(".L UWAnalysis/ROOT/macros/plotScripts/templatePlots/makePlot.C");



//    makeLTauStack("muTau/pt1","muTauPlots/muTau_pt1.root","muTau_X",3,"#mu p_{T}","GeV",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/pt1LOG","muTauPlots/muTau_pt1.root","muTau_X",3,"#mu p_{T}","GeV",false,"#tau_{#mu}#tau_{h}",true,false);
// 
//    makeLTauStack("muTau/pt2","muTauPlots/muTau_pt2.root","muTau_X",3,"#tau p_{T}","GeV",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/pt2LOG","muTauPlots/muTau_pt2.root","muTau_X",3,"#tau p_{T}","GeV",false,"#tau_{#mu}#tau_{h}",true,false);
// 
//    makeLTauStack("muTau/eta1","muTauPlots/muTau_eta1.root","muTau_X",3,"#mu #eta","",true,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/eta1LOG","muTauPlots/muTau_eta1.root","muTau_X",3,"#mu #eta","",true,"#tau_{#mu}#tau_{h}",true,false);
// 
//    makeLTauStack("muTau/eta2","muTauPlots/muTau_eta2.root","muTau_X",3,"#tau #eta","",true,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/eta2LOG","muTauPlots/muTau_eta2.root","muTau_X",3,"#tau #eta","",true,"#tau_{#mu}#tau_{h}",true,false);
// 
//    makeLTauStack("muTau/mvis","muTauPlots/muTau_MVis.root","muTau_X",3,"m_{vis}","GeV",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/mvisLOG","muTauPlots/muTau_MVis.root","muTau_X",3,"m_{vis}","GeV",false,"#tau_{#mu}#tau_{h}",true,false);
// 
//    makeLTauStack("muTau/sv","muTauPlots/muTau_SVFit.root","muTau_X",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/svLOG","muTauPlots/muTau_SVFit.root","muTau_X",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,false);

//    makeLTauStack("muTau/mvis_NOB","muTauPlots/muTau_MVis.root","muTau_NoB",2,"m_{vis}","GeV",false,"#tau_{#mu}#tau_{h}",false),false,true;
//    makeLTauStack("muTau/mvis_NOBLOG","muTauPlots/muTau_MVis.root","muTau_NoB",2,"m_{vis}","GeV",false,"#tau_{#mu}#tau_{h}",true,false,true);
// 
//    makeLTauStack("muTau/sv_NOB","muTauPlots/muTau_SVFit.root","muTau_NoB",2,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true,true);
//    makeLTauStack("muTau/sv_NOBLOG","muTauPlots/muTau_SVFit.root","muTau_NoB",2,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true,true);
// 
//    makeLTauStack("muTau/mvis_B","muTauPlots/muTau_MVisLS.root","muTau_B",1,"m_{vis}","GeV",false,"#tau_{#mu}#tau_{h}",false,false,true);
//    makeLTauStack("muTau/mvis_BLOG","muTauPlots/muTau_MVisLS.root","muTau_B",1,"m_{vis}","GeV",false,"#tau_{#mu}#tau_{h}",true,false,true);

//    makeLTauStack("muTau/sv_B","muTauPlots/muTau.root","muTau_B",1,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
//    makeLTauStack("muTau/sv_BLOG","muTauPlots/muTau.root","muTau_B",1,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);

//    makeLTauStack("muTau/mvis_0JetLow","muTauPlots/muTauMVis.root","muTau_0jet_low",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
//    makeLTauStack("muTau/mvis_0JetLowLOG","muTauPlots/muTauMVis.root","muTau_0jet_low",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);
// 
//    makeLTauStack("muTau/mvis_0JetHigh","muTauPlots/muTauMVis.root","muTau_0jet_high",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
//    makeLTauStack("muTau/mvis_0JetHighLOG","muTauPlots/muTauMVis.root","muTau_0jet_high",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);
// 
//    makeLTauStack("muTau/mvis_1JetLow","muTauPlots/muTauMVis.root","muTau_boost_low",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
//    makeLTauStack("muTau/mvis_1JetLowLOG","muTauPlots/muTauMVis.root","muTau_boost_low",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);
// 
//    makeLTauStack("muTau/mvis_1JetHigh","muTauPlots/muTauMVis.root","muTau_boost_high",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
//    makeLTauStack("muTau/mvis_1JetHighLOG","muTauPlots/muTauMVis.root","muTau_boost_high",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);
// 
//    makeLTauStack("muTau/mvis_vbf","muTauPlots/muTauMVis.root","muTau_vbf",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
//    makeLTauStack("muTau/mvis_vbfLOG","muTauPlots/muTauMVis.root","muTau_vbf",3,"m_{#mu#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);

   makeLTauStack("muTau/sv_0JetLow","muTauPlots/muTauSM.root","muTau_0jet_low",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
   makeLTauStack("muTau/sv_0JetLowLOG","muTauPlots/muTauSM.root","muTau_0jet_low",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);

   makeLTauStack("muTau/sv_0JetHigh","muTauPlots/muTauSM.root","muTau_0jet_high",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
   makeLTauStack("muTau/sv_0JetHighLOG","muTauPlots/muTauSM.root","muTau_0jet_high",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);

   makeLTauStack("muTau/sv_1JetLow","muTauPlots/muTauSM.root","muTau_boost_low",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
   makeLTauStack("muTau/sv_1JetLowLOG","muTauPlots/muTauSM.root","muTau_boost_low",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);

   makeLTauStack("muTau/sv_1JetHigh","muTauPlots/muTauSM.root","muTau_boost_high",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
   makeLTauStack("muTau/sv_1JetHighLOG","muTauPlots/muTauSM.root","muTau_boost_high",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);

   makeLTauStack("muTau/sv_vbf","muTauPlots/muTauSM.root","muTau_vbf",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",false,true);
   makeLTauStack("muTau/sv_vbfLOG","muTauPlots/muTauSM.root","muTau_vbf",3,"m_{#tau#tau}","GeV",false,"#tau_{#mu}#tau_{h}",true,true);

//    makeLTauStack("muTau/jets","muTauPlots/muTau_jets.root","muTau_X",3,"Number of Jets","",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/jetsLOG","muTauPlots/muTau_jets.root","muTau_X",3,"Number of  Jets","",false,"#tau_{#mu}#tau_{h}",true,false);
// 
//    makeLTauStack("muTau/bjets","muTauPlots/muTau_bjets.root","muTau_X",3,"Number of  b-Tagged Jets","",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/bjetsLOG","muTauPlots/muTau_bjets.root","muTau_X",3,"Number of b-Tagged Jets","",false,"#tau_{#mu}#tau_{h}",true,false);

   makeLTauStack("muTau/deta","muTauPlots/muTau_DEta.root","muTau_vbf",3,"#Delta #eta(jj)","",false,"#tau_{#mu}#tau_{h}",false,false);
   makeLTauStack("muTau/Mjj","muTauPlots/muTau_MJJ.root","muTau_vbf",3,"M(jj)","GeV",false,"#tau_{#mu}#tau_{h}",false,false);
   
//    makeLTauStack("muTau/vbfEta1","muTauPlots/muTau_vbfEta1.root","muTau_vbf",3,"Leading Jet #eta","",true,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/vbfEta2","muTauPlots/muTau_vbfEta2.root","muTau_vbf",3,"Sub-Leading Jet #eta","",true,"#tau_{#mu}#tau_{h}",false,false);
//    
//    makeLTauStack("muTau/vbfPt1","muTauPlots/muTau_vbfPt1.root","muTau_vbf",3,"Leading Jet p_{T}","",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/vbfPt2","muTauPlots/muTau_vbfPt2.root","muTau_vbf",3,"Sub-Leading Jet p_{T}","",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/vbfMVA","muTauPlots/muTau_vbfMVA.root","muTau_vbf",3,"vbf MVA","",false,"#tau_{#mu}#tau_{h}",false,false);
// 
//    makeLTauStack("muTau/vbfDPhi","muTauPlots/muTau_vbfDPhi.root","muTau_vbf",3,"#Delta#phi_{jj}","",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/vbfDPhiHJ","muTauPlots/muTau_vbfDPhiHJ.root","muTau_vbf",3,"#Delta#phi_{HJ}","",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/vbfDiJetPt","muTauPlots/muTau_vbfDiJetPt.root","muTau_vbf",3,"p_{T}_{jj}","",false,"#tau_{#mu}#tau_{h}",false,false);
// 
//    makeLTauStack("muTau/vbfDiTauPt","muTauPlots/muTau_vbfDiTauPt.root","muTau_vbf",3,"Di-#tau p_{T}","GeV",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/vbfC1","muTauPlots/muTau_vbfC1.root","muTau_vbf",3,"Min(#Delta#eta_{Di-#tau,j})","",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/vbfC2","muTauPlots/muTau_vbfC2.root","muTau_vbf",3,"Visible Di-#tau p_{T}","",false,"#tau_{#mu}#tau_{h}",false,false);
// 
//    makeLTauStack("muTau/vbfDPhiLOG","muTauPlots/muTau_vbfDPhi.root","muTau_vbf",3,"#Delta#phi_{jj}","",false,"#tau_{#mu}#tau_{h}",true,false);
//    makeLTauStack("muTau/vbfDPhiHJLOG","muTauPlots/muTau_vbfDPhiHJ.root","muTau_vbf",3,"#Delta#phi_{HJ}","",false,"#tau_{#mu}#tau_{h}",true,false);
//    makeLTauStack("muTau/vbfDiJetPtLOG","muTauPlots/muTau_vbfDiJetPt.root","muTau_vbf",3,"p_{T}_{jj}","",false,"#tau_{#mu}#tau_{h}",true,false);
   makeLTauStack("muTau/detaLOG","muTauPlots/muTau_DEta.root","muTau_vbf",3,"#Delta #eta(jj)","",false,"#tau_{#mu}#tau_{h}",true,false);
   makeLTauStack("muTau/MjjLOG","muTauPlots/muTau_MJJ.root","muTau_vbf",3,"M(jj)","GeV",false,"#tau_{#mu}#tau_{h}",true,false);
//    makeLTauStack("muTau/vbfDiTauPtLOG","muTauPlots/muTau_vbfDiTauPt.root","muTau_vbf",3,"Di-#tau p_{T}","GeV",false,"#tau_{#mu}#tau_{h}",true,false);
//    makeLTauStack("muTau/vbfC1LOG","muTauPlots/muTau_vbfC1.root","muTau_vbf",3,"Min(#Delta#eta_{Di-#tau,j})","",false,"#tau_{#mu}#tau_{h}",true,false);
//    makeLTauStack("muTau/vbfC2LOG","muTauPlots/muTau_vbfC2.root","muTau_vbf",3,"Visible Di-#tau p_{T}","",false,"#tau_{#mu}#tau_{h}",true,false);
//    makeLTauStack("muTau/vbfMVALOG","muTauPlots/muTau_vbfMVA.root","muTau_vbf",3,"vbf MVA","",false,"#tau_{#mu}#tau_{h}",true,false);
//   
//    makeLTauStack("muTau/PZ","muTauPlots/muTau_PZ.root","muTau_X",3,"p_{#zeta} - 1.5 #times p_{#zeta}^{vis}","GeV",true,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/MT","muTauPlots/muTau_MT.root","muTau_X",3,"M_{T}(#mu,MET)","GeV",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/MET","muTauPlots/muTau_MET.root","muTau_X",3,"MET","GeV",false,"#tau_{#mu}#tau_{h}",false,false);
// 
//    makeLTauStack("muTau/BoostPt","muTauPlots/muTau_BoostedPt.root","muTau_X",3,"highest Jet P_{T}","GeV",false,"#tau_{#mu}#tau_{h}",false,false);
//    makeLTauStack("muTau/BoostEta","muTauPlots/muTau_BoostedEta.root","muTau_X",3,"highest Jet #eta","GeV",true,"#tau_{#mu}#tau_{h}",false,false);
// 
//    makeLTauStack("muTau/NPVs","muTauPlots/muTau_NPVs.root","muTau_X",3,"PVs","",false,"#tau_{#mu}#tau_{h}",false,false);
// 
// 
//    makeLTauStack("eleTau/pt1","eleTauPlots/eleTau_pt1.root","eleTau_X",3,"e p_{T}","GeV",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/pt1LOG","eleTauPlots/eleTau_pt1.root","eleTau_X",3,"e p_{T}","GeV",false,"#tau_{e}#tau_{h}",true);
// 
//   makeLTauStack("eleTau/eta1","eleTauPlots/eleTau_eta1.root","eleTau_X",3,"e #eta","",true,"#tau_{e}#tau_{h}",false,false);
//   makeLTauStack("eleTau/eta1LOG","eleTauPlots/eleTau_eta1.root","eleTau_X",3,"e #eta","",true,"#tau_{e}#tau_{h}",true);
// 
//    makeLTauStack("eleTau/pt2","eleTauPlots/eleTau_pt2.root","eleTau_X",3,"#tau p_{T}","GeV",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/pt2LOG","eleTauPlots/eleTau_pt2.root","eleTau_X",3,"#tau p_{T}","GeV",false,"#tau_{e}#tau_{h}",true);
//  
//   makeLTauStack("eleTau/eta2","eleTauPlots/eleTau_eta2.root","eleTau_X",3,"#tau #eta","",true,"#tau_{e}#tau_{h}",false,false);
//   makeLTauStack("eleTau/eta2LOG","eleTauPlots/eleTau_eta2.root","eleTau_X",3,"#tau #eta","",true,"#tau_{e}#tau_{h}",true);
//  
//    makeLTauStack("eleTau/mvis","eleTauPlots/eleTau_MVis.root","eleTau_X",3,"m_{vis}","GeV",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/mvisLOG","eleTauPlots/eleTau_MVis.root","eleTau_X",3,"m_{vis}","GeV",false,"#tau_{e}#tau_{h}",true);
//  
//    makeLTauStack("eleTau/sv","eleTauPlots/eleTau_SVFit.root","eleTau_X",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/svLOG","eleTauPlots/eleTau_SVFit.root","eleTau_X",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",true);
//  
//    makeLTauStack("eleTau/mvis_NOB","eleTauPlots/eleTau_MVis.root","eleTau_NoB",2,"m_{vis}","GeV",false,"#tau_{e}#tau_{h}",false);
//    makeLTauStack("eleTau/mvis_NOBLOG","eleTauPlots/eleTau_MVis.root","eleTau_NoB",2,"m_{vis}","GeV",false,"#tau_{e}#tau_{h}",true);
// 
//    makeLTauStack("eleTau/sv_NOB","eleTauPlots/eleTau.root","eleTau_NoB",2,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/sv_NOBLOG","eleTauPlots/eleTau.root","eleTau_NoB",2,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/mvis_B","eleTauPlots/eleTau_MVisLS.root","eleTau_B",1,"m_{vis}","GeV",false,"#tau_{e}#tau_{h}",false);
//    makeLTauStack("eleTau/mvis_BLOG","eleTauPlots/eleTau_MVisLS.root","eleTau_B",1,"m_{vis}","GeV",false,"#tau_{e}#tau_{h}",true);
// 
//    makeLTauStack("eleTau/sv_B","eleTauPlots/eleTau_SVFitLS.root","eleTau_B",1,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",false);
//    makeLTauStack("eleTau/sv_BLOG","eleTauPlots/eleTau_SVFitLS.root","eleTau_B",1,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",true);

//    makeLTauStack("eleTau/mvis_0JetLow","eleTauPlots/eleTauMVis.root","eleTau_0jet_low",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/mvis_0JetLowLOG","eleTauPlots/eleTauMVis.root","eleTau_0jet_low",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/mvis_0JetHigh","eleTauPlots/eleTauMVis.root","eleTau_0jet_high",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/mvis_0JetHighLOG","eleTauPlots/eleTauMVis.root","eleTau_0jet_high",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/mvis_1JetLow","eleTauPlots/eleTauMVis.root","eleTau_boost_low",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/mvis_1JetLowLOG","eleTauPlots/eleTauMVis.root","eleTau_boost_low",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/mvis_1JetHigh","eleTauPlots/eleTauMVis.root","eleTau_boost_high",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/mvis_1JetHighLOG","eleTauPlots/eleTauMVis.root","eleTau_boost_high",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/mvis_vbf","eleTauPlots/eleTauMVis.root","eleTau_vbf",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/mvis_vbfLOG","eleTauPlots/eleTauMVis.root","eleTau_vbf",3,"m_{e#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/sv_0JetLow","eleTauPlots/eleTauSM.root","eleTau_0jet_low",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/sv_0JetLowLOG","eleTauPlots/eleTauSM.root","eleTau_0jet_low",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/sv_0JetHigh","eleTauPlots/eleTauSM.root","eleTau_0jet_high",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/sv_0JetHighLOG","eleTauPlots/eleTauSM.root","eleTau_0jet_high",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/sv_1JetLow","eleTauPlots/eleTauSM.root","eleTau_boost_low",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/sv_1JetLowLOG","eleTauPlots/eleTauSM.root","eleTau_boost_low",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/sv_1JetHigh","eleTauPlots/eleTauSM.root","eleTau_boost_high",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/sv_1JetHighLOG","eleTauPlots/eleTauSM.root","eleTau_boost_high",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/sv_vbf","eleTauPlots/eleTauSM.root","eleTau_vbf",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",false,true);
//    makeLTauStack("eleTau/sv_vbfLOG","eleTauPlots/eleTauSM.root","eleTau_vbf",3,"m_{#tau#tau}","GeV",false,"#tau_{e}#tau_{h}",true,true);
// 
//    makeLTauStack("eleTau/PZ","eleTauPlots/eleTau_PZ.root","eleTau_X",3,"p_{#zeta} - 1.5 x p_{#zeta}^{vis}","GeV",true,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/MT","eleTauPlots/eleTau_MT.root","eleTau_X",3,"M_{T}(e,MET)","GeV",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/MET","eleTauPlots/eleTau_MET.root","eleTau_X",3,"MET","GeV",false,"#tau_{e}#tau_{h}",false,false);
// 
// 
//    makeLTauStack("eleTau/jets","eleTauPlots/eleTau_jets.root","eleTau_X",3,"Number of Jets","",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/jetsLOG","eleTauPlots/eleTau_jets.root","eleTau_X",3,"Number of Jets","",false,"#tau_{e}#tau_{h}",true);
// 
//    makeLTauStack("eleTau/vbfEta1","eleTauPlots/eleTau_vbfEta1.root","eleTau_vbf",3,"Leading Jet #eta","",true,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/vbfEta2","eleTauPlots/eleTau_vbfEta2.root","eleTau_vbf",3,"Sub-Leading Jet #eta","",true,"#tau_{e}#tau_{h}",false,false);
//    
//   makeLTauStack("eleTau/vbfPt1","eleTauPlots/eleTau_vbfPt1.root","eleTau_vbf",3,"Leading Jet p_{T}","",false,"#tau_{e}#tau_{h}",false,false);
//   makeLTauStack("eleTau/vbfPt2","eleTauPlots/eleTau_vbfPt2.root","eleTau_vbf",3,"Sub-Leading Jet p_{T}","",false,"#tau_{e}#tau_{h}",false,false);
// 
//    makeLTauStack("eleTau/bjets","eleTauPlots/eleTau_bjets.root","eleTau_X",3,"Number of b-Tagged Jets","",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/bjetsLOG","eleTauPlots/eleTau_bjets.root","eleTau_X",3,"Number of b-Tagged Jets","",false,"#tau_{e}#tau_{h}",true);
// 
//    makeLTauStack("eleTau/BoostPt","eleTauPlots/eleTau_BoostedPt.root","eleTau_X",3,"highest Jet P_{T}","GeV",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/BoostEta","eleTauPlots/eleTau_BoostedEta.root","eleTau_X",3,"highest Jet #eta","GeV",true,"#tau_{e}#tau_{h}",false,false);
// 
//    makeLTauStack("eleTau/vbfMVA","eleTauPlots/eleTau_vbfMVA.root","eleTau_vbf",3,"vbf MVA","",false,"#tau_{e}#tau_{h}",false,false);
// 
//    makeLTauStack("eleTau/vbfDPhi","eleTauPlots/eleTau_vbfDPhi.root","eleTau_vbf",3,"#Delta#phi_{jj}","",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/vbfDPhiHJ","eleTauPlots/eleTau_vbfDPhiHJ.root","eleTau_vbf",3,"#Delta#phi_{HJ}","",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/vbfDiJetPt","eleTauPlots/eleTau_vbfDiJetPt.root","eleTau_vbf",3,"p_{T}_{jj}","",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/deta","eleTauPlots/eleTau_DEta.root","eleTau_vbf",3,"#Delta #eta(jj)","",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/Mjj","eleTauPlots/eleTau_MJJ.root","eleTau_vbf",3,"M(jj)","GeV",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/vbfDiTauPt","eleTauPlots/eleTau_vbfDiTauPt.root","eleTau_vbf",3,"Di-#tau p_{T}","GeV",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/vbfC1","eleTauPlots/eleTau_vbfC1.root","eleTau_vbf",3,"Min(#Delta#eta_{Di-#tau,j})","",false,"#tau_{e}#tau_{h}",false,false);
//    makeLTauStack("eleTau/vbfC2","eleTauPlots/eleTau_vbfC2.root","eleTau_vbf",3,"Visible Di-#tau p_{T}","",false,"#tau_{e}#tau_{h}",false,false);
// 
//    makeLTauStack("eleTau/vbfDPhiLOG","eleTauPlots/eleTau_vbfDPhi.root","eleTau_vbf",3,"#Delta#phi_{jj}","",false,"#tau_{e}#tau_{h}",true,false);
//    makeLTauStack("eleTau/vbfDPhiHJLOG","eleTauPlots/eleTau_vbfDPhiHJ.root","eleTau_vbf",3,"#Delta#phi_{HJ}","",false,"#tau_{e}#tau_{h}",true,false);
//    makeLTauStack("eleTau/vbfDiJetPtLOG","eleTauPlots/eleTau_vbfDiJetPt.root","eleTau_vbf",3,"p_{T}_{jj}","",false,"#tau_{e}#tau_{h}",true,false);
//    makeLTauStack("eleTau/detaLOG","eleTauPlots/eleTau_DEta.root","eleTau_vbf",3,"#Delta #eta(jj)","",false,"#tau_{e}#tau_{h}",true,false);
//    makeLTauStack("eleTau/MjjLOG","eleTauPlots/eleTau_MJJ.root","eleTau_vbf",3,"M(jj)","GeV",false,"#tau_{e}#tau_{h}",true,false);
//    makeLTauStack("eleTau/vbfDiTauPtLOG","eleTauPlots/eleTau_vbfDiTauPt.root","eleTau_vbf",3,"Di-#tau p_{T}","GeV",false,"#tau_{e}#tau_{h}",true,false);
//    makeLTauStack("eleTau/vbfC1LOG","eleTauPlots/eleTau_vbfC1.root","eleTau_vbf",3,"Min(#Delta#eta_{Di-#tau,j})","",false,"#tau_{e}#tau_{h}",true,false);
//    makeLTauStack("eleTau/vbfC2LOG","eleTauPlots/eleTau_vbfC2.root","eleTau_vbf",3,"Visible Di-#tau p_{T}","",false,"#tau_{e}#tau_{h}",true,false);
//    makeLTauStack("eleTau/vbfMVALOG","eleTauPlots/eleTau_vbfMVA.root","eleTau_vbf",3,"vbf MVA","",false,"#tau_{e}#tau_{h}",true,false);
// 
//    makeLTauStack("eleTau/NPVs","eleTauPlots/eleTau_NPVs.root","eleTau_X",3,"PVs","",false,"#tau_{e}#tau_{h}",false,false);


//    makeEMuStack("eleMu/pt1","eleMuPlots/pt1.root","eleMu_X",1,"e p_{T}","GeV",false,false);
//    makeEMuStack("eleMu/pt1LOG","eleMuPlots/pt1.root","eleMu_X",1,"e p_{T}","GeV",false,true);
// 
//    makeEMuStack("eleMu/pt2","eleMuPlots/pt2.root","eleMu_X",1,"#mu p_{T}","GeV",false,false);
//    makeEMuStack("eleMu/pt2LOG","eleMuPlots/pt2.root","eleMu_X",1,"#mu p_{T}","GeV",false,true);
// 
// 
//    makeEMuStack("eleMu/mvis","eleMuPlots/mvis.root","eleMu_X",1,"m_{vis}","GeV",false,false);
//    makeEMuStack("eleMu/mvisLOG","eleMuPlots/mvis.root","eleMu_X",1,"m_{vis}","GeV",false,true);
// 
//    makeEMuStack("eleMu/sv","eleMuPlots/sv.root","eleMu_X",1,"m_{#tau#tau}","GeV",false,false);
//    makeEMuStack("eleMu/svLOG","eleMuPlots/sv.root","eleMu_X",1,"m_{#tau#tau}","GeV",false,true);
// 
//    makeEMuStack("eleMu/mvis_NOB","eleMuPlots/mvis.root","eleMu_NoB",2,"m_{#tau#tau}","GeV",false,false);
//    makeEMuStack("eleMu/mvis_NOBLOG","eleMuPlots/mvis.root","eleMu_NoB",2,"m_{#tau#tau}","GeV",false,true);
// 
//    makeEMuStack("eleMu/sv_NOB","eleMuPlots/sv.root","eleMu_NoB",2,"m_{#tau#tau}","GeV",false,false);
//    makeEMuStack("eleMu/sv_NOBLOG","eleMuPlots/sv.root","eleMu_NoB",2,"m_{#tau#tau}","GeV",false,true);
// 
//    makeEMuStack("eleMu/mvis_B","eleMuPlots/mvis_LS.root","eleMu_B",1,"m_{vis}","GeV",false,false);
//    makeEMuStack("eleMu/mvis_BLOG","eleMuPlots/mvis_LS.root","eleMu_B",1,"m_{vis}","GeV",false,true);
// 
//    makeEMuStack("eleMu/sv_B","eleMuPlots/sv_LS.root","eleMu_B",1,"m_{#tau#tau}","GeV",false,false);
//    makeEMuStack("eleMu/sv_BLOG","eleMuPlots/sv_LS.root","eleMu_B",1,"m_{#tau#tau}","GeV",false,true);
// 
// 
//    makeEMuStack("eleMu/mvis_SM0","eleMuPlots/mvis.root","eleMu_SM0",3,"m_{vis}","GeV",false,false);
//    makeEMuStack("eleMu/mvis_SM0LOG","eleMuPlots/mvis.root","eleMu_SM0",3,"m_{vis}","GeV",false,true);
// 
//    makeEMuStack("eleMu/sv_SM0","eleMuPlots/sv.root","eleMu_SM0",3,"m_{#tau#tau}","GeV",false,false);
//    makeEMuStack("eleMu/sv_SM0LOG","eleMuPlots/sv.root","eleMu_SM0",3,"m_{#tau#tau}","GeV",false,true);
// 
// 
//    makeEMuStack("eleMu/mvis_SM1","eleMuPlots/mvis_LS.root","eleMu_SM1",3,"m_{vis}","GeV",false,false);
//    makeEMuStack("eleMu/mvis_SM1LOG","eleMuPlots/mvis_LS.root","eleMu_SM1",3,"m_{vis}","GeV",false,true);
// 
//    makeEMuStack("eleMu/sv_SM1","eleMuPlots/sv_LS.root","eleMu_SM1",3,"m_{#tau#tau}","GeV",false,false);
//    makeEMuStack("eleMu/sv_SM1LOG","eleMuPlots/sv_LS.root","eleMu_SM1",3,"m_{#tau#tau}","GeV",false,true);
// 
//    makeEMuStack("eleMu/mvis_SM2","eleMuPlots/mvis_LS.root","eleMu_SM2",3,"m_{vis}","GeV",false,false);
//    makeEMuStack("eleMu/mvis_SM2LOG","eleMuPlots/mvis_LS.root","eleMu_SM2",3,"m_{vis}","GeV",false,true);
// 
//    makeEMuStack("eleMu/sv_SM2","eleMuPlots/sv_LS.root","eleMu_SM2",3,"m_{#tau#tau}","GeV",false,false);
//    makeEMuStack("eleMu/sv_SM2LOG","eleMuPlots/sv_LS.root","eleMu_SM2",3,"m_{#tau#tau}","GeV",false,true);






}

