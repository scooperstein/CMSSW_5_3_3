

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
#   '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F441FDD0-BB76-E011-AEA9-003048D3C7BC.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F2C4477C-C276-E011-BC02-0025901D4938.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F2AD28E1-CA76-E011-ABF4-0025901D4AF0.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F283DFF0-C976-E011-AC41-003048D4393E.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F27CA45F-CF76-E011-A04A-002481E0DC66.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F0F98170-F276-E011-9277-00266CF32920.root',
#  '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F0C6F93A-CF76-E011-BD04-003048F0E188.root',
# '/store/mc/Summer11/DYToMuMu_M-20_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v1/0000/F0895ABE-EB76-E011-B1AD-0025901D4124.root',
#	'/store/user/swanson/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Zjets_M50_2012-06-02-8TeV-078e4bc/ea74c25a04048a8dd7df6542c03c7a9b/output_99_1_ohb.root'	
#'/store/user/tapas/2012-09-18-8TeV-53X-PatTuple/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/1/patTuple_cfg-FEF4E41A-46D4-E111-9594-0025B3E06424.root'	
		)
		
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


#addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
#                             'MuonHLTMu8ZZ',
#                            'triggeredPatMuons',
#                           'selectedTagAndProbeMuTracks',
#                          ['ID','ISO'],
# ['userFloat("isZZMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.25']
#				[''],
#    ['hltSingleMuIsoL3IsoFiltered12','hltSingleMuIsoL3IsoFiltered24'],
#				[''],
#                             ['hltDiMuonL3PreFiltered8','hltDiMuonL3PreFiltered7']

#)

#addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
#                             'MuonZ2',
#                            'triggeredPatMuons',
#                           'selectedTagAndProbeMuTracks',
#                          ['ID','ISO'],
# ['userFloat("isZZMuon")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.1']
#				[''],
#  ['hltSingleMuIsoL3IsoFiltered12','hltSingleMuIsoL3IsoFiltered24','hltL3IsoL1sMu14Eta2p1L1f0L2f14QL2IsoL3f24L3IsoFiltered'],
#				[''],
#                             ['hltDiMuonL3PreFiltered8','hltDiMuonL3PreFiltered7','hltDiMuonL3p5PreFiltered8']

#)

addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
			'MuonHttMu12',
			'triggeredPatMuons',
			'selectedTagAndProbeMuTracks',
			#['WW','ISO','tightID'],
			['ID','SIP','ISO'],
			#['pt()>30','pt()>10000'],
 			#['userInt("WWID")>0.5','(userIso(0)+max(photonIso()+neutralHadronIso()-0.5*puChargedHadronIso,0.0))/pt() < 0.1', 'userInt("tightID") >0.5'],			
                        ['pfCandidateRef().isNonnull()&(isGlobalMuon()|isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.40'],

