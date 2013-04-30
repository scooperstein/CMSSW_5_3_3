import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR_R_52_V8::All'
process.load('Configuration/StandardSequences/Services_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       $inputFileNames
       #'/store/data/Run2011B/DoubleMu/AOD/PromptReco-v1/000/178/098/78673382-F6F5-E011-8431-BCAEC518FF69.root',
       #'/store/data/Run2011B/DoubleMu/AOD/PromptReco-v1/000/178/098/72FA2E53-DBF3-E011-8C39-BCAEC53296F4.root',
       #'/store/data/Run2011B/DoubleMu/AOD/PromptReco-v1/000/178/098/626E4CC3-CFF4-E011-B927-003048F1DBAE.root',
       #'/store/data/Run2011B/DoubleMu/AOD/PromptReco-v1/000/178/098/5AB6073B-AEF3-E011-9BD3-BCAEC5329724.root',
       #'/store/data/Run2011B/DoubleMu/AOD/PromptReco-v1/000/178/098/4E2882E1-81F3-E011-B7A6-001D09F29146.root',
       #'/store/data/Run2011B/DoubleMu/AOD/PromptReco-v1/000/178/098/42A8A5D7-CFF4-E011-958C-003048F01184.root',
       #'/store/data/Run2011B/DoubleMu/AOD/PromptReco-v1/000/178/098/400F3553-7FF3-E011-B6D0-BCAEC518FF8F.root',
       #'/store/data/Run2011B/DoubleMu/AOD/PromptReco-v1/000/178/098/28427520-F2F3-E011-8E6C-002481E0D90C.root',
       #'/store/user/tapas/2012-07-18-8TeV-PatTuple/data_SingleMu_Run2012B_PromptReco_v1_Run193752_196531/1/patTuple_cfg-10BC45C2-40AD-E111-A58A-485B3977172C.root '
       #'/store/user/tapas/2012-07-18-8TeV-PatTuple/data_SingleMu_Run2012B_PromptReco_v1_Run193752_196531/10/patTuple_cfg-000426AE-67B9-E111-BF18-0025901D629C.root'
        )
#,
       # inputCommands=cms.untracked.vstring(
        #                'keep *',
         #               'drop *_finalState*_*_*',
          #              'drop *_patFinalStateEvent*_*_*'
           #             )

)

#process.load("PhysicsTools.PatAlgos.patSequences_cff")


from UWAnalysis.Configuration.tools.analysisTools import *
from UWAnalysis.Configuration.tools.analysisToolsPT import *
defaultReconstructionPT(process,'HLT',['HLT_IsoMu12',
                                    'HLT_IsoMu24',
                                    'HLT_IsoMu24_eta2p1'
				  #  'HLT_IsoMu27_WP80',
	                	  #  'HLT_IsoMu17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50',
        		       	  #  'HLT_IsoMu20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50',
                                  #  'HLT_IsoMu32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50'

                                     ]
			)
#defaultReconstructionPT(process,'HLT',[
 #               'HLT_IsoMu27_WP80',
  #              'HLT_IsoMu17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50',
   #             'HLT_IsoMu20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50',
    #            'HLT_IsoMu32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50'
     #           ]

    #)


from UWAnalysis.Configuration.tools.analysisToolsPT import addTagAndProbePlotter

#tagAndProbe 

process.load("UWAnalysis.Configuration.zMuMuTagAndProbe_cff")
process.tagAndProbe = cms.Path(process.tagAndProbeSequence)

#from UWAnalysis.Configuration.tools.ntupleTools import *
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuonHttMu12',
                        'triggeredPatMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],
                        #['pt()>30','pt()>10000'],
			['pfCandidateRef().isNonnull()&(isGlobalMuon()|isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.25'],
			['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8','hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8','hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17','hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17']
#,'hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
#			['hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8']
)
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuonHttMu12GeV8',
                        'triggeredPatMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],
                        #['pt()>30','pt()>10000'],
                        ['pfCandidateRef().isNonnull()&(isGlobalMuon()|isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.25'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
                        ['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8','hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8']
#,'hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
)
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuonHttMu12GeV17',
                        'triggeredPatMuons',
                        'selectedTagAndProbeMuTracks',
                        ['ID','SIP','ISO'],
                        #['pt()>30','pt()>10000'],
                        ['pfCandidateRef().isNonnull()&(isGlobalMuon()|isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.25'],
                        ['hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q'],
                        ['hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17','hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17']
