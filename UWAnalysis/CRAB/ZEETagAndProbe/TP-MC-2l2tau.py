
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START52_V10::All'

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( $inputFileNames
#'file:/hdfs/store/user/tapas/2012-08-30-8TeV-PatTuple/data_SingleElectron_Run2012C_PromptReco_v2_Run198934_201264/1/patTuple_cfg-803ECF43-34D5-E111-A1D0-E0CB4E5536AE.root'
    	#'file:/hdfs/store/user/swanson/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Zjets_M50_2012-06-02-8TeV-078e4bc/ea74c25a04048a8dd7df6542c03c7a9b/output_145_1_QvD.root'       
#         'file:/hdfs/store/user/cepeda/SingleElectron/data_SingleElectron_Run2012A_PromptReco_v1_2012-05-29-8TeV-PatTuple-67c1f94/a7f10efca7dd683ad59c7e946715fa59/output_555_1_6eN.root'
#          'file:/hdfs/store/user/cepeda/SingleElectron/data_SingleElectron_Run2012A_PromptReco_v1_2012-05-29-8TeV-PatTuple-67c1f94/a7f10efca7dd683ad59c7e946715fa59/output_323_1_S80.root'
#           'file:/hdfs/store/user/cepeda/SingleElectron/data_SingleElectron_Run2012A_PromptReco_v1_2012-05-29-8TeV-PatTuple-67c1f94/a7f10efca7dd683ad59c7e946715fa59/output_180_1_Clc.root'
#         'file:/hdfs/store/user/cepeda/SingleElectron/data_SingleElectron_Run2012B_PromptReco_v1_a_2012-05-29-8TeV-PatTuple-67c1f94/a7f10efca7dd683ad59c7e946715fa59/output_299_1_mGd.root'
#          'file:/hdfs/store/user/iross/DoubleElectron/data_DoubleElectron_Run2012A_PromptReco_v1_2012-06-08-8TeV-PatTuple-data-4495432/c7a1c2223886075833473549ad1960ce/output_178_1_WXE.root'
#'/store/user/tapas/2012-09-18-8TeV-53X-PatTuple/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/1/patTuple_cfg-FEF4E41A-46D4-E111-9594-0025B3E06424.root'
#'/store/user/tapas/2012-09-18-8TeV-53X-PatTuple/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/1/patTuple_cfg-FEF4E41A-46D4-E111-9594-0025B3E06424.root'
        ),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'drop *_finalState*_*_*',
						'drop *_patFinalStateEvent*_*_*'
		)
)

process.load("PhysicsTools.PatAlgos.patSequences_cff")


from UWAnalysis.Configuration.tools.analysisToolsPT import *
defaultReconstructionPT(process,'HLT',[
    'HLT_Ele27_WP80',
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50',
    'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50',
    'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50',
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL'
    ])



#tagAndProbe 

process.load("UWAnalysis.Configuration.zEETagAndProbe_cff")


process.tagAndProbe = cms.Path(process.tagAndProbeSequence)

from UWAnalysis.Configuration.tools.ntupleToolsPT import * 

#the first is a test from the MC
#addTagAndProbePlotter(process,'ElectronTrackTagAndProbePlotter',
#                              'electronHtt152',
#                              'triggeredPatElectrons',
#                              'tagAndProbeEleTracks',
#                              ['WWID','ISO'],
#                              ['(abs(eta())<0.8 && electronID("mvaNonTrigV0")>0.5) || (abs(eta())<1.479 && abs(eta())>0.8 && electronID("mvaNonTrigV0")>0.12) ||  (abs(eta())>1.479 && electronID("mvaNonTrigV0")>0.6)','(userIso(0)+max(0.0, userIso(1)+neutralHadronIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.25'],
#                              ['hltEle27WP80TrackIsoFilter'],
#                              ['hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsolFilter']
#
#
#)
addTagAndProbePlotter(process,'ElectronTagAndProbePlotter',
                              'electron2ltau17GeVTriggerLoose',
                              'triggeredPatElectrons',
                              'selectedTagAndProbeDiElectrons',
                              ['MVAID','ISO'],
                              ['(abs(superCluster().eta())<0.8 && electronID("mvaNonTrigV0")>0.5) || (abs(superCluster().eta())<1.479 && abs(superCluster().eta())>0.8 && electronID("mvaNonTrigV0")>0.12) ||  (abs(eta())>1.479 && electronID("mvaNonTrigV0")>0.6)','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.25'],
                              ['hltEle27WP80TrackIsoFilter'],
                              ['hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoFilter']# 17 GeV leg

)

