#!/bin/sh
voms-proxy-init --voms cms --valid 100:00


#farmoutAnalysisJobs  $1  --input-dir=/store/user/friis/DoubleMu/embedded_2012A_mutau_2012-05-29-8TeV-PatTuple-v5-c9b7dbb/    MTEM_2012A      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MT-EM.py
farmoutAnalysisJobs  $1  --clean-crab-dupes --input-dir=/store/user/friis/DoubleMu/embedded_2012B_mutau_193752_195135_2012-05-29-8TeV-PatTuple-v11-afde45e/8abec6319d88c45f391ca5c79f24387e     MTEM_2012B_1      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MT-EM.py
farmoutAnalysisJobs  $1  --clean-crab-dupes --input-dir=/store/user/friis/DoubleMu/embedded_2012B_etau_195147_196070_2012-05-29-8TeV-PatTuple-v11-afde45e/8abec6319d88c45f391ca5c79f24387e     MTEM_2012B_2      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MT-EM.py

farmoutAnalysisJobs  $1  --clean-crab-dupes --input-dir=/store/user/friis/DoubleMu/embedded_2012A_etau_2012-05-29-8TeV-PatTuple-v5-c9b7dbb/    ETEM_2012A      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-ET-EM.py
farmoutAnalysisJobs  $1  --clean-crab-dupes --input-dir=/store/user/friis/DoubleMu/embedded_2012B_etau_193752_195135_2012-05-29-8TeV-PatTuple-v11-afde45e/8abec6319d88c45f391ca5c79f24387e     ETEM_2012B_1      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-ET-EM.py
farmoutAnalysisJobs  $1  --clean-crab-dupes --input-dir=/store/user/friis/DoubleMu/embedded_2012B_mutau_195147_196070_2012-05-29-8TeV-PatTuple-v11-afde45e/8abec6319d88c45f391ca5c79f24387e     ETEM_2012B_2      $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-ET-EM.py


