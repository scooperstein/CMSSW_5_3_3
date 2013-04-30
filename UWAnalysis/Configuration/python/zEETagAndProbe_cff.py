import FWCore.ParameterSet.Config as cms



#Import tool that creates the cut sequence
from UWAnalysis.Configuration.tools.CutSequenceProducer import *


#tagAndProbeConfigurator = CutSequenceProducer(initialCounter  = 'initialEvents',
#                                  pyModuleName = __name__,
#                                  pyNameSpace  = locals())


#Tag and probe electron+GSF track
#tagAndProbeConfigurator.addDiCandidateModule('tagAndProbeEleTracks','PATEleTrackPairProducer', 'triggeredPatElectrons','gsfTrackCandidates','systematicsMET','cleanPatJets',0,9999,text = '',leadingObjectsOnly = True,dR = 0.15,recoMode = "")
#tagAndProbeConfigurator.addSorter('eleTracksSorted','PATEleTrackPairSorter')
#tagAndProbeConfigurator.addSelector('selectedTagAndProbeEleTracks','PATEleTrackPairSelector','abs(leg2.eta())<2.5&&(!(abs(leg2.eta())>1.442&&abs(leg2.eta())<1.566))&&leg1.pt()>15&&charge==0&&leg2.pt()>5&&mass>15&&mass<120&&leg1.userFloat("WWID")>0&&(leg1.chargedHadronIso+leg1.photonIso+leg1.neutralHadronIso)/leg1.pt()<0.1','tagAndProbeEleTracks',0,100)
#
#tagAndProbeSequenceEleTracks =tagAndProbeConfigurator.returnSequence()


##Tag and probe electron+SC
#tagAndProbeConfigurator2 = CutSequenceProducer(initialCounter  = 'initialTagAndProbeEvents2',
#                                   pyModuleName = __name__,
#                                   pyNameSpace  = locals())


##Tag and probe electron+SC
#tagAndProbeConfigurator2.addDiCandidateModule('tagAndProbeEleSCs','PATEleSCPairProducer', 'triggeredPatElectrons','superClusterCands','systematicsMET','cleanPatJets',1,9999,text = '',leadingObjectsOnly = True,dR = 0.5,recoMode = "")
#tagAndProbeConfigurator2.addSorter('eleSCsSorted','PATEleSCPairSorter')
#tagAndProbeConfigurator2.addSelector('selectedTagAndProbeEleSCs','PATEleSCPairSelector','calibratedMET.pt()<20 && abs(leg1.eta())<2.5&&abs(leg2.eta())<2.5&&leg1.pt()>20&&leg2.pt()>5&&mass>50&&mass<120&&leg1.userFloat("WWID")>0&&(leg1.chargedHadronIso+leg1.photonIso+leg1.neutralHadronIso())/leg1.pt()<0.1','tagAndProbeEleSCs',0,100)
#tagAndProbeSequenceEleSCs =tagAndProbeConfigurator2.returnSequence()



#Tag and probe electron+electron
tagAndProbeConfigurator3 = CutSequenceProducer(initialCounter  = 'initialTagAndProbeEvents3',
                                  pyModuleName = __name__,
                                  pyNameSpace  = locals())

tagAndProbeConfigurator3.addDiCandidateModule('tagAndProbeDiElectrons','PATElePairProducer', 'triggeredPatElectrons','triggeredPatElectrons','systematicsMET','cleanPatJets',0,9999,text = '',leadingObjectsOnly = False,dR = 0.15,recoMode = "")
tagAndProbeConfigurator3.addSorter('dielectronsSortedByZMass','PATElePairSorterByZMass')
tagAndProbeConfigurator3.addSelector('selectedTagAndProbeDiElectrons','PATElePairSelector','calibratedMET.pt()<20&&leg1.pt()>20&&leg2.pt()>5&&charge==0&&(leg1.userIso(0)+max(0.0, leg1.userIso(1)+leg1.neutralHadronIso()-0.5*leg1.userIso(2)))/leg1.pt()<0.10&&leg1.userFloat("WWID")>0&&abs(leg1.eta())<2.5','EEss',0,100)
tagAndProbeSequenceDiElectrons =tagAndProbeConfigurator3.returnSequence()

# tagAndProbeConfigurator4 = CutSequenceProducer(initialCounter  = 'initialTagAndProbeEvents4',
#                                   pyModuleName = __name__,
#                                   pyNameSpace  = locals())
#                                   
# ##Tag and probe electron+Tau
# tagAndProbeConfigurator4.addDiCandidateModule('tagAndProbeEleTaus','PATEleTauPairProducer', 'triggeredPatElectrons','triggeredPatTaus','systematicsMET','cleanPatJets',1,9999,text = '',leadingObjectsOnly = True,dR = 0.15,recoMode = "")
# tagAndProbeConfigurator4.addSelector('selectedTagAndProbeEleTaus','PATEleTauPairSelector','abs(leg2.eta())<2.1&&(!(abs(leg2.eta())>1.442&&abs(leg2.eta())<1.566))&&leg1.pt()>15&&charge==0&&leg2.pt()>5&&mass>15&&mass<120&&leg1.userFloat("WWID")>0&&(leg1.chargedHadronIso+leg1.photonIso+leg1.neutralHadronIso)/leg1.pt()<0.1&&(leg2.userFloat("hltOverlapFilterIsoEle15IsoPFTau20")+leg2.userFloat("hltOverlapFilterIsoEle15IsoPFTau15")+leg2.userFloat("hltOverlapFilterIsoEle15TightIsoPFTau20")+leg2.userFloat("hltOverlapFilterIsoEle18MediumIsoPFTau20")+leg2.userFloat("hltOverlapFilterIsoEle20MediumIsoPFTau20"))>0.5','tagAndProbeEleTracks',0,100)
# 
# tagAndProbeSequenceEleTaus =tagAndProbeConfigurator4.returnSequence()


#tagAndProbeSequence = cms.Sequence(tagAndProbeSequenceEleTaus + tagAndProbeSequenceEleSCs + tagAndProbeSequenceDiElectrons + tagAndProbeSequenceEleTracks)

tagAndProbeSequence = cms.Sequence(tagAndProbeSequenceDiElectrons)
