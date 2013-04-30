import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START52_V10::All'

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)



process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       '/store/user/friis/DoubleMu/embedded_2012A_mutau_2012-05-29-8TeV-PatTuple-v5-c9b7dbb/8abec6319d88c45f391ca5c79f24387e/output_9_1_wcb.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'drop *_finalState*_*_*',
						'drop *_patFinalStateEvent*_*_*'
		)
)


from UWAnalysis.Configuration.tools.analysisToolsPT import *
defaultReconstructionPT(process,'EmbeddedRECO',
                      [
						"HLT_IsoMu18_eta2p1_LooseIsoPFTau20",
						"HLT_IsoMu15_eta2p1_L1ETM20"
                      ])

                      

#EventSelection
process.load("UWAnalysis.Configuration.LepTauAnalysis_cff")

process.metCalibration.applyCalibration = cms.bool(False)

process.eventSelectionMT = cms.Path(process.selectionSequenceMT)


#Systematic Shifts 1sigma
process.eventSelectionMTTauUp    = createSystematics(process,process.selectionSequenceMT,'TauUp',1.00,1.0,1.03,0,1.0)
process.eventSelectionMTTauDown  = createSystematics(process,process.selectionSequenceMT,'TauDown',1.0,1.0,0.97,0,1.0)
# process.eventSelectionMTJetUp    = createSystematics(process,process.selectionSequenceMT,'JetUp',1.00,1.0,1.0,1,1.0)
# process.eventSelectionMTJetDown  = createSystematics(process,process.selectionSequenceMT,'JetDown',1.0,1.0,1.0,-1,1.0)
# process.eventSelectionMTUncUp    = createSystematics(process,process.selectionSequenceMT,'UncUp',1.00,1.0,1.0,0,1.1)
# process.eventSelectionMTUncDown  = createSystematics(process,process.selectionSequenceMT,'UncDown',1.0,1.0,1.0,0,0.9)


createGeneratedParticles(process,
                         'genDaughters',
                          [
                           "keep pdgId = 15",
                           "keep pdgId = -15"
                          ]
)


from UWAnalysis.Configuration.tools.ntupleToolsPT import addMuTauEventTree
addMuTauEventTree(process,'muTauEventTree')
addMuTauEventTree(process,'muTauEventTreeFinal','diTausOS','diMuonsSorted')

addEventSummary(process,True,'MT','eventSelectionMT')



#Final trees afor shapes after shifts
addMuTauEventTree(process,'muTauEventTreeTauUp','diTausSortedTauUp','diMuonsSortedTauUp')
addMuTauEventTree(process,'muTauEventTreeTauDown','diTausSortedTauDown','diMuonsSortedTauDown')
addMuTauEventTree(process,'muTauEventTreeFinalTauUp','diTausOSTauUp','diMuonsSortedTauUp')
addMuTauEventTree(process,'muTauEventTreeFinalTauDown','diTausOSTauDown','diMuonsSortedTauDown')
# addMuTauEventTree(process,'muTauEventTreeJetUp','diTausTauMuonVetoJetUp','diMuonsSortedJetUp')
# addMuTauEventTree(process,'muTauEventTreeJetDown','diTausTauMuonVetoJetDown','diMuonsSortedJetDown')
# addMuTauEventTree(process,'muTauEventTreeUncUp','diTausTauMuonVetoUncUp','diMuonsSortedUncUp')
# addMuTauEventTree(process,'muTauEventTreeUncDown','diTausTauMuonVetoUncDown','diMuonsSortedUncDown')
