#!/bin/sh
voms-proxy-init --voms cms --valid 100:00


farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/TauPlusX/swanson-data_TauPlusX_Run2012A_PromptReco_v1_2012-06-02-8TeV-078e4bc-4781a9f4dc0c84a9e1b1308811a1a37a/USER    2012A      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/TauPlusX/swanson-data_TauPlusX_Run2012B_PromptReco_v1_a_2012-06-02-8TeV-078e4bc-4781a9f4dc0c84a9e1b1308811a1a37a/USER	 2012B_1      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/TauPlusX/swanson-data_TauPlusX_Run2012B_PromptReco_v1_a_2012-06-09_8TeV-078e4bc-4781a9f4dc0c84a9e1b1308811a1a37a/USER	 2012B_2      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/TauPlusX/swanson-data_TauPlusX_Run2012B_PromptReco_v1_a_2012-06-13_8TeV-078e4bc-4781a9f4dc0c84a9e1b1308811a1a37a/USER     2012B_3      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/TauPlusX/swanson-data_TauPlusX_Run2012B_PromptReco_v1_a_2012-06-15_8TeV-078e4bc-4781a9f4dc0c84a9e1b1308811a1a37a/USER     2012B_4      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB.py
farmoutAnalysisJobs  $1  --dbs-service-url=http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_01/servlet/DBSServlet --input-dbs-path=/TauPlusX/swanson-data_TauPlusX_Run2012B_PromptReco_v1_a_2012-06-22-8TeV-078e4bc-4781a9f4dc0c84a9e1b1308811a1a37a/USER     2012B_5      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB.py


