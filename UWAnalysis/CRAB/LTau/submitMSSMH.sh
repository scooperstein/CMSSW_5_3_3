#!/bin/sh
voms-proxy-init --voms cms --valid 100:00

farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-80_8TeV-pythia6-tauola  bbA80  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-90_8TeV-pythia6-tauola  bbA90  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-100_8TeV-pythia6-tauola  bbA100  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-120_8TeV-pythia6-tauola  bbA120  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-130_8TeV-pythia6-tauola  bbA130  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-140_8TeV-pythia6-tauola  bbA140  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-160_8TeV-pythia6-tauola  bbA160  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-180_8TeV-pythia6-tauola  bbA180  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-200_8TeV-pythia6-tauola  bbA200  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-250_8TeV-pythia6-tauola  bbA250  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola  bbA300  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-350_8TeV-pythia6-tauola  bbA350  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-400_8TeV-pythia6-tauola  bbA400  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-450_8TeV-pythia6-tauola  bbA450  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-500_8TeV-pythia6-tauola  bbA500  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-600_8TeV-pythia6-tauola  bbA600  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-700_8TeV-pythia6-tauola  bbA700  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-800_8TeV-pythia6-tauola  bbA800  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-900_8TeV-pythia6-tauola  bbA900  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYBBHToTauTau_M-1000_8TeV-pythia6-tauola  bbA1000  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
############################################################################################################################################
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-80_8TeV-pythia6-tauola   ggH80  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-90_8TeV-pythia6-tauola   ggH90  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-100_8TeV-pythia6-tauola   ggH100  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-120_8TeV-pythia6-tauola   ggH120  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-130_8TeV-pythia6-tauola   ggH130  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-140_8TeV-pythia6-tauola   ggH140  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-160_8TeV-pythia6-tauola   ggH160  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-180_8TeV-pythia6-tauola   ggH180  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-200_8TeV-pythia6-tauola   ggH200  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-250_8TeV-pythia6-tauola   ggH250  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-300_8TeV-pythia6-tauola   ggH300  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-350_8TeV-pythia6-tauola   ggH350  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-400_8TeV-pythia6-tauola   ggH400  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-450_8TeV-pythia6-tauola   ggH450  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-500_8TeV-pythia6-tauola   ggH500  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-600_8TeV-pythia6-tauola   ggH600  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-700_8TeV-pythia6-tauola   ggH700  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-800_8TeV-pythia6-tauola   ggH800  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-900_8TeV-pythia6-tauola   ggH900  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 
farmoutAnalysisJobs  $1     --input-dir=/store/user/swanson/SUSYGluGluToHToTauTau_M-1000_8TeV-pythia6-tauola   ggH1000  $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/LTau/SUB-MCH.py 

