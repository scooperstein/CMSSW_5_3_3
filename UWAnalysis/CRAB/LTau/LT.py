import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_P_V41_AN1::All'

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)



process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       '/store/user/tapas/2012-08-23-8TeV-PatTuple/data_TauPlusX_Run2012C_PromptReco_v2_Run198934_201264/1/patTuple_cfg-5269D888-7ADA-E111-90A9-BCAEC532970F.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'drop *_finalState*_*_*',
						'drop *_patFinalStateEvent*_*_*'
		)
)


from UWAnalysis.Configuration.tools.analysisToolsPT import *
defaultReconstructionPT(process,'HLT',
                      [
						"HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20",
						"HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20",
						"HLT_IsoMu18_eta2p1_LooseIsoPFTau20",
						"HLT_IsoMu17_eta2p1_LooseIsoPFTau20"
                      ])

                      

#EventSelection
process.load("UWAnalysis.Configuration.LepTauAnalysis_cff")

process.eventSelectionMT = cms.Path(process.selectionSequenceMT)
process.eventSelectionET = cms.Path(process.selectionSequenceET)

from UWAnalysis.Configuration.tools.ntupleToolsPT import addMuTauEventTree
addMuTauEventTree(process,'muTauEventTree')
addMuTauEventTree(process,'muTauEventTreeIso','diTausLooseTauIsolation','diMuonsSorted')
addMuTauEventTree(process,'muTauEventTreeFinal','diTausOS','diMuonsSorted')

from UWAnalysis.Configuration.tools.ntupleToolsPT import addEleTauEventTree
addEleTauEventTree(process,'eleTauEventTree')
addEleTauEventTree(process,'eleTauEventTreeIso','eleTausLooseIsolation','osDiElectrons')
addEleTauEventTree(process,'eleTauEventTreeFinal','eleTausOS','osDiElectrons')

addEventSummary(process,False,'MT','eventSelectionMT')
addEventSummary(process,False,'ET','eventSelectionET')
