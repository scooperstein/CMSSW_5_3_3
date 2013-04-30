

import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START52_V9::All'
process.load('Configuration/StandardSequences/Services_cff')
process.maxEvents = cms.untracked.PSet(
			input = cms.untracked.int32(-1)
			)


process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(  $inputFileNames
#	'/store/user/swanson/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Zjets_M50_2012-06-02-8TeV-078e4bc/ea74c25a04048a8dd7df6542c03c7a9b/output_99_1_ohb.root'	
#'/store/user/tapas/2012-09-18-8TeV-53X-PatTuple/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/1/patTuple_cfg-FEF4E41A-46D4-E111-9594-0025B3E06424.root'
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
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu4lT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],                  
                        ['pfCandidateRef().isNonnull()&&(isGlobalMuon()||isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.4'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu4lT8dBetta',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],                  
                        ['pfCandidateRef().isNonnull()&&(isGlobalMuon()||isTrackerMuon())','abs(userFloat("ip3DS"))<4','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.4'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu2l2tauLooseT8',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.25'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu2l2tauLooseT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.25'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu2l2tauTightT8',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.15'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'Mu2l2tauTightT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("effArea")))/pt()<0.15'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuZHLooseT8',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.25'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuZHLooseT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.25'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuZHTightT8',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.15'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8']
)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuZHTightT17',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0','(userIso(0)+max(0.0,userIso(1)+neutralHadronIso()-0.5*userIso(2)))/pt()<0.15'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
)


addEventSummary(process,False,'summary','tagAndProbe')

process.source.inputCommands=cms.untracked.vstring(
                        'keep *', 'drop *_finalState*_*_*',
                        'drop *_patFinalStateEvent*_*_*'
)
process.TFileService.fileName=cms.string("$outputFileName")
