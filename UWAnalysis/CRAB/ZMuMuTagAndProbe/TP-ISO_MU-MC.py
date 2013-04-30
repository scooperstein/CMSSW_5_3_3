

import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START52_V9::All'
process.load('Configuration/StandardSequences/Services_cff')
process.maxEvents = cms.untracked.PSet(
			input = cms.untracked.int32(200)
			)


process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring( #$inputFileNames
#'/store/user/tapas/2012-10-02-8TeV-53X-PatTuple_ShareFSFix/data_SingleMu_Run2012C_PromptReco_v2_Run198934_201264/patTuple_cfg-0C3C4F15-46DE-E111-A02B-0025901D5E10.root'
'/store/user/tapas/2012-09-18-8TeV-53X-PatTuple/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/1/patTuple_cfg-FEF4E41A-46D4-E111-9594-0025B3E06424.root'
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

# IsoMu tags
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'IsoMu',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0&&abs(userFloat("dz"))<0.2&&abs(userFloat("ipDXY"))<0.045&&isTrackerMuon()&&eta()<2.1', '(userIso(0)+max(photonIso+neutralHadronIso()-0.5*puChargedHadronIso,0.0))/pt()<0.1'],                      
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10', 'hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoFiltered10' , 'hltL3crIsoL1sMu14erORMu16erL1f0L2f14QL3f17QL3crIsoRhoFiltered0p15']
)

# Non-IsoMu tags (prescaled)
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'NonIsoMuPS',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0&&abs(userFloat("dz"))<0.2&&abs(userFloat("ipDXY"))<0.045&&isTrackerMuon()&&eta()<2.1', '(userIso(0)+max(photonIso+neutralHadronIso()-0.5*puChargedHadronIso,0.0))/pt()<0.1'],
                        ['hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoFiltered10' , 'hltL3crIsoL1sMu14erORMu16erL1f0L2f14QL3f17QL3crIsoRhoFiltered0p15']
)

# Non-IsoMu tags (not prescaled)
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'NonIsoMu',
                        'probeMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','ISO'],                  
                        ['userInt("tightID")>0&&abs(userFloat("dz"))<0.2&&abs(userFloat("ipDXY"))<0.045&&isTrackerMuon&&eta()<2.1', '(userIso(0)+max(photonIso+neutralHadronIso()-0.5*puChargedHadronIso,0.0))/pt()<0.1'],
                        ['hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoFiltered10' , 'hltL3crIsoL1sMu14erORMu16erL1f0L2f14QL3f17QL3crIsoRhoFiltered0p15']
)

addEventSummary(process,False,'summary','tagAndProbe')

process.source.inputCommands=cms.untracked.vstring(
                        'keep *', 'drop *_finalState*_*_*',
                        'drop *_patFinalStateEvent*_*_*'
)
process.TFileService.fileName=cms.string("outputFileName.root")