#['userInt("WWID")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(2),0.0))/pt()<0.1'],
	#		['hltBLifetimeL3PFFilterSingleTop','hltIsoMu202p1CentralPFJet30MuCleaned','hltIsoMu20eta2p1CentralPFJet80MuCleaned','hltBLifetimeL3PFNoPUFilterSingleTop','hltIsoMu202p1CentralPFNoPUJet30MuCleaned','hltIsoMu202p1DiCentralPFJet30MuCleaned','hltIsoMu202p1DiCentralPFNoPUJet30MuCleaned','hltIsoMu202p1TriCentralPFJet30MuCleaned','hltIsoMu202p1CentralPFJet50MuCleaned','hltIsoMu202p1TriCentralPFNoPUJet30MuCleaned','hltIsoMu202p1CentralPFNoPUJet50MuCleaned','hlt2IsoMu20eta2p1PFMHTPt80','hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f20L3crIsoFiltered10','hltPFMHT20Filter','hltIsoMu24eta2p1DiCentralPFJet25MuCleaned','hltIsoMu24eta2p1PFJet30PFJet25Deta3PFJetCollectionsVBFFilter','hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10','hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f30QL3crIsoFiltered10','hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f34QL3crIsoFiltered10','hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f40QL3crIsoFiltered10','hltPFMHT55Filter','hltPFMHT60Filter','hltL3L1Mu10erJetC20JetC12Corr1OrL1Mu10erJetC32OrMu10erJetC32JetC12Corr1L3Mufiltered12Eta2p1','hltBLifetime3D1stTrkL3FilterJet20HbbL1FastJet','hltDiBLifetime3D1stTrkL3FilterJet20HbbL1FastJet','hltL3L1Mu10erJetC20JetC12Corr1OrL1Mu10erJetC32OrMu10erJetC32JetC12Corr1L3Mufiltered12Eta2p1','hltL3L1Mu10erJetC20JetC12Corr1OrL1Mu10erJetC32OrMu10erJetC32JetC12Corr1L3Mufiltered12Eta2p1','hltL3fL1sMu7L3Filtered12','hltBLifetime3D1stTrkL3FilterJet20HbbL1FastJet','hltDiBLifetime3D1stTrkL3FilterJet20HbbL1FastJet','hltL1Mu10Eta2p1Jet20Jet12CentralCorrOrMu10erJetC32L3Mufiltered15Eta2p1','hltL3fL1sMu7L1fEta2p1L2fEta2p1f7L3FilteredEta2p1Filtered15','hltBLifetimeL3PFFilterSingleTopNoIso','hltBLifetimeL3PFNoPUFilterSingleTopNoIso','hltMu202p1TriCentralPFJet30MuCleaned','hltMu202p1CentralPFJet50MuCleaned','hltMu202p1TriCentralPFNoPUJet30MuCleaned','hltMu202p1CentralPFNoPUJet50MuCleaned','hltMu24eta2p1DiCentralPFJet25MuCleaned','hltMu24eta2p1PFJet30PFJet25Deta3PFJetCollectionsVBFFilter','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered30Q','hltDeDxFilter50DEDX3p6Mu','hltDeDxFilter60DEDX3p7Mu','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q','hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered50Q','hltL3fL1sMu3L3Filtered5','hltL3reliso1p0mufiltermu17','hltL3reliso1p0mufiltermu5'],
			['hltL3crIsoL1sMu16Eta2p4L1f0L2f16QL3f24QL3crIsoFiltered10'],
                        #['hltSingleMuIsoL3IsoFiltered12'],
			
			#['hltSingleMuIsoL3IsoFiltered12']
			#['hltDoubleMu11ExclL3PreFiltered','hltDoubleMu4ExclL3PreFiltered','hltDoubleMu5IsoMu5IsoL3IsoFiltered5','hltL2DoubleMu23NoVertexL2Filtered2ChaAngle2p5','hltL2DoubleMu23NoVertexL2PreFiltered','hltL2DoubleMu38NoVertexL2Filtered2ChaAngle2p5','hltDiMuonMu17Mu8DzFiltered0p2','hltDiMuonGlb17Trk8DzFiltered0p2','hltL3fL1sMu12L3Filtered17','hltDiMuonGlb22Trk22DzFiltered0p2','hltDiMuonGlb22Trk8DzFiltered0p2','hltL3fL1sMu3L3Filtered8','hltTripleMu0L3TriMuFiltered5']	
			['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8','hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']
#,'hltL3fL1DoubleMu10MuOpenL1f0L2f10L3Filtered17']

)
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuonHttMu12GeV8',
                        'triggeredPatMuons',
                        'selectedTagAndProbeMuTracks',
                        #['WW','ISO','tightID'],
                        ['ID','SIP','ISO'],
                        #['pt()>30','pt()>10000'],
                        #['userInt("WWID")>0.5','(userIso(0)+max(photonIso()+neutralHadronIso()-0.5*puChargedHadronIso,0.0))/pt() < 0.1', 'userInt("tightID") >0.5'],                   
                        ['pfCandidateRef().isNonnull()&(isGlobalMuon()|isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.40'],

#['userInt("WWID")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(2),0.0))/pt()<0.1'],
                        ['hltL3crIsoL1sMu16Eta2p4L1f0L2f16QL3f24QL3crIsoFiltered10'],

                        ['hltL3pfL1DoubleMu10MuOpenL1f0L2pf0L3PreFiltered8']
)
addTagAndProbePlotter(process,'MuonPairTagAndProbePlotter',
                        'MuonHttMu12GeV17',
                        'triggeredPatMuons',
                        'selectedTagAndProbeMuTracks',
                        #['WW','ISO','tightID'],
                        ['ID','SIP','ISO'],
                        #['pt()>30','pt()>10000'],
                        #['userInt("WWID")>0.5','(userIso(0)+max(photonIso()+neutralHadronIso()-0.5*puChargedHadronIso,0.0))/pt() < 0.1', 'userInt("tightID") >0.5'],                   
                        ['pfCandidateRef().isNonnull()&(isGlobalMuon()|isTrackerMuon())','abs(userFloat("ip3DS"))<4','(chargedHadronIso()+max(0.0,neutralHadronIso()+photonIso()-userFloat("zzRho2012")*userFloat("EAGammaNeuHadron04")))/pt()<0.40'],

#['userInt("WWID")>0.5','(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(2),0.0))/pt()<0.1'],
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