addTagAndProbePlotter(process,'ElectronTagAndProbePlotter',
                              'electron2ltau17GeVTriggerTight',
                              'triggeredPatElectrons',
                              'selectedTagAndProbeDiElectrons',
                              ['MVAID','ISO'],
                              ['(abs(superCluster().eta())<0.8 && electronID("mvaNonTrigV0")>0.5) || (abs(superCluster().eta())<1.479 && abs(superCluster().eta())>0.8 && electronID("mvaNonTrigV0")>0.12) ||  (abs(eta())>1.479 && electronID("mvaNonTrigV0")>0.6)','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.10'],
                              ['hltEle27WP80TrackIsoFilter'],
                              ['hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoFilter']# 17 GeV leg

)

addTagAndProbePlotter(process,'ElectronTagAndProbePlotter',
                              'electron2l2t8GeVTriggerLoose',
                              'triggeredPatElectrons',
                              'selectedTagAndProbeDiElectrons',
                              ['MVAID','ISO'],
                              ['(abs(superCluster().eta())<0.8 && electronID("mvaNonTrigV0")>0.5) || (abs(superCluster().eta())<1.479 && abs(superCluster().eta())>0.8 && electronID("mvaNonTrigV0")>0.12) ||  (abs(eta())>1.479 && electronID("mvaNonTrigV0")>0.6)','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.25'],
                              ['hltEle27WP80TrackIsoFilter'],
                              ['hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoDoubleFilter']# 8 GeV leg

)

addTagAndProbePlotter(process,'ElectronTagAndProbePlotter',
                              'electron2l2t8GevTriggerTight',
                              'triggeredPatElectrons',
                              'selectedTagAndProbeDiElectrons',
                              ['MVAID','ISO'],
                              ['(abs(superCluster().eta())<0.8 && electronID("mvaNonTrigV0")>0.5) || (abs(superCluster().eta())<1.479 && abs(superCluster().eta())>0.8 && electronID("mvaNonTrigV0")>0.12) ||  (abs(eta())>1.479 && electronID("mvaNonTrigV0")>0.6)','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.10'],
                              ['hltEle27WP80TrackIsoFilter'],
                              ['hltEle17TightIdLooseIsoEle8TightIdLooseIsoTrackIsoDoubleFilter']# 8 GeV leg

)


