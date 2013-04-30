import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START52_V10::All'



from UWAnalysis.Configuration.tools.analysisToolsPT import *
defaultReconstructionPT(process,'EmbeddedRECO',
                      [
						"HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20",

                      ])

                      

#EventSelection
process.load("UWAnalysis.Configuration.LepTauAnalysis_cff")

process.metCalibration.applyCalibration = cms.bool(False)

process.eventSelectionET = cms.Path(process.selectionSequenceET)


#Systematic Shifts 1sigma
process.eventSelectionETTauUp    = createSystematics(process,process.selectionSequenceET,'TauUp',1.00,1.0,1.03,0,1.0)
process.eventSelectionETTauDown  = createSystematics(process,process.selectionSequenceET,'TauDown',1.0,1.0,0.97,0,1.0)
# process.eventSelectionETEleUp    = createSystematics(process,process.selectionSequenceET,'EleUp',1.01,1.0,1.03,0,1.0)
# process.eventSelectionETEleDown  = createSystematics(process,process.selectionSequenceET,'EleDown',0.99,1.0,0.97,0,1.0)


createGeneratedParticles(process,
                         'genDaughters',
                          [
                           "keep pdgId = 15",
                           "keep pdgId = -15"
                          ]
)





from UWAnalysis.Configuration.tools.ntupleToolsLTau import addEleTauEventTree
addEleTauEventTree(process,'eleTauEventTree')
addEleTauEventTree(process,'eleTauEventTreeFinal','eleTausOS','osDiElectrons')

addEventSummary(process,True,'ET','eventSelectionET')



addEleTauEventTree(process,'eleTauEventTreeTauUp','eleTausSortedTauUp','osDiElectronsTauUp')
addEleTauEventTree(process,'eleTauEventTreeTauDown','eleTausSortedTauDown','osDiElectronsTauDown')
addEleTauEventTree(process,'eleTauEventTreeFinalTauUp','eleTausOSTauUp','osDiElectronsTauUp')
addEleTauEventTree(process,'eleTauEventTreeFinalTauDown','eleTausOSTauDown','osDiElectronsTauDown')
# addEleTauEventTree(process,'eleTauEventTreeEleUp','eleTausSortedEleUp','osDiElectronsEleUp')
# addEleTauEventTree(process,'eleTauEventTreeEleDown','eleTausSortedEleDown','osDiElectronsEleDown')


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)



process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       $inputFileNames
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'drop *_finalState*_*_*',
						'drop *_patFinalStateEvent*_*_*'
		)
)


process.TFileService.fileName=cms.string("$outputFileName")

