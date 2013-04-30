#!/bin/sh
voms-proxy-init --voms cms --valid 100:00


farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/swanson-Zjets_M50_2012-06-02-8TeV-078e4bc-ea74c25a04048a8dd7df6542c03c7a9b/USER   		DYJets    $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCZ.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/cepeda-WplusJets_madgraph_2012-06-03-8TeV-40bf417-4bae4b458a2ca6a872dfccd34b84cd42/USER	 		WJets     $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCW.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/TTJets_TuneZ2star_8TeV-madgraph-tauola/friis-TTplusJets_madgraph_2012-05-29-8TeV-PatTuple-67c1f94-4729152ae17d7e4009729a1d0d9e952d/USER		 	 	TTBar     $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MC.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/WWTo2L2Nu_TuneZ2star_8TeV_pythia6_tauola/swanson-WWJetsTo2L2Nu_TuneZ2_7TeV_2012-05-28-8TeV-PatTuple-8a107b9-4729152ae17d7e4009729a1d0d9e952d/USER	 	WW2L      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MC.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/WZTo3LNu_TuneZ2star_8TeV_pythia6_tauola/friis-WZJetsTo3LNu_pythia_2012-05-29-8TeV-PatTuple-67c1f94-4729152ae17d7e4009729a1d0d9e952d/USER				WZ3L      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MC.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/ZZJetsTo4L_TuneZ2star_8TeV-madgraph-tauola/iross-ZZ4LJetsTo4L_madgraph_2012-05-29-8TeV-PatTuple-67c1f94-c8fc7c2ff4112a438286838f75d59cdb/USER			ZZ4L	  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MC.py

#farmoutAnalysisJobs  $1  T11_S-SKIM      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MC.py
#farmoutAnalysisJobs  $1  T11_T-SKIM      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MC.py 
#farmoutAnalysisJobs  $1  T11_TW-SKIM     $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MC.py 
#farmoutAnalysisJobs  $1  W11_3J-SKIM     $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MC.py
#farmoutAnalysisJobs  $1  WZ11_LLQQ-SKIM  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MC.py



