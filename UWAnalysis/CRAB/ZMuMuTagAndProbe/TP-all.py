

import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START52_V9::All'
process.load('Configuration/StandardSequences/Services_cff')
process.maxEvents = cms.untracked.PSet(
			input = cms.untracked.int32(-1)
			)


process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring( $inputFileNames
#	'/store/user/swanson/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Zjets_M50_2012-06-02-8TeV-078e4bc/ea74c25a04048a8dd7df6542c03c7a9b/output_99_1_ohb.root'	
#'/store/user/tapas/2012-07-18-8TeV-PatTuple/data_SingleMu_Run2012A_PromptReco_v1_Run190456_193683/1/patTuple_cfg-FE78C9F0-2688-E111-8765-001D09F2910A.root'
#'/store/user/tapas/2012-08-30-8TeV-PatTuple/data_SingleMu_Run2012C_PromptReco_v2_Run198934_201264/1/patTuple_cfg-863976F4-81E3-E111-82CC-BCAEC53296FB.root'
#'/store/user/tapas/2012-10-02-8TeV-53X-PatTuple_ShareFSFix/data_SingleMu_Run2012C_PromptReco_v2_Run198934_201264/patTuple_cfg-0C3C4F15-46DE-E111-A02B-0025901D5E10.root'
#'/store/user/tapas/2012-10-02-8TeV-53X-PatTuple_ShareFSFix/data_SingleMu_Run2012C_PromptReco_v2_Run198934_201264/patTuple_cfg-80548ADB-9EDE-E111-B86A-0019B9F70468.root'
#'file:/hdfs/store/user/tapas/SingleMu/Run2012D-PromptReco-v1/AOD/2013-01-11-8TeV-53X-PatTuple_Master/patTuple_cfg-FE00497A-6B39-E211-B6C7-5404A6388694.root'
#'file:/hdfs/store/user/tapas/SingleMu/Run2012D-PromptReco-v1/AOD/2013-01-11-8TeV-53X-PatTuple_Master/patTuple_cfg-FEF3113B-1324-E211-B5B5-485B3977172C.root'
			)
		
)
#process.load("PhysicsTools.PatAlgos.patSequences_cff")


from UWAnalysis.Configuration.tools.analysisTools import *
from UWAnalysis.Configuration.tools.analysisToolsPT import *
from UWAnalysis.Configuration.tools.analysisToolsPT import addTagAndProbePlotter
defaultReconstructionPT(process,'HLT',[
                                     'HLT_IsoMu24_eta2p1'
                                     ]
    )



#tagAndProbe 

process.load("UWAnalysis.Configuration.zMuMuTagAndProbe_cff")
process.tagAndProbe = cms.Path(process.tagAndProbeSequence)

process.probeMuons = cms.EDProducer("PATMuonEffectiveAreaEmbedder",
        src = cms.InputTag("triggeredPatMuons"),
        target = cms.string("2012Data"),# Available targets: Fal11MC, Summer11MC, 2011Data, 2012Data
        )
process.probeLeptons = cms.Path(process.probeMuons)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu4lT8',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],                  
                        ['pfCandidateRef().isNonnull()&&(isGlobalMuon()||isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.4'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8','hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu4lT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],                  
                        ['pfCandidateRef().isNonnull()&&(isGlobalMuon()||isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.4'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17','hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu4lT8dBetta',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],                  
                        ['pfCandidateRef().isNonnull()&&(isGlobalMuon()||isTrackerMuon())','abs(userFloat("ip3DS"))<4','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.4'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8','hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu2l2tauLooseT8',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.25'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8','hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu2l2tauLooseT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.25'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17','hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu2l2tauTightT8',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.15'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8','hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu2l2tauTightT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.15'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17','hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuZHLooseT8',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.25'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8','hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuZHLooseT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.25'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17','hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuZHTightT8',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.15'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8','hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuZHTightT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.15'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17','hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17']
)


addEventSummary(process,False,'summary','tagAndProbe')

process.source.inputCommands=cms.untracked.vstring(
                        'keep *', 'drop *_finalState*_*_*',
                        'drop *_patFinalStateEvent*_*_*'
)
process.TFileService.fileName=cms.string("$outputFileName")