#addTagAndProbePlotter(process,'ElectronTagAndProbePlotter',
#                              'electronHtt15',
#                              'triggeredPatElectrons',
#                              'tagAndProbeDiElectrons',
#                              ['WWID','ISO'],
#                              ['userFloat("WWID")>0','(chargedHadronIso+max(0.0,neutralHadronIso+photonIso-0.5*puChargedHadronIso))/pt()<0.1'],
#                              ['hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1IsoEG18OrEG20'],
#                              ['hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1IsoEG18OrEG20']
#
#
#)
#addTagAndProbePlotter(process,'ElectronTrackTagAndProbePlotter',
#                              'electronHtt152',
#                              'triggeredPatElectrons',
#                              'tagAndProbeEleTracks',
#                              ['WWID','ISO'],
#                              ['userFloat("WWID")>0','(chargedHadronIso+max(0.0,neutralHadronIso+photonIso-0.5*puChargedHadronIso))/pt()<0.1'],
#                              ['hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1IsoEG18OrEG20'],
#                              ['hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1IsoEG18OrEG20']
#
#
#)
# addTagAndProbePlotter(process,'ElectronSCTagAndProbePlotter',
#                               'electron2l2t17L',
#                               'triggeredPatElectrons',
#                               'selectedTagAndProbeEleSCs',
#                               ['WWID','ISO'],
#                               ['userFloat("WWID")>0','(chargedHadronIso+max(0.0,neutralHadronIso+photonIso-0.5*puChargedHadronIso))/pt()<0.1'],
#                               ['hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1IsoEG18OrEG20'],
#                               ['hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1IsoEG18OrEG20']
# )
# addTagAndProbePlotter(process,'ElectronSCTagAndProbePlotter',
#                               'electron2l2t8L',
#                               'convRejElectrons',
#                               'selectedTagAndProbeEleSCs',
#                               ['CIC','ISO'],
#                               ['gsfTrack().trackerExpectedHitsInner().numberOfHits()<2&&(electronID("cicTight")==1||electronID("cicTight")==3||electronID("cicTight")==5||electronID("cicTight")==7||electronID("cicTight")==9||electronID("cicTight")==11||electronID("cicTight")==13||electronID("cicTight")==15)','(chargedHadronIso+max(0.0,neutralHadronIso+photonIso-0.5*particleIso))/pt()<0.25'],
#                               ['hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8TrackIsolFilter','hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTEle8TrackIsolFilter'],
#                               ['hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter','hltEle8CaloIdLCaloIsoVLPixelMatchFilter']
#                                                             
# )
# 
# 
# 
# addTagAndProbePlotter(process,'ElectronSCTagAndProbePlotter',
#                               'electronNuJetISOPF',
#                               'convRejElectrons',
#                               'selectedTagAndProbeEleSCs',
#                               ['IDL','ISOPF'],
#                               ['((isEB &&sigmaIetaIeta<0.01&&abs(deltaPhiSuperClusterTrackAtVtx)<0.03&& abs(deltaEtaSuperClusterTrackAtVtx)<0.004 ) || (isEE &&sigmaIetaIeta<0.03&&abs(deltaPhiSuperClusterTrackAtVtx)<0.02 && abs(deltaEtaSuperClusterTrackAtVtx)<0.005))&& hcalOverEcal()<0.025 && abs(dB())<0.02 && (gsfTrack.trackerExpectedHitsInner.numberOfHits==0 && !(-0.02<convDist<0.02 && -0.02<convDcot<0.02)) ','(chargedHadronIso()+max(photonIso()+neutralHadronIso()-userFloat("rho")*3.14*0.4*0.4,0.0))/pt()<0.05'],
#                       # This ID is equivalent to wp70, but it is not configured in the default analysisTools,
#                               ['hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8TrackIsolFilter','hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTEle8TrackIsolFilter'],
#                               ['hltEle32WP70PFMT50PFMTFilter','hltEle27WP80PFMT50PFMTFilter','hltEle27WP80PFMT50PFMTFilter','hltEle32WP80PFMT50PFMTFilter']
# )
# 
# 
# addTagAndProbePlotter(process,'ElectronSCTagAndProbePlotter',
#                               'electronNuJetISORel',
#                               'convRejElectrons',
#                               'selectedTagAndProbeEleSCs',
#                               ['IDL','ISOPF'],
#                               ['((isEB &&sigmaIetaIeta<0.01&&abs(deltaPhiSuperClusterTrackAtVtx)<0.03&& abs(deltaEtaSuperClusterTrackAtVtx)<0.004 ) || (isEE &&sigmaIetaIeta<0.03&&abs(deltaPhiSuperClusterTrackAtVtx)<0.02 && abs(deltaEtaSuperClusterTrackAtVtx)<0.005))&& hcalOverEcal()<0.025 && abs(dB())<0.02 && (gsfTrack.trackerExpectedHitsInner.numberOfHits==0 && !(-0.02<convDist<0.02 && -0.02<convDcot<0.02)) ','(dr03TkSumPt()+max(0,dr03EcalRecHitSumEt()+dr03HcalTowerSumEt()-userFloat("rho")*3.14*0.3*0.3))/pt()<0.05'],
#                       # This ID is equivalent to wp70, but it is not configured in the default analysisTools,
#                               ['hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8TrackIsolFilter','hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTEle8TrackIsolFilter'],
#                               ['hltEle32WP70PFMT50PFMTFilter','hltEle27WP80PFMT50PFMTFilter','hltEle27WP80PFMT50PFMTFilter','hltEle32WP80PFMT50PFMTFilter']
# )


# addTagAndProbePlotter(process,'ElectronMisIDTagAndProbePlotter',
#                               'TauMisID',
#                               'patOverloadedTaus',
#                               'selectedTagAndProbeEleTracks',
#                               ['DM','ISO','ELEVETO'],
#                               ['tauID("decayModeFinding")>0.5','tauID("byLooseIsolation")>0.5','tauID("againstElectronTight")>0.5'],
#                               ['hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8TrackIsolFilter','hltEle32CaloIdTCaloIsoTTrkIdTTrkIsoTTrackIsoFilter'],
#                               ['hltOverlapFilterIsoEle15IsoPFTau15','hltOverlapFilterIsoEle18IsoPFTau20']
# 
# )





#process.TFileService.fileName=cms.string("$outputFileName")


addEventSummary(process,False,'summary','tagAndProbe')











