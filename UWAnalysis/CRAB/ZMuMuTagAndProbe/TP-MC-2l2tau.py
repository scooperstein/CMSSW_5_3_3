

import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START52_V9::All'
process.load('Configuration/StandardSequences/Services_cff')
process.maxEvents = cms.untracked.PSet(
			input = cms.untracked.int32(-1)
			)


process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
		$inputFileNames
#'/store/user/tapas/2012-08-30-8TeV-PatTuple/data_SingleMu_Run2012C_PromptReco_v2_Run198934_201264/1/patTuple_cfg-108EDD4A-A3E4-E111-8FC8-003048F024FA.root'
#   '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F441FDD0-BB76-E011-AEA9-003048D3C7BC.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F2C4477C-C276-E011-BC02-0025901D4938.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F2AD28E1-CA76-E011-ABF4-0025901D4AF0.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F283DFF0-C976-E011-AC41-003048D4393E.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F27CA45F-CF76-E011-A04A-002481E0DC66.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F0F98170-F276-E011-9277-00266CF32920.root',
#  '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F0C6F93A-CF76-E011-BD04-003048F0E188.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F0895ABE-EB76-E011-B1AD-0025901D4124.root',
#	'/store/user/swanson/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Zjets_M50_2012-06-02-8TeV-078e4bc/ea74c25a04048a8dd7df6542c03c7a9b/output_99_1_ohb.root'	
#'/store/user/tapas/2012-09-18-8TeV-53X-PatTuple/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/1/patTuple_cfg-FEF4E41A-46D4-E111-9594-0025B3E06424.root'			)
		
)
#process.load("PhysicsTools.PatAlgos.patSequences_cff")


from UWAnalysis.Configuration.tools.analysisTools import *
from UWAnalysis.Configuration.tools.analysisToolsPT import *
#defaultReconstructionPT(process,'HLT',[
	#	'HLT_IsoMu27_WP80',
	#	'HLT_IsoMu17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50',
	#	'HLT_IsoMu20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50',
	#	'HLT_IsoMu32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50'
	#	])
from UWAnalysis.Configuration.tools.analysisToolsPT import addTagAndProbePlotter
defaultReconstructionPT(process,'HLT',['HLT_IsoMu12',
                                     'HLT_IsoMu24',
                                     ]
    )



#tagAndProbe 

process.load("UWAnalysis.Configuration.zMuMuTagAndProbe_cff")
process.tagAndProbe = cms.Path(process.tagAndProbeSequence)





addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuonHttMu12GeV8Loose',
                        'triggeredPatMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],                  
                        ['pfCandidateRef().isNonnull()&&(isGlobalMuon()||isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.25'],
                        ['hltL3crIsoL1sMu16Eta2p4L1f0L2f16QL3f24QL3crIsoFiltered10'],
                        ['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8']
)
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuonHttMu12GeV8Tight',
                        'triggeredPatMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],                  
                        ['pfCandidateRef().isNonnull()&&(isGlobalMuon()||isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.15'],
                        ['hltL3crIsoL1sMu16Eta2p4L1f0L2f16QL3f24QL3crIsoFiltered10'],
                        ['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8']
)
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuonHttMu12GeV17Loose',
                        'triggeredPatMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],                   
                        ['pfCandidateRef().isNonnull()&&(isGlobalMuon()||isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.25'],
                        ['hltL3crIsoL1sMu16Eta2p4L1f0L2f16QL3f24QL3crIsoFiltered10'],
                        ['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
)
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuonHttMu12GeV17Tight',
                        'triggeredPatMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],                   
                        ['pfCandidateRef().isNonnull()&&(isGlobalMuon()||isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.15'],
                        ['hltL3crIsoL1sMu16Eta2p4L1f0L2f16QL3f24QL3crIsoFiltered10'],
                        ['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
)

# addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
#                               'MuonID',
#                               'patMuonsForAnalysis',
#                               'selectedTagAndProbeMuTracks',
#                               ['WW','ISO'],
#                               ['userFloat("isWWMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.1'],
#                               ['hltSingleMuIsoL3IsoFiltered24'],
#                               ['hltSingleMuIsoL3IsoFiltered24']
#                        
# )
# 
# addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
#                               'MuonHLTIsoMu12',
#                               'patMuonsForAnalysis',
#                               'selectedTagAndProbeMuTracks',
#                               ['WW','ISO'],
#                               ['userFloat("isWWMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.1'],
#                               ['hltSingleMuIsoL3IsoFiltered12'],
#                               ['hltSingleMuIsoL3IsoFiltered12']
# 
#                        
# )
# 
# 
# addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
#                               'MuonHLTIsoMu15',
#                               'patMuonsForAnalysis',
#                               'selectedTagAndProbeMuTracks',
#                               ['WW','ISO'],
#                               ['userFloat("isWWMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.1'],
#                               ['hltSingleMuIsoL3IsoFiltered24'],
#                               ['hltSingleMuIsoL3IsoFiltered15']
# 
# )

#addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',		 
#                              'MuonHLTMu8ZZ',			 
 #                             'patMuonsForAnalysis', 		 
  #                            'selectedTagAndProbeMuTracks',	 
   #                           ['ID','ISO'],			
    #                          ['userFloat("isZZMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.25'],  
     #                         ['hltSingleMuIsoL3IsoFiltered12','hltSingleMuIsoL3IsoFiltered24'], 						
      #                        ['hltDiMuonL3PreFiltered8','hltDiMuonL3PreFiltered7'] 								

#)

# 
# addTagAndProbePlotter(process,'MuonMisIDTagAndProbePlotter',
#                               'TauMisID',
#                               'patOverloadedTaus',
#                               'selectedTagAndProbeMuTracks',
#                               ['DM','ISO','MUVETO'],
#                               ['tauID("decayModeFinding")>0.5','isolationPFChargedHadrCandsPtSum()+max(0.0,isolationPFGammaCandsEtSum()-0.35*particleIso())<2.0','tauID("againstMuonTight")>0.5'],
#                               ['hltSingleMuIsoL3IsoFiltered24'],
#                               ['hltOverlapFilterIsoMu15IsoPFTau15','hltOverlapFilterIsoMu12IsoPFTau10']
# )
addEventSummary(process,False,'summary','tagAndProbe')

process.source.inputCommands=cms.untracked.vstring(
                        'keep *', 'drop *_finalState*_*_*',
                        'drop *_patFinalStateEvent*_*_*'
)
process.TFileService.fileName=cms.string("$outputFileName")