#,'hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
)

#addTagAndProbePlotter(process,'MuonTagAndProbePlotter',
 #                             'MuonHLTMu8ZZ',
  #                            'patMuonsForAnalysis',
   #                           'selectedTagAndProbeMuTracks',
    #                          ['ID','ISO'],
     #                         ['userFloat("isZZMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.25'],
      #                        ['hltSingleMuIsoL3IsoFiltered12','hltSingleMuIsoL3IsoFiltered24','hltL3IsoL1sMu14Eta2p1L1f0L2f14QL2IsoL3f24L3IsoFiltered'],
       #                       ['hltDiMuonL3PreFiltered8','hltDiMuonL3PreFiltered7','hltDiMuonL3p5PreFiltered8']

#)

#addTagAndProbePlotter(process,'MuonTagAndProbePlotter',
 #                             'MuonHLTMu13ZZ',
  #                            'patMuonsForAnalysis',
   #                           'selectedTagAndProbeMuTracks',
    #                          ['ID','ISO'],
     #                         ['userFloat("isZZMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.25'],
      #                        ['hltSingleMuIsoL3IsoFiltered24','hltL3IsoL1sMu14Eta2p1L1f0L2f14QL2IsoL3f24L3IsoFiltered'],
       #                       ['hltSingleMu13L3Filtered13']

#)
#addTagAndProbePlotter(process,'MuonTagAndProbePlotter',
 #                             'MuonHLTMu17ZZ',
  #                            'patMuonsForAnalysis',
   #                           'selectedTagAndProbeMuTracks',
    #                          ['ID','ISO'],
     #                         ['userFloat("isZZMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.25'],
      #                        ['hltL3IsoL1sMu14Eta2p1L1f0L2f14QL2IsoL3f24L3IsoFiltered'],
       #                       ['hltSingleMu13L3Filtered17']

#)

#addTagAndProbePlotter(process,'MuonTagAndProbePlotter',
 #                             'MuonZ2',
  #                            'patMuonsForAnalysis',
   #                           'selectedTagAndProbeMuTracks',
    #                          ['ID','ISO'],
     #                         ['userFloat("isZZMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.1'],
      #                        ['hltSingleMuIsoL3IsoFiltered12','hltSingleMuIsoL3IsoFiltered24','hltL3IsoL1sMu14Eta2p1L1f0L2f14QL2IsoL3f24L3IsoFiltered'],
       #                       ['hltDiMuonL3PreFiltered8','hltDiMuonL3PreFiltered7','hltDiMuonL3p5PreFiltered8']

#)

#addTagAndProbePlotter(process,'MuonTagAndProbePlotter',
 #                             'MuonHttL1_14',
  #                            'patMuonsForAnalysis',
   #                           'selectedTagAndProbeMuTracks',
    #                          ['WW','ISO'],
     #                         ['userFloat("isWWMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.1'],
      #                        ['hltL3IsoL1sMu14Eta2p1L1f0L2f14QL2IsoL3f24L3IsoFiltered'],
       #                       ['hltSingleMuIsoL1s14L3IsoFiltered15eta2p1']
                       
#)

#addTagAndProbePlotter(process,'MuonTagAndProbePlotter',
 #                             'MuonHttMu12',
  #                            'patMuonsForAnalysis',
   #                           'selectedTagAndProbeMuTracks',
    #                          ['WW','ISO'],
     #                         ['userFloat("isWWMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.1'],
      #                        ['hltSingleMuIsoL3IsoFiltered12'],
       #                       ['hltSingleMuIsoL3IsoFiltered12']

                       
#)

#addTagAndProbePlotter(process,'MuonTagAndProbePlotter',
 #                             'MuonHttMu15',
  #                            'patMuonsForAnalysis',
   #                           'selectedTagAndProbeMuTracks',
    #                          ['WW','ISO'],
     #                         ['userFloat("isWWMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.1'],
      #                        ['hltSingleMuIsoL3IsoFiltered24'],
       #                       ['hltSingleMuIsoL3IsoFiltered15']

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
