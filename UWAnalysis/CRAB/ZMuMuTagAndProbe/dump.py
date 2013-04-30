import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.source = cms.Source("PoolSource",
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_finalState*_*_*', 
        'drop *_patFinalStateEvent*_*_*'),
    fileNames = cms.untracked.vstring('/store/user/swanson/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Zjets_M50_2012-06-02-8TeV-078e4bc/ea74c25a04048a8dd7df6542c03c7a9b/output_99_1_ohb.root')
)
process.MEtoEDMConverter = cms.EDProducer("MEtoEDMConverter",
    deleteAfterCopy = cms.untracked.bool(True),
    Verbosity = cms.untracked.int32(0),
    Frequency = cms.untracked.int32(50),
    Name = cms.untracked.string('MEtoEDMConverter'),
    MEPathToSave = cms.untracked.string('')
)


process.ak5CaloJetsL1FastL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak5CaloJets"),
    correctors = cms.vstring('ak5CaloL1FastL2L3')
)


process.ak5CaloJetsL1FastL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak5CaloJets"),
    correctors = cms.vstring('ak5CaloL1FastL2L3Residual')
)


process.ak5CaloJetsL1L2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak5CaloJets"),
    correctors = cms.vstring('ak5CaloL1L2L3')
)


process.ak5CaloJetsL1L2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak5CaloJets"),
    correctors = cms.vstring('ak5CaloL1L2L3Residual')
)


process.ak5CaloJetsL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak5CaloJets"),
    correctors = cms.vstring('ak5CaloL2L3')
)


process.ak5CaloJetsL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak5CaloJets"),
    correctors = cms.vstring('ak5CaloL2L3Residual')
)


process.ak5JPTJetsL1FastL2L3 = cms.EDProducer("JPTJetCorrectionProducer",
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
    correctors = cms.vstring('ak5JPTL1FastL2L3')
)


process.ak5JPTJetsL1FastL2L3Residual = cms.EDProducer("JPTJetCorrectionProducer",
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
    correctors = cms.vstring('ak5JPTL1FastL2L3Residual')
)


process.ak5JPTJetsL1L2L3 = cms.EDProducer("JPTJetCorrectionProducer",
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
    correctors = cms.vstring('ak5JPTL1L2L3')
)


process.ak5JPTJetsL1L2L3Residual = cms.EDProducer("JPTJetCorrectionProducer",
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
    correctors = cms.vstring('ak5JPTL1L2L3Residual')
)


process.ak5JPTJetsL2L3 = cms.EDProducer("JPTJetCorrectionProducer",
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
    correctors = cms.vstring('ak5JPTL2L3')
)


process.ak5JPTJetsL2L3Residual = cms.EDProducer("JPTJetCorrectionProducer",
    src = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
    correctors = cms.vstring('ak5JPTL2L3Residual')
)


process.ak5PFJetsL1FastL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak5PFJets"),
    correctors = cms.vstring('ak5PFL1FastL2L3')
)


process.ak5PFJetsL1FastL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak5PFJets"),
    correctors = cms.vstring('ak5PFL1FastL2L3Residual')
)


process.ak5PFJetsL1L2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak5PFJets"),
    correctors = cms.vstring('ak5PFL1L2L3')
)


process.ak5PFJetsL1L2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak5PFJets"),
    correctors = cms.vstring('ak5PFL1L2L3Residual')
)


process.ak5PFJetsL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak5PFJets"),
    correctors = cms.vstring('ak5PFL2L3')
)


process.ak5PFJetsL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak5PFJets"),
    correctors = cms.vstring('ak5PFL2L3Residual')
)


process.ak5TrackJetsL2L3 = cms.EDProducer("TrackJetCorrectionProducer",
    src = cms.InputTag("ak5TrackJets"),
    correctors = cms.vstring('ak5TrackL2L3')
)


process.ak7CaloJetsL1FastL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak7CaloJets"),
    correctors = cms.vstring('ak7CaloL1FastL2L3')
)


process.ak7CaloJetsL1FastL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak7CaloJets"),
    correctors = cms.vstring('ak7CaloL1FastL2L3Residual')
)


process.ak7CaloJetsL1L2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak7CaloJets"),
    correctors = cms.vstring('ak7CaloL1L2L3')
)


process.ak7CaloJetsL1L2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak7CaloJets"),
    correctors = cms.vstring('ak7CaloL1L2L3Residual')
)


process.ak7CaloJetsL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak7CaloJets"),
    correctors = cms.vstring('ak7CaloL2L3')
)


process.ak7CaloJetsL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak7CaloJets"),
    correctors = cms.vstring('ak7CaloL2L3Residual')
)


process.ak7PFJetsL1FastL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak7PFJets"),
    correctors = cms.vstring('ak7PFL1FastL2L3')
)


process.ak7PFJetsL1FastL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak7PFJets"),
    correctors = cms.vstring('ak7PFL1FastL2L3Residual')
)


process.ak7PFJetsL1L2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak7PFJets"),
    correctors = cms.vstring('ak7PFL1L2L3')
)


process.ak7PFJetsL1L2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak7PFJets"),
    correctors = cms.vstring('ak7PFL1L2L3Residual')
)


process.ak7PFJetsL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak7PFJets"),
    correctors = cms.vstring('ak7PFL2L3')
)


process.ak7PFJetsL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak7PFJets"),
    correctors = cms.vstring('ak7PFL2L3Residual')
)


process.calibratedAK5PFJetsForPFMEtMVA = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak5PFJets"),
    correctors = cms.vstring('ak5PFL1FastL2L3')
)


process.cleanPatJets = cms.EDProducer("PATJetCleaner",
    finalCut = cms.string(''),
    src = cms.InputTag("selectedPatJets"),
    checkOverlaps = cms.PSet(

    ),
    preselection = cms.string('abs(eta)<5.0&&userFloat("idLoose")>0&&pt>10&&userInt("fullIdLoose")>0')
)


process.ic5CaloJetsL1FastL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5CaloJets"),
    correctors = cms.vstring('ic5CaloL1FastL2L3')
)


process.ic5CaloJetsL1FastL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5CaloJets"),
    correctors = cms.vstring('ic5CaloL1FastL2L3Residual')
)


process.ic5CaloJetsL1L2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5CaloJets"),
    correctors = cms.vstring('ic5CaloL1L2L3')
)


process.ic5CaloJetsL1L2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5CaloJets"),
    correctors = cms.vstring('ic5CaloL1L2L3Residual')
)


process.ic5CaloJetsL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5CaloJets"),
    correctors = cms.vstring('ic5CaloL2L3')
)


process.ic5CaloJetsL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5CaloJets"),
    correctors = cms.vstring('ic5CaloL2L3Residual')
)


process.ic5PFJetsL1FastL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5PFJets"),
    correctors = cms.vstring('ic5PFL1FastL2L3')
)


process.ic5PFJetsL1FastL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5PFJets"),
    correctors = cms.vstring('ic5PFL1FastL2L3Residual')
)


process.ic5PFJetsL1L2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5PFJets"),
    correctors = cms.vstring('ic5PFL1L2L3')
)


process.ic5PFJetsL1L2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5PFJets"),
    correctors = cms.vstring('ic5PFL1L2L3Residual')
)


process.ic5PFJetsL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5PFJets"),
    correctors = cms.vstring('ic5PFL2L3')
)


process.ic5PFJetsL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5PFJets"),
    correctors = cms.vstring('ic5PFL2L3Residual')
)


process.initialCounter = cms.EDProducer("EventCounter",
    name = cms.string('initialEvents')
)


process.initialTagAndProbeEventsCounter = cms.EDProducer("EventCounter",
    name = cms.string('initialTagAndProbeEvents')
)


process.kt4CaloJetsL1FastL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt4CaloJets"),
    correctors = cms.vstring('kt4CaloL1FastL2L3')
)


process.kt4CaloJetsL1FastL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt4CaloJets"),
    correctors = cms.vstring('kt4CaloL1FastL2L3Residual')
)


process.kt4CaloJetsL1L2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt4CaloJets"),
    correctors = cms.vstring('kt4CaloL1L2L3')
)


process.kt4CaloJetsL1L2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt4CaloJets"),
    correctors = cms.vstring('kt4CaloL1L2L3Residual')
)


process.kt4CaloJetsL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt4CaloJets"),
    correctors = cms.vstring('kt4CaloL2L3')
)


process.kt4CaloJetsL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt4CaloJets"),
    correctors = cms.vstring('kt4CaloL2L3Residual')
)


process.kt4PFJetsL1FastL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt4PFJets"),
    correctors = cms.vstring('kt4PFL1FastL2L3')
)


process.kt4PFJetsL1FastL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt4PFJets"),
    correctors = cms.vstring('kt4PFL1FastL2L3Residual')
)


process.kt4PFJetsL1L2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt4PFJets"),
    correctors = cms.vstring('kt4PFL1L2L3')
)


process.kt4PFJetsL1L2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt4PFJets"),
    correctors = cms.vstring('kt4PFL1L2L3Residual')
)


process.kt4PFJetsL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt4PFJets"),
    correctors = cms.vstring('kt4PFL2L3')
)


process.kt4PFJetsL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt4PFJets"),
    correctors = cms.vstring('kt4PFL2L3Residual')
)


process.kt6CaloJetsL1FastL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt6CaloJets"),
    correctors = cms.vstring('kt6CaloL1FastL2L3')
)


process.kt6CaloJetsL1FastL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt6CaloJets"),
    correctors = cms.vstring('kt6CaloL1FastL2L3Residual')
)


process.kt6CaloJetsL1L2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt6CaloJets"),
    correctors = cms.vstring('kt6CaloL1L2L3')
)


process.kt6CaloJetsL1L2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt6CaloJets"),
    correctors = cms.vstring('kt6CaloL1L2L3Residual')
)


process.kt6CaloJetsL2L3 = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt6CaloJets"),
    correctors = cms.vstring('kt6CaloL2L3')
)


process.kt6CaloJetsL2L3Residual = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt6CaloJets"),
    correctors = cms.vstring('kt6CaloL2L3Residual')
)


process.kt6PFJetsL1FastL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt6PFJets"),
    correctors = cms.vstring('kt6PFL1FastL2L3')
)


process.kt6PFJetsL1FastL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt6PFJets"),
    correctors = cms.vstring('kt6PFL1FastL2L3Residual')
)


process.kt6PFJetsL1L2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt6PFJets"),
    correctors = cms.vstring('kt6PFL1L2L3')
)


process.kt6PFJetsL1L2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt6PFJets"),
    correctors = cms.vstring('kt6PFL1L2L3Residual')
)


process.kt6PFJetsL2L3 = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt6PFJets"),
    correctors = cms.vstring('kt6PFL2L3')
)


process.kt6PFJetsL2L3Residual = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt6PFJets"),
    correctors = cms.vstring('kt6PFL2L3Residual')
)


process.mvaMetEleTau = cms.EDProducer("PFMETProducerMVA2",
    srcLeptons = cms.VInputTag("metElectrons", "metEleTaus"),
    dZcut = cms.double(0.1),
    inputFileNames = cms.PSet(
        DPhi = cms.FileInPath('pharris/MVAMet/data/gbrmetphi_52.root'),
        CovU2 = cms.FileInPath('pharris/MVAMet/data/gbrmetu2cov_52.root'),
        U = cms.FileInPath('pharris/MVAMet/data/gbrmet_52.root'),
        CovU1 = cms.FileInPath('pharris/MVAMet/data/gbrmetu1cov_52.root')
    ),
    srcPFCandidates = cms.InputTag("particleFlow"),
    srcMVAData = cms.InputTag("pfMEtMVAData")
)


process.mvaMetMuTau = cms.EDProducer("PFMETProducerMVA2",
    srcLeptons = cms.VInputTag("metMuons", "metMuTaus"),
    dZcut = cms.double(0.1),
    inputFileNames = cms.PSet(
        DPhi = cms.FileInPath('pharris/MVAMet/data/gbrmetphi_52.root'),
        CovU2 = cms.FileInPath('pharris/MVAMet/data/gbrmetu2cov_52.root'),
        U = cms.FileInPath('pharris/MVAMet/data/gbrmet_52.root'),
        CovU1 = cms.FileInPath('pharris/MVAMet/data/gbrmetu1cov_52.root')
    ),
    srcPFCandidates = cms.InputTag("particleFlow"),
    srcMVAData = cms.InputTag("pfMEtMVAData")
)


process.patMETs = cms.EDProducer("PATMETProducer",
    metSource = cms.InputTag("caloType1CorrectedMet"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addResolutions = cms.bool(False),
    addEfficiencies = cms.bool(False),
    genMETSource = cms.InputTag("genMetTrue"),
    efficiencies = cms.PSet(

    ),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(True),
    muonSource = cms.InputTag("muons"),
    resolutions = cms.PSet(

    )
)


process.patMVAMetEleTau = cms.EDProducer("PATMETProducer",
    metSource = cms.InputTag("mvaMetEleTau"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addResolutions = cms.bool(False),
    muonSource = cms.InputTag("muons"),
    addEfficiencies = cms.bool(False),
    genMETSource = cms.InputTag("genMetTrue"),
    efficiencies = cms.PSet(

    ),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    resolutions = cms.PSet(

    )
)


process.patMVAMetMuTau = cms.EDProducer("PATMETProducer",
    metSource = cms.InputTag("mvaMetMuTau"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring()
    ),
    addResolutions = cms.bool(False),
    muonSource = cms.InputTag("muons"),
    addEfficiencies = cms.bool(False),
    genMETSource = cms.InputTag("genMetTrue"),
    efficiencies = cms.PSet(

    ),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    resolutions = cms.PSet(

    )
)


process.pfMEtMVA = cms.EDProducer("PFMETProducerMVA",
    tmvaVariables = cms.vstring('nvtx', 
        'jetPt', 
        'jetEta', 
        'jetPhi', 
        'dZ', 
        'd0', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dRMean', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'),
    minCorrJetPt = cms.double(-1.0),
    tmvaMethod = cms.string('JetID'),
    cutBased = cms.bool(False),
    verbosity = cms.int32(0),
    srcCorrJets = cms.InputTag("calibratedAK5PFJetsForPFMEtMVA"),
    srcVertices = cms.InputTag("offlinePrimaryVertices"),
    tmvaSpectators = cms.vstring(),
    impactParTkThreshold = cms.double(0.0),
    version = cms.int32(-1),
    inputFileNames = cms.PSet(
        DPhi = cms.FileInPath('pharris/MVAMet/data/gbrmetphi_52.root'),
        CovU2 = cms.FileInPath('pharris/MVAMet/data/gbrmetu2cov_52.root'),
        U = cms.FileInPath('pharris/MVAMet/data/gbrmet_52.root'),
        CovU1 = cms.FileInPath('pharris/MVAMet/data/gbrmetu1cov_52.root')
    ),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    dZcut = cms.double(0.1),
    srcLeptons = cms.VInputTag(),
    srcUncorrJets = cms.InputTag("ak5PFJets"),
    globalThreshold = cms.double(0.0),
    JetIdParams = cms.PSet(
        Pt2030_Tight = cms.vdouble(0.3, 0.4, 0.7, 0.8),
        Pt2030_Loose = cms.vdouble(0.0, 0.0, 0.2, 0.6),
        Pt3050_Medium = cms.vdouble(0.3, 0.2, 0.7, 0.8),
        Pt1020_Tight = cms.vdouble(-0.2, 0.2, 0.2, 0.6),
        Pt2030_Medium = cms.vdouble(0.2, 0.2, 0.5, 0.7),
        Pt010_Tight = cms.vdouble(0.5, 0.6, 0.6, 0.9),
        Pt1020_Loose = cms.vdouble(-0.4, -0.4, -0.4, 0.4),
        Pt010_Medium = cms.vdouble(0.2, 0.4, 0.2, 0.6),
        Pt1020_Medium = cms.vdouble(-0.3, 0.0, 0.0, 0.5),
        Pt010_Loose = cms.vdouble(0.0, 0.0, 0.0, 0.2),
        Pt3050_Loose = cms.vdouble(0.0, 0.0, 0.6, 0.2),
        Pt3050_Tight = cms.vdouble(0.5, 0.4, 0.8, 0.9)
    ),
    tmvaWeights = cms.string('CMGTools/External/data/mva_JetID_v1.weights.xml'),
    srcPFCandidates = cms.InputTag("particleFlow")
)


process.pfMEtMVA2 = cms.EDProducer("PFMETProducerMVA2",
    srcLeptons = cms.VInputTag(),
    dZcut = cms.double(0.1),
    inputFileNames = cms.PSet(
        DPhi = cms.FileInPath('pharris/MVAMet/data/gbrmetphi_52.root'),
        CovU2 = cms.FileInPath('pharris/MVAMet/data/gbrmetu2cov_52.root'),
        U = cms.FileInPath('pharris/MVAMet/data/gbrmet_52.root'),
        CovU1 = cms.FileInPath('pharris/MVAMet/data/gbrmetu1cov_52.root')
    ),
    srcPFCandidates = cms.InputTag("particleFlow"),
    srcMVAData = cms.InputTag("pfMEtMVAData")
)


process.pfMEtMVAData = cms.EDProducer("PFMETProducerMVAData",
    tmvaVariables = cms.vstring('nvtx', 
        'jetPt', 
        'jetEta', 
        'jetPhi', 
        'dZ', 
        'd0', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dRMean', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'),
    minCorrJetPt = cms.double(-1.0),
    tmvaMethod = cms.string('JetID'),
    cutBased = cms.bool(False),
    verbosity = cms.int32(0),
    srcCorrJets = cms.InputTag("calibratedAK5PFJetsForPFMEtMVA"),
    srcVertices = cms.InputTag("offlinePrimaryVertices"),
    tmvaSpectators = cms.vstring(),
    impactParTkThreshold = cms.double(0.0),
    version = cms.int32(-1),
    srcRho = cms.InputTag("kt6PFJets","rho"),
    dZcut = cms.double(0.1),
    srcUncorrJets = cms.InputTag("ak5PFJets"),
    globalThreshold = cms.double(0.0),
    JetIdParams = cms.PSet(
        Pt2030_Tight = cms.vdouble(0.3, 0.4, 0.7, 0.8),
        Pt2030_Loose = cms.vdouble(0.0, 0.0, 0.2, 0.6),
        Pt3050_Medium = cms.vdouble(0.3, 0.2, 0.7, 0.8),
        Pt1020_Tight = cms.vdouble(-0.2, 0.2, 0.2, 0.6),
        Pt2030_Medium = cms.vdouble(0.2, 0.2, 0.5, 0.7),
        Pt010_Tight = cms.vdouble(0.5, 0.6, 0.6, 0.9),
        Pt1020_Loose = cms.vdouble(-0.4, -0.4, -0.4, 0.4),
        Pt010_Medium = cms.vdouble(0.2, 0.4, 0.2, 0.6),
        Pt1020_Medium = cms.vdouble(-0.3, 0.0, 0.0, 0.5),
        Pt010_Loose = cms.vdouble(0.0, 0.0, 0.0, 0.2),
        Pt3050_Loose = cms.vdouble(0.0, 0.0, 0.6, 0.2),
        Pt3050_Tight = cms.vdouble(0.5, 0.4, 0.8, 0.9)
    ),
    tmvaWeights = cms.string('CMGTools/External/data/mva_JetID_v1.weights.xml'),
    srcPFCandidates = cms.InputTag("particleFlow")
)


process.pfMet = cms.EDProducer("METProducer",
    resolutionsEra = cms.string('Spring10'),
    PF_EtResType6 = cms.vdouble(0.0, 1.22, 0.05),
    HB_EtResPar = cms.vdouble(0.0, 1.22, 0.05),
    jdphi6 = cms.vdouble(0.084, 0.08, 0.072, 0.065, 0.066, 
        0.06, 0.051, 0.049, 0.045, 0.045),
    jdphi3 = cms.vdouble(0.042, 0.043, 0.044, 0.043, 0.041, 
        0.039, 0.039, 0.036, 0.034, 0.031),
    jdpt9 = cms.vdouble(0.843, 0.885, 1.245, 1.665, 1.944, 
        1.981, 1.972, 2.875, 3.923, 7.51),
    jdpt8 = cms.vdouble(0.889, 0.939, 1.166, 1.365, 1.553, 
        1.805, 2.06, 2.22, 2.268, 2.247),
    jdpt7 = cms.vdouble(1.094, 1.139, 1.436, 1.672, 1.831, 
        2.05, 2.267, 2.549, 2.785, 2.86),
    jdpt6 = cms.vdouble(1.213, 1.298, 1.716, 2.015, 2.191, 
        2.612, 2.863, 2.879, 2.925, 2.902),
    jdpt5 = cms.vdouble(1.049, 1.149, 1.607, 1.869, 2.012, 
        2.219, 2.289, 2.412, 2.695, 2.865),
    jdpt4 = cms.vdouble(0.85, 0.961, 1.337, 1.593, 1.854, 
        2.005, 2.209, 2.533, 2.812, 3.047),
    jdpt3 = cms.vdouble(0.929, 1.04, 1.46, 1.74, 2.042, 
        2.289, 2.639, 2.837, 2.946, 2.971),
    jdpt2 = cms.vdouble(0.841, 0.937, 1.316, 1.605, 1.919, 
        2.295, 2.562, 2.722, 2.943, 3.293),
    EE_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    jdpt0 = cms.vdouble(0.749, 0.829, 1.099, 1.355, 1.584, 
        1.807, 2.035, 2.217, 2.378, 2.591),
    HF_PhiResPar = cms.vdouble(0.05022),
    HE_PhiResPar = cms.vdouble(0.02511),
    jdpt1 = cms.vdouble(0.718, 0.813, 1.133, 1.384, 1.588, 
        1.841, 2.115, 2.379, 2.508, 2.772),
    PF_PhiResType2 = cms.vdouble(0.002),
    PF_PhiResType3 = cms.vdouble(0.002),
    HF_EtResPar = cms.vdouble(0.0, 1.82, 0.09),
    resolutionsAlgo = cms.string('AK5PF'),
    PF_PhiResType6 = cms.vdouble(0.02511),
    PF_PhiResType7 = cms.vdouble(0.02511),
    PF_PhiResType4 = cms.vdouble(0.0028, 0.0, 0.0022),
    PF_PhiResType5 = cms.vdouble(0.1, 0.1, 0.13),
    ptresolthreshold = cms.double(10.0),
    HO_EtResPar = cms.vdouble(0.0, 1.3, 0.005),
    EB_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    EB_PhiResPar = cms.vdouble(0.00502),
    jdphi9 = cms.vdouble(0.062, 0.059, 0.053, 0.047, 0.042, 
        0.045, 0.036, 0.032, 0.034, 0.044),
    jdphi8 = cms.vdouble(0.059, 0.057, 0.051, 0.044, 0.038, 
        0.035, 0.037, 0.032, 0.028, 0.028),
    jdphi4 = cms.vdouble(0.042, 0.042, 0.043, 0.042, 0.038, 
        0.036, 0.036, 0.033, 0.031, 0.031),
    HO_PhiResPar = cms.vdouble(0.02511),
    jdphi2 = cms.vdouble(0.04, 0.04, 0.04, 0.04, 0.04, 
        0.038, 0.036, 0.035, 0.034, 0.033),
    jdphi1 = cms.vdouble(0.034, 0.035, 0.035, 0.035, 0.035, 
        0.034, 0.031, 0.03, 0.029, 0.027),
    jdphi0 = cms.vdouble(0.034, 0.034, 0.034, 0.034, 0.032, 
        0.031, 0.028, 0.027, 0.027, 0.027),
    jdphi7 = cms.vdouble(0.077, 0.072, 0.059, 0.05, 0.045, 
        0.042, 0.039, 0.039, 0.037, 0.031),
    EE_PhiResPar = cms.vdouble(0.02511),
    jdphi5 = cms.vdouble(0.069, 0.069, 0.064, 0.058, 0.053, 
        0.049, 0.049, 0.043, 0.039, 0.04),
    HB_PhiResPar = cms.vdouble(0.02511),
    PF_PhiResType1 = cms.vdouble(0.002),
    PF_EtResType5 = cms.vdouble(0.41, 0.52, 0.25),
    PF_EtResType4 = cms.vdouble(0.042, 0.1, 0.0),
    PF_EtResType7 = cms.vdouble(0.0, 1.22, 0.05),
    HE_EtResPar = cms.vdouble(0.0, 1.3, 0.05),
    PF_EtResType1 = cms.vdouble(0.05, 0, 0),
    PF_EtResType3 = cms.vdouble(0.05, 0, 0),
    PF_EtResType2 = cms.vdouble(0.05, 0, 0),
    src = cms.InputTag("particleFlow"),
    METType = cms.string('PFMET'),
    calculateSignificance = cms.bool(True),
    alias = cms.string('PFMET'),
    noHF = cms.bool(False),
    jets = cms.InputTag("ak5PFJets"),
    globalThreshold = cms.double(0.0),
    InputType = cms.string('PFCandidateCollection')
)


process.preTriggeredPatTaus = cms.EDProducer("TauTriggerMatcher",
    pdgId = cms.int32(0),
    trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
    filters = cms.VInputTag(cms.InputTag("hltFilterDoubleIsoPFTau20Trk5LeadTrack5IsolationL1HLTMatched","","HLT"), cms.InputTag("hltOverlapFilterIsoEle20LooseIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoMu18LooseIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle20WP90LooseIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoMu17LooseIsoPFTau20","","HLT")),
    src = cms.InputTag("cleanPatTaus")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.selectedTagAndProbeMuTracksCounter = cms.EDProducer("EventCounter",
    name = cms.string('tagAndProbePairs')
)


process.tagAndProbeMuTracks = cms.EDProducer("PATMuPairProducer",
    useLeadingTausOnly = cms.bool(False),
    srcLeg1 = cms.InputTag("cleanPatMuons"),
    srcLeg2 = cms.InputTag("cleanPatMuons"),
    srcJets = cms.InputTag("selectedPatJets"),
    dRmin12 = cms.double(0.15),
    srcMET = cms.InputTag("systematicsMET"),
    srcPrimaryVertex = cms.InputTag("offlinePrimaryVertices"),
    srcBeamSpot = cms.InputTag("offlineBeamSpot"),
    srcGenParticles = cms.InputTag("genTaus"),
    recoMode = cms.string(''),
    verbosity = cms.untracked.int32(0),
    doSVreco = cms.bool(False),
    metCalibration = cms.PSet(
        responseMCU2 = cms.string('-0.00544907'),
        resolutionMCU2 = cms.string('10.5649+0.0225853*x-5.81371e-5*x*x'),
        resolutionMCU1 = cms.string('10.6449+0.0436475*x+3.07554e-5*x*x'),
        responseMCU1 = cms.string('1.26247-0.950094*x'),
        responseU1 = cms.string('1.33223-0.917782*x'),
        responseU2 = cms.string('-0.013'),
        applyCalibration = cms.bool(False),
        calibrationScheme = cms.string('BothLegs'),
        resolutionU1 = cms.string('11.1566+0.0654529*x+0.000124436*x*x'),
        resolutionU2 = cms.string('11.1235+0.0449872*x-6.39822e-5*x*x')
    )
)


process.triggeredPatElectrons = cms.EDProducer("ElectronTriggerMatcher",
    pdgId = cms.int32(11),
    trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
    filters = cms.VInputTag(cms.InputTag("hltOverlapFilterIsoEle15IsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle15TightIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle18MediumIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle18TightIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle18IsoPFTau20","","HLT"), 
        cms.InputTag("hltOverlapFilterIsoEle20MediumIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle20LooseIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle20WP90LooseIsoPFTau20","","HLT"), cms.InputTag("hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTEle8PMMassFilter","","HLT"), cms.InputTag("hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1IsoEG18OrEG20","","HLT")),
    src = cms.InputTag("triggeredPatElectronsL")
)


process.triggeredPatElectronsL = cms.EDProducer("ElectronTriggerMatcher",
    pdgId = cms.int32(0),
    trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
    filters = cms.VInputTag(cms.InputTag("hltEle17CaloIdLCaloIsoVLPixelMatchFilterDoubleEG125","","HLT")),
    src = cms.InputTag("cleanPatElectrons")
)


process.triggeredPatMuons = cms.EDProducer("MuonTriggerMatcher",
    pdgId = cms.int32(13),
    trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
    filters = cms.VInputTag(cms.InputTag("hltBLifetimeL3PFFilterSingleTop","","HLT"), cms.InputTag("hltIsoMu202p1CentralPFJet30MuCleaned","","HLT"), cms.InputTag("hltIsoMu20eta2p1CentralPFJet80MuCleaned","","HLT"), cms.InputTag("hltBLifetimeL3PFNoPUFilterSingleTop","","HLT"), cms.InputTag("hltIsoMu202p1CentralPFNoPUJet30MuCleaned","","HLT"), 
        cms.InputTag("hltIsoMu202p1DiCentralPFJet30MuCleaned","","HLT"), cms.InputTag("hltIsoMu202p1DiCentralPFNoPUJet30MuCleaned","","HLT"), cms.InputTag("hltIsoMu202p1TriCentralPFJet30MuCleaned","","HLT"), cms.InputTag("hltIsoMu202p1CentralPFJet50MuCleaned","","HLT"), cms.InputTag("hltIsoMu202p1TriCentralPFNoPUJet30MuCleaned ","","HLT"), 
        cms.InputTag("hltIsoMu202p1CentralPFNoPUJet50MuCleaned","","HLT"), cms.InputTag("hlt2IsoMu20eta2p1PFMHTPt80","","HLT"), cms.InputTag("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f20L3crIsoFiltered10","","HLT"), cms.InputTag("hltPFMHT20Filter","","HLT"), cms.InputTag("hltIsoMu24eta2p1DiCentralPFJet25MuCleaned","","HLT"), 
        cms.InputTag("hltIsoMu24eta2p1PFJet30PFJet25Deta3PFJetCollectionsVBFFilter","","HLT"), cms.InputTag("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10","","HLT"), cms.InputTag("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f30QL3crIsoFiltered10","","HLT"), cms.InputTag("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f34QL3crIsoFiltered10","","HLT"), cms.InputTag("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f40QL3crIsoFiltered10","","HLT"), 
        cms.InputTag("hltPFMHT55Filter","","HLT"), cms.InputTag("hltPFMHT60Filter","","HLT"), cms.InputTag("hltL3L1Mu10erJetC20JetC12Corr1OrL1Mu10erJetC32OrMu10erJetC32JetC12Corr1L3Mufiltered12Eta2p1","","HLT"), cms.InputTag("hltBLifetime3D1stTrkL3FilterJet20HbbL1FastJet","","HLT"), cms.InputTag("hltDiBLifetime3D1stTrkL3FilterJet20HbbL1FastJet","","HLT"), 
        cms.InputTag("hltL3L1Mu10erJetC20JetC12Corr1OrL1Mu10erJetC32OrMu10erJetC32JetC12Corr1L3Mufiltered12Eta2p1","","HLT"), cms.InputTag("hltL3L1Mu10erJetC20JetC12Corr1OrL1Mu10erJetC32OrMu10erJetC32JetC12Corr1L3Mufiltered12Eta2p1","","HLT"), cms.InputTag("hltL3fL1sMu7L3Filtered12","","HLT"), cms.InputTag("hltBLifetime3D1stTrkL3FilterJet20HbbL1FastJet","","HLT"), cms.InputTag("hltDiBLifetime3D1stTrkL3FilterJet20HbbL1FastJet","","HLT"), 
        cms.InputTag("hltL1Mu10Eta2p1Jet20Jet12CentralCorrOrMu10erJetC32L3Mufiltered15Eta2p1","","HLT"), cms.InputTag("hltL3fL1sMu7L1fEta2p1L2fEta2p1f7L3FilteredEta2p1Filtered15","","HLT"), cms.InputTag("hltBLifetimeL3PFFilterSingleTopNoIso","","HLT"), cms.InputTag("hltBLifetimeL3PFNoPUFilterSingleTopNoIso","","HLT"), cms.InputTag("hltMu202p1TriCentralPFJet30MuCleaned","","HLT"), 
        cms.InputTag("hltMu202p1CentralPFJet50MuCleaned","","HLT"), cms.InputTag("hltMu202p1TriCentralPFNoPUJet30MuCleaned","","HLT"), cms.InputTag("hltMu202p1CentralPFNoPUJet50MuCleaned","","HLT"), cms.InputTag("hltMu24eta2p1DiCentralPFJet25MuCleaned","","HLT"), cms.InputTag("hltMu24eta2p1PFJet30PFJet25Deta3PFJetCollectionsVBFFilter","","HLT"), 
        cms.InputTag("hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q","","HLT"), cms.InputTag("hltSingleMuIsoL3IsoFiltered12","","HLT"), cms.InputTag("hltSingleMuIsoL3IsoFiltered15","","HLT"), cms.InputTag("hltSingleMuIsoL3IsoFiltered24","","HLT"), cms.InputTag("hltOverlapFilterIsoMu15IsoPFTau15","","HLT"), 
        cms.InputTag("hltOverlapFilterIsoMu12IsoPFTau10","","HLT"), cms.InputTag("hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered30Q","","HLT"), cms.InputTag("hltDeDxFilter50DEDX3p6Mu","","HLT"), cms.InputTag("hltDeDxFilter60DEDX3p7Mu","","HLT"), cms.InputTag("hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q","","HLT"), 
        cms.InputTag("hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered50Q","","HLT"), cms.InputTag("hltL3fL1sMu3L3Filtered5","","HLT"), cms.InputTag("hltL3reliso1p0mufiltermu17","","HLT"), cms.InputTag("hltL3reliso1p0mufiltermu5","","HLT"), cms.InputTag("hltSingleMuIsoL3IsoFiltered17","","HLT"), 
        cms.InputTag("hltSingleMuIsoL1s14L3IsoFiltered15eta2p1","","HLT"), cms.InputTag("hltL3IsoL1sMu14Eta2p1L1f0L2f14QL2IsoL3f24L3IsoFiltered","","HLT"), cms.InputTag("hltOverlapFilterIsoMu15IsoPFTau20","","HLT"), cms.InputTag("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoFiltered10","","HLT"), cms.InputTag("hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10","","HLT"), 
        cms.InputTag("hltOverlapFilterIsoMu18LooseIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoMu17LooseIsoPFTau20","","HLT"), cms.InputTag("hltDoubleMu11ExclL3PreFiltered","","HLT"), cms.InputTag("hltDoubleMu4ExclL3PreFiltered","","HLT"), cms.InputTag("hltDoubleMu5IsoMu5IsoL3IsoFiltered5","","HLT"), 
        cms.InputTag("hltL2DoubleMu23NoVertexL2Filtered2ChaAngle2p5","","HLT"), cms.InputTag("hltL2DoubleMu23NoVertexL2PreFiltered","","HLT"), cms.InputTag("hltL2DoubleMu38NoVertexL2Filtered2ChaAngle2p5","","HLT"), cms.InputTag("hltDiMuonMu17Mu8DzFiltered0p2","","HLT"), cms.InputTag("hltDiMuonGlb17Trk8DzFiltered0p2","","HLT"), 
        cms.InputTag("hltL3fL1sMu12L3Filtered17","","HLT"), cms.InputTag("hltDiMuonGlb22Trk22DzFiltered0p2","","HLT"), cms.InputTag("hltDiMuonGlb22Trk8DzFiltered0p2 ","","HLT"), cms.InputTag("hltL3fL1sMu3L3Filtered8","","HLT"), cms.InputTag("hltTripleMu0L3TriMuFiltered5","","HLT")),
    src = cms.InputTag("cleanPatMuons")
)


process.triggeredPatTaus = cms.EDProducer("TauTriggerMatcher",
    pdgId = cms.int32(15),
    trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
    filters = cms.VInputTag(cms.InputTag("hltOverlapFilterIsoMu15IsoPFTau15","","HLT"), cms.InputTag("hltOverlapFilterIsoMu15IsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoMu15MediumIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoMu15TightIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterMu15IsoPFTau20","","HLT"), 
        cms.InputTag("hltOverlapFilterIsoMu12IsoPFTau10","","HLT"), cms.InputTag("hltOverlapFilterIsoMu15IsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle15IsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle15TightIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle18MediumIsoPFTau20","","HLT"), 
        cms.InputTag("hltOverlapFilterIsoEle20MediumIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle20LooseIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoMu18LooseIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoEle20WP90LooseIsoPFTau20","","HLT"), cms.InputTag("hltOverlapFilterIsoMu17LooseIsoPFTau20","","HLT")),
    src = cms.InputTag("preTriggeredPatTaus")
)


process.metEleTaus = cms.EDFilter("PATTauSelector",
    filter = cms.bool(False),
    src = cms.InputTag("cleanPatTaus"),
    cut = cms.string('abs(userFloat("dz"))<0.2&&pt>20&&tauID("byLooseIsolationMVA")&&tauID("againstElectronMedium")&&tauID("againstElectronMVA")&&tauID("againstMuonLoose")&&abs(eta())<2.3')
)


process.metElectrons = cms.EDFilter("PATElectronSelector",
    filter = cms.bool(False),
    src = cms.InputTag("cleanPatElectrons"),
    cut = cms.string('abs(userFloat("dz"))<0.2&&pt>20&&userFloat("wp95V")>0&&(userIso(0)+max(photonIso+neutralHadronIso()-0.5*userIso(2),0.0))/pt()<0.1&&!(userFloat("hasConversion")>0)&&userInt("missingHits")==0&&abs(userFloat("ipDXY"))<0.045&&abs(eta())<2.1')
)


process.metMuTaus = cms.EDFilter("PATTauSelector",
    filter = cms.bool(False),
    src = cms.InputTag("cleanPatTaus"),
    cut = cms.string('abs(userFloat("dz"))<0.2&&pt>20&&tauID("byLooseIsolationMVA")&&tauID("againstElectronLoose")&&tauID("againstMuonTight")&&abs(eta())<2.3')
)


process.metMuons = cms.EDFilter("PATMuonSelector",
    filter = cms.bool(False),
    src = cms.InputTag("cleanPatMuons"),
    cut = cms.string('abs(userFloat("dz"))<0.2&&pt>17&&userInt("tightID")>0&&(userIso(0)+max(photonIso+neutralHadronIso()-0.5*userIso(2),0.0))/pt()<0.1&&abs(eta())<2.1&&abs(userFloat("ipDXY"))<0.045')
)


process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string('ndof()>4&&position().rho()<2&&abs(z())<24')
)


process.selectedPatElectrons = cms.EDFilter("PATElectronSelector",
    filter = cms.bool(False),
    src = cms.InputTag("cleanPatElectrons"),
    cut = cms.string('pt>10&&userFloat("wp95")>0&&(userIso(0)+max(photonIso+neutralHadronIso()-0.5*userIso(2),0.0))/pt()<0.3')
)


process.selectedPatMuons = cms.EDFilter("PATMuonSelector",
    filter = cms.bool(False),
    src = cms.InputTag("cleanPatMuons"),
    cut = cms.string('pt>10&&userInt("tightID")&&(userIso(0)+max(photonIso+neutralHadronIso()-0.5*userIso(2),0.0))/pt()<0.3')
)


process.selectedPatTaus = cms.EDFilter("PATTauSelector",
    filter = cms.bool(False),
    src = cms.InputTag("cleanPatTaus"),
    cut = cms.string('pt>15&&tauID("byLooseIsolationMVA")&&tauID("againstElectronLoose")&&tauID("againstMuonLoose")')
)


process.selectedTagAndProbeMuTracks = cms.EDFilter("PATMuPairSelector",
    src = cms.InputTag("tagAndProbeMuTracks"),
    cut = cms.string('charge==0&&mass>50&&mass<120&&leg1.pt()>25&&leg2.pt()>5&&abs(leg2.eta())<2.4&&abs(leg1.eta())<2.1'),
    filter = cms.bool(False)
)


process.selectedTagAndProbeMuTracksFilter = cms.EDFilter("PATCandViewCountFilter",
    minNumber = cms.uint32(1),
    maxNumber = cms.uint32(100),
    src = cms.InputTag("selectedTagAndProbeMuTracks")
)


process.tagAndProbeMuTracksFilter = cms.EDFilter("PATCandViewCountFilter",
    minNumber = cms.uint32(1),
    maxNumber = cms.uint32(9999),
    src = cms.InputTag("tagAndProbeMuTracks")
)


process.EDMtoMEConverter = cms.EDAnalyzer("EDMtoMEConverter",
    convertOnEndLumi = cms.untracked.bool(True),
    Frequency = cms.untracked.int32(50),
    Verbosity = cms.untracked.int32(0),
    Name = cms.untracked.string('EDMtoMEConverter'),
    convertOnEndRun = cms.untracked.bool(True)
)


process.dqmEnv = cms.EDAnalyzer("DQMEventInfo",
    subSystemFolder = cms.untracked.string('YourSubsystem'),
    eventRateWindow = cms.untracked.double(0.5),
    eventInfoFolder = cms.untracked.string('EventInfo')
)


process.dqmSaver = cms.EDAnalyzer("DQMFileSaver",
    dirName = cms.untracked.string('.'),
    saveByTime = cms.untracked.int32(-1),
    producer = cms.untracked.string('DQM'),
    saveByEvent = cms.untracked.int32(-1),
    forceRunNumber = cms.untracked.int32(-1),
    saveByRun = cms.untracked.int32(1),
    workflow = cms.untracked.string(''),
    saveAtJobEnd = cms.untracked.bool(False),
    version = cms.untracked.int32(1),
    referenceRequireStatus = cms.untracked.int32(100),
    convention = cms.untracked.string('Offline'),
    saveByMinute = cms.untracked.int32(-1),
    runIsComplete = cms.untracked.bool(False),
    saveByLumiSection = cms.untracked.int32(-1),
    referenceHandling = cms.untracked.string('all')
)


process.summary = cms.EDAnalyzer("EventSummary",
    src = cms.untracked.vstring('initialTagAndProbeEvents', 
        'tagAndProbePairs')
)


process.tagAndProbeMuonHLTMu8ZZ = cms.EDAnalyzer("MuonPairTagAndProbePlotter",
    src = cms.InputTag("patMuonsForAnalysis"),
    methods = cms.vstring('userFloat("isZZMuon")>0.5', 
        '(chargedHadronIso+max(photonIso+neutralHadronIso-0.5*userIso(0),0.0))/pt()<0.25'),
    triggers = cms.vstring('hltSingleMuIsoL3IsoFiltered12', 
        'hltSingleMuIsoL3IsoFiltered24'),
    patTrigger = cms.InputTag("patTrigger"),
    vertices = cms.InputTag("primaryVertexFilter"),
    triggersProbe = cms.vstring('hltDiMuonL3PreFiltered8', 
        'hltDiMuonL3PreFiltered7'),
    ref = cms.InputTag("selectedTagAndProbeMuTracks"),
    id = cms.vstring('ID', 
        'ISO')
)


process.tagAndProbeMuonHttMu12 = cms.EDAnalyzer("MuonPairTagAndProbePlotter",
    src = cms.InputTag("cleanPatMuons"),
    methods = cms.vstring('pt()>0', 
        'pt()>0'),
    triggers = cms.vstring('hltBLifetimeL3PFFilterSingleTop', 
        'hltIsoMu202p1CentralPFJet30MuCleaned', 
        'hltIsoMu20eta2p1CentralPFJet80MuCleaned', 
        'hltBLifetimeL3PFNoPUFilterSingleTop', 
        'hltIsoMu202p1CentralPFNoPUJet30MuCleaned', 
        'hltIsoMu202p1DiCentralPFJet30MuCleaned', 
        'hltIsoMu202p1DiCentralPFNoPUJet30MuCleaned', 
        'hltIsoMu202p1TriCentralPFJet30MuCleaned', 
        'hltIsoMu202p1CentralPFJet50MuCleaned', 
        'hltIsoMu202p1TriCentralPFNoPUJet30MuCleaned', 
        'hltIsoMu202p1CentralPFNoPUJet50MuCleaned', 
        'hlt2IsoMu20eta2p1PFMHTPt80', 
        'hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f20L3crIsoFiltered10', 
        'hltPFMHT20Filter', 
        'hltIsoMu24eta2p1DiCentralPFJet25MuCleaned', 
        'hltIsoMu24eta2p1PFJet30PFJet25Deta3PFJetCollectionsVBFFilter', 
        'hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10', 
        'hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f30QL3crIsoFiltered10', 
        'hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f34QL3crIsoFiltered10', 
        'hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f40QL3crIsoFiltered10', 
        'hltPFMHT55Filter', 
        'hltPFMHT60Filter', 
        'hltL3L1Mu10erJetC20JetC12Corr1OrL1Mu10erJetC32OrMu10erJetC32JetC12Corr1L3Mufiltered12Eta2p1', 
        'hltBLifetime3D1stTrkL3FilterJet20HbbL1FastJet', 
        'hltDiBLifetime3D1stTrkL3FilterJet20HbbL1FastJet', 
        'hltL3L1Mu10erJetC20JetC12Corr1OrL1Mu10erJetC32OrMu10erJetC32JetC12Corr1L3Mufiltered12Eta2p1', 
        'hltL3L1Mu10erJetC20JetC12Corr1OrL1Mu10erJetC32OrMu10erJetC32JetC12Corr1L3Mufiltered12Eta2p1', 
        'hltL3fL1sMu7L3Filtered12', 
        'hltBLifetime3D1stTrkL3FilterJet20HbbL1FastJet', 
        'hltDiBLifetime3D1stTrkL3FilterJet20HbbL1FastJet', 
        'hltL1Mu10Eta2p1Jet20Jet12CentralCorrOrMu10erJetC32L3Mufiltered15Eta2p1', 
        'hltL3fL1sMu7L1fEta2p1L2fEta2p1f7L3FilteredEta2p1Filtered15', 
        'hltBLifetimeL3PFFilterSingleTopNoIso', 
        'hltBLifetimeL3PFNoPUFilterSingleTopNoIso', 
        'hltMu202p1TriCentralPFJet30MuCleaned', 
        'hltMu202p1CentralPFJet50MuCleaned', 
        'hltMu202p1TriCentralPFNoPUJet30MuCleaned', 
        'hltMu202p1CentralPFNoPUJet50MuCleaned', 
        'hltMu24eta2p1DiCentralPFJet25MuCleaned', 
        'hltMu24eta2p1PFJet30PFJet25Deta3PFJetCollectionsVBFFilter', 
        'hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered24Q', 
        'hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered30Q', 
        'hltDeDxFilter50DEDX3p6Mu', 
        'hltDeDxFilter60DEDX3p7Mu', 
        'hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q', 
        'hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered50Q', 
        'hltL3fL1sMu3L3Filtered5', 
        'hltL3reliso1p0mufiltermu17', 
        'hltL3reliso1p0mufiltermu5'),
    patTrigger = cms.InputTag("patTrigger"),
    vertices = cms.InputTag("primaryVertexFilter"),
    triggersProbe = cms.vstring('hltDoubleMu11ExclL3PreFiltered', 
        'hltDoubleMu4ExclL3PreFiltered', 
        'hltDoubleMu5IsoMu5IsoL3IsoFiltered5', 
        'hltL2DoubleMu23NoVertexL2Filtered2ChaAngle2p5', 
        'hltL2DoubleMu23NoVertexL2PreFiltered', 
        'hltL2DoubleMu38NoVertexL2Filtered2ChaAngle2p5', 
        'hltDiMuonMu17Mu8DzFiltered0p2', 
        'hltDiMuonGlb17Trk8DzFiltered0p2', 
        'hltL3fL1sMu12L3Filtered17', 
        'hltDiMuonGlb22Trk22DzFiltered0p2', 
        'hltDiMuonGlb22Trk8DzFiltered0p2', 
        'hltL3fL1sMu3L3Filtered8', 
        'hltTripleMu0L3TriMuFiltered5'),
    ref = cms.InputTag("selectedTagAndProbeMuTracks"),
    id = cms.vstring('WW', 
        'ISO')
)


process.pfMEtMVAsequence = cms.Sequence(process.calibratedAK5PFJetsForPFMEtMVA+process.pfMEtMVA)


process.saveHistos = cms.Sequence(process.MEtoEDMConverter)


process.selectedObjectsForSyst = cms.Sequence(process.selectedPatTaus+process.selectedPatElectrons+process.selectedPatMuons+process.cleanPatJets)


process.tagAndProbeSequence = cms.Sequence(process.initialTagAndProbeEventsCounter+process.tagAndProbeMuTracks+process.tagAndProbeMuTracksFilter+process.selectedTagAndProbeMuTracks+process.selectedTagAndProbeMuTracksFilter+process.selectedTagAndProbeMuTracksCounter)


process.loadHistos = cms.Sequence(process.EDMtoMEConverter)


process.mvaMetEleTauSequence = cms.Sequence(process.metEleTaus+process.metElectrons+process.mvaMetEleTau+process.patMVAMetEleTau)


process.mvaMetMuTauSequence = cms.Sequence(process.metMuTaus+process.metMuons+process.mvaMetMuTau+process.patMVAMetMuTau)


process.startupSequence = cms.Sequence(process.initialCounter)


process.pfMEtMVA2sequence = cms.Sequence(process.calibratedAK5PFJetsForPFMEtMVA+process.pfMEtMVAData+process.pfMEtMVA2)


process.analysisSequence = cms.Sequence(((((process.triggeredPatMuons)+process.triggeredPatElectronsL+process.triggeredPatElectrons)+process.preTriggeredPatTaus+process.triggeredPatTaus+process.primaryVertexFilter)+process.selectedObjectsForSyst)+process.mvaMetMuTauSequence+process.mvaMetEleTauSequence)


process.startupSequenceFromSkim = cms.Sequence(process.loadHistos)


process.runAnalysisSequence = cms.Path(process.analysisSequence)


process.tagAndProbe = cms.Path(process.tagAndProbeSequence)


process.tagAndProbePathMuonHttMu12 = cms.EndPath(process.tagAndProbeMuonHttMu12)


process.tagAndProbePathMuonHLTMu8ZZ = cms.EndPath(process.tagAndProbeMuonHLTMu8ZZ)


process.summaryPath = cms.EndPath(process.summary)


process.DQM = cms.Service("DQM",
    filter = cms.untracked.string(''),
    publishFrequency = cms.untracked.double(5.0),
    collectorHost = cms.untracked.string('localhost'),
    collectorPort = cms.untracked.int32(9090),
    debug = cms.untracked.bool(False)
)


process.DQMStore = cms.Service("DQMStore",
    verboseQT = cms.untracked.int32(0),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    collateHistograms = cms.untracked.bool(False)
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    horeco = cms.PSet(
        initialSeed = cms.untracked.uint32(541321),
        engineName = cms.untracked.string('TRandom3')
    ),
    paramMuons = cms.PSet(
        initialSeed = cms.untracked.uint32(54525),
        engineName = cms.untracked.string('TRandom3')
    ),
    saveFileName = cms.untracked.string(''),
    hbhereco = cms.PSet(
        initialSeed = cms.untracked.uint32(541321),
        engineName = cms.untracked.string('TRandom3')
    ),
    externalLHEProducer = cms.PSet(
        initialSeed = cms.untracked.uint32(234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    famosPileUp = cms.PSet(
        initialSeed = cms.untracked.uint32(918273),
        engineName = cms.untracked.string('TRandom3')
    ),
    simMuonDTDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    siTrackerGaussianSmearingRecHits = cms.PSet(
        initialSeed = cms.untracked.uint32(24680),
        engineName = cms.untracked.string('TRandom3')
    ),
    ecalPreshowerRecHit = cms.PSet(
        initialSeed = cms.untracked.uint32(6541321),
        engineName = cms.untracked.string('TRandom3')
    ),
    generator = cms.PSet(
        initialSeed = cms.untracked.uint32(123456789),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simMuonRPCDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    hiSignal = cms.PSet(
        initialSeed = cms.untracked.uint32(123456789),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simCastorDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(12345678),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    mix = cms.PSet(
        initialSeed = cms.untracked.uint32(12345),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    VtxSmeared = cms.PSet(
        initialSeed = cms.untracked.uint32(98765432),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    LHCTransport = cms.PSet(
        initialSeed = cms.untracked.uint32(87654321),
        engineName = cms.untracked.string('TRandom3')
    ),
    ecalRecHit = cms.PSet(
        initialSeed = cms.untracked.uint32(654321),
        engineName = cms.untracked.string('TRandom3')
    ),
    hfreco = cms.PSet(
        initialSeed = cms.untracked.uint32(541321),
        engineName = cms.untracked.string('TRandom3')
    ),
    simSiStripDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simEcalUnsuppressedDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    hiSignalG4SimHits = cms.PSet(
        initialSeed = cms.untracked.uint32(11),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    famosSimHits = cms.PSet(
        initialSeed = cms.untracked.uint32(13579),
        engineName = cms.untracked.string('TRandom3')
    ),
    MuonSimHits = cms.PSet(
        initialSeed = cms.untracked.uint32(987346),
        engineName = cms.untracked.string('TRandom3')
    ),
    g4SimHits = cms.PSet(
        initialSeed = cms.untracked.uint32(11),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    hiSignalLHCTransport = cms.PSet(
        initialSeed = cms.untracked.uint32(88776655),
        engineName = cms.untracked.string('TRandom3')
    ),
    mixGenPU = cms.PSet(
        initialSeed = cms.untracked.uint32(918273),
        engineName = cms.untracked.string('TRandom3')
    ),
    l1ParamMuons = cms.PSet(
        initialSeed = cms.untracked.uint32(6453209),
        engineName = cms.untracked.string('TRandom3')
    ),
    simBeamSpotFilter = cms.PSet(
        initialSeed = cms.untracked.uint32(87654321),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simHcalUnsuppressedDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(11223344),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simMuonCSCDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(11223344),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    mixData = cms.PSet(
        initialSeed = cms.untracked.uint32(12345),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simSiPixelDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('HepJamesRandom')
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('analysis.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string(''),
    useDDD = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    alignmentsLabel = cms.string(''),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerHardcodeGeometryEP = cms.ESProducer("CaloTowerHardcodeGeometryEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorHardcodeGeometryEP = cms.ESProducer("CastorHardcodeGeometryEP")


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.EcalBarrelGeometryEP = cms.ESProducer("EcalBarrelGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryEP = cms.ESProducer("EcalEndcapGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryEP = cms.ESProducer("EcalPreshowerGeometryEP",
    applyAlignment = cms.bool(False)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalHardcodeGeometryEP = cms.ESProducer("HcalHardcodeGeometryEP")


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP")


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_8T')
    ),
    label = cms.untracked.string('parametrizedField')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    useDDD = cms.untracked.bool(True),
    compatibiltyWith11 = cms.untracked.bool(True)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle')
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    fromDDD = cms.bool(True)
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991),
    overrideMasterSector = cms.bool(False),
    useParametrizedTrackerField = cms.bool(True),
    label = cms.untracked.string(''),
    version = cms.string('grid_1103l_090322_3_8t'),
    debugBuilder = cms.untracked.bool(False),
    paramLabel = cms.string('parametrizedField'),
    cacheLastVolume = cms.untracked.bool(True)
)


process.ZdcHardcodeGeometryEP = cms.ESProducer("ZdcHardcodeGeometryEP")


process.ak5CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute')
)


process.ak5CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloL6SLB')
)


process.ak5CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloResidual')
)


process.ak5CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet')
)


process.ak5CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Offset', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute')
)


process.ak5CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Offset', 
        'ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloResidual')
)


process.ak5CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset')
)


process.ak5CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL2Relative', 
        'ak5CaloL3Absolute')
)


process.ak5CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloL6SLB')
)


process.ak5CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL2Relative', 
        'ak5CaloL3Absolute', 
        'ak5CaloResidual')
)


process.ak5CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak5CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak5CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("ak5CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak5CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.ak5CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak5JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5JPTL1Fastjet', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute')
)


process.ak5JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5JPTL1Fastjet', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute', 
        'ak5JPTResidual')
)


process.ak5JPTL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet')
)


process.ak5JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute')
)


process.ak5JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute', 
        'ak5JPTResidual')
)


process.ak5JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1Offset')
)


process.ak5JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute')
)


process.ak5JPTL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5L1JPTOffset', 
        'ak5JPTL2Relative', 
        'ak5JPTL3Absolute', 
        'ak5JPTResidual')
)


process.ak5JPTL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2Relative')
)


process.ak5JPTL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L3Absolute')
)


process.ak5JPTResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2L3Residual')
)


process.ak5L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    offsetService = cms.string('ak5CaloL1Offset'),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset')
)


process.ak5PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFL6SLB')
)


process.ak5PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6PFJets","rho"),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet')
)


process.ak5PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset')
)


process.ak5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFL6SLB')
)


process.ak5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("ak5PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak5PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.ak5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.ak5TrackL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak5TrackL2Relative', 
        'ak5TrackL3Absolute')
)


process.ak5TrackL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5TrackL2Relative', 
        'ak5TrackL3Absolute')
)


process.ak5TrackL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L2Relative')
)


process.ak5TrackL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet')
)


process.ak7CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset')
)


process.ak7CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.ak7CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7JPTL1Fastjet', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet')
)


process.ak7JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset')
)


process.ak7JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    offsetService = cms.string('ak5CaloL1Offset'),
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset')
)


process.ak7PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6PFJets","rho"),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet')
)


process.ak7PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset')
)


process.ak7PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.ak7PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    file = cms.untracked.string(''),
    dump = cms.untracked.vstring('')
)


process.ic5CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet')
)


process.ic5CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset')
)


process.ic5CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.ic5CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6PFJets","rho"),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet')
)


process.ic5PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset')
)


process.ic5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.ic5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    useDDD = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    alignmentsLabel = cms.string('fakeForIdeal'),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(False)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string('fakeForIdeal')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    appendToDataLabel = cms.string('idealForDigi'),
    fromDDD = cms.bool(True),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string('fakeForIdeal')
)


process.kt4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet')
)


process.kt4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset')
)


process.kt4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.kt4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6PFJets","rho"),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet')
)


process.kt4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset')
)


process.kt4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.kt4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6CaloJets","rho"),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet')
)


process.kt6CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset')
)


process.kt6CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.kt6CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6PFJets","rho"),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet')
)


process.kt6PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices'),
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset')
)


process.kt6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos"),
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB')
)


process.kt6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    printDebug = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    APVGain = cms.VPSet(cms.PSet(
        Record = cms.string('SiStripApvGainRcd'),
        NormalizationFactor = cms.untracked.double(1.0),
        Label = cms.untracked.string('')
    ), 
        cms.PSet(
            Record = cms.string('SiStripApvGain2Rcd'),
            NormalizationFactor = cms.untracked.double(1.0),
            Label = cms.untracked.string('')
        )),
    AutomaticNormalization = cms.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        record = cms.string('SiStripLatencyRcd'),
        label = cms.untracked.string('')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('deconvolution')
    ),
    LorentzAnglePeakMode = cms.PSet(
        record = cms.string('SiStripLorentzAngleRcd'),
        label = cms.untracked.string('peak')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    appendToDataLabel = cms.string(''),
    PrintDebugOutput = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        ))
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        connectionRetrialPeriod = cms.untracked.int32(10)
    ),
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    toGet = cms.VPSet(),
    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
    globaltag = cms.string('START52_V9::All')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml', 
        'Geometry/CMSCommonData/data/rotations.xml', 
        'Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMother.xml', 
        'Geometry/CMSCommonData/data/cmsTracker.xml', 
        'Geometry/CMSCommonData/data/caloBase.xml', 
        'Geometry/CMSCommonData/data/cmsCalo.xml', 
        'Geometry/CMSCommonData/data/muonBase.xml', 
        'Geometry/CMSCommonData/data/cmsMuon.xml', 
        'Geometry/CMSCommonData/data/mgnt.xml', 
        'Geometry/CMSCommonData/data/beampipe.xml', 
        'Geometry/CMSCommonData/data/cmsBeam.xml', 
        'Geometry/CMSCommonData/data/muonMB.xml', 
        'Geometry/CMSCommonData/data/muonMagnet.xml', 
        'Geometry/TrackerCommonData/data/pixfwdMaterials.xml', 
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x2.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq1x5.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x3.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x4.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPlaq2x5.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPanelBase.xml', 
        'Geometry/TrackerCommonData/data/pixfwdPanel.xml', 
        'Geometry/TrackerCommonData/data/pixfwdBlade.xml', 
        'Geometry/TrackerCommonData/data/pixfwdNipple.xml', 
        'Geometry/TrackerCommonData/data/pixfwdDisk.xml', 
        'Geometry/TrackerCommonData/data/pixfwdCylinder.xml', 
        'Geometry/TrackerCommonData/data/pixfwd.xml', 
        'Geometry/TrackerCommonData/data/pixbarmaterial.xml', 
        'Geometry/TrackerCommonData/data/pixbarladder.xml', 
        'Geometry/TrackerCommonData/data/pixbarladderfull.xml', 
        'Geometry/TrackerCommonData/data/pixbarladderhalf.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer0.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer1.xml', 
        'Geometry/TrackerCommonData/data/pixbarlayer2.xml', 
        'Geometry/TrackerCommonData/data/pixbar.xml', 
        'Geometry/TrackerCommonData/data/tibtidcommonmaterial.xml', 
        'Geometry/TrackerCommonData/data/tibmaterial.xml', 
        'Geometry/TrackerCommonData/data/tibmodpar.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0a.xml', 
        'Geometry/TrackerCommonData/data/tibmodule0b.xml', 
        'Geometry/TrackerCommonData/data/tibmodule2.xml', 
        'Geometry/TrackerCommonData/data/tibstringpar.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring0lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring0ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring0.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring1lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring1ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring1.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring2lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring2ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring2.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ll.xml', 
        'Geometry/TrackerCommonData/data/tibstring3lr.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ul.xml', 
        'Geometry/TrackerCommonData/data/tibstring3ur.xml', 
        'Geometry/TrackerCommonData/data/tibstring3.xml', 
        'Geometry/TrackerCommonData/data/tiblayerpar.xml', 
        'Geometry/TrackerCommonData/data/tiblayer0.xml', 
        'Geometry/TrackerCommonData/data/tiblayer1.xml', 
        'Geometry/TrackerCommonData/data/tiblayer2.xml', 
        'Geometry/TrackerCommonData/data/tiblayer3.xml', 
        'Geometry/TrackerCommonData/data/tib.xml', 
        'Geometry/TrackerCommonData/data/tidmaterial.xml', 
        'Geometry/TrackerCommonData/data/tidmodpar.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0r.xml', 
        'Geometry/TrackerCommonData/data/tidmodule0l.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1r.xml', 
        'Geometry/TrackerCommonData/data/tidmodule1l.xml', 
        'Geometry/TrackerCommonData/data/tidmodule2.xml', 
        'Geometry/TrackerCommonData/data/tidringpar.xml', 
        'Geometry/TrackerCommonData/data/tidring0.xml', 
        'Geometry/TrackerCommonData/data/tidring0f.xml', 
        'Geometry/TrackerCommonData/data/tidring0b.xml', 
        'Geometry/TrackerCommonData/data/tidring1.xml', 
        'Geometry/TrackerCommonData/data/tidring1f.xml', 
        'Geometry/TrackerCommonData/data/tidring1b.xml', 
        'Geometry/TrackerCommonData/data/tidring2.xml', 
        'Geometry/TrackerCommonData/data/tid.xml', 
        'Geometry/TrackerCommonData/data/tidf.xml', 
        'Geometry/TrackerCommonData/data/tidb.xml', 
        'Geometry/TrackerCommonData/data/tibtidservices.xml', 
        'Geometry/TrackerCommonData/data/tibtidservicesf.xml', 
        'Geometry/TrackerCommonData/data/tibtidservicesb.xml', 
        'Geometry/TrackerCommonData/data/tobmaterial.xml', 
        'Geometry/TrackerCommonData/data/tobmodpar.xml', 
        'Geometry/TrackerCommonData/data/tobmodule0.xml', 
        'Geometry/TrackerCommonData/data/tobmodule2.xml', 
        'Geometry/TrackerCommonData/data/tobmodule4.xml', 
        'Geometry/TrackerCommonData/data/tobrodpar.xml', 
        'Geometry/TrackerCommonData/data/tobrod0c.xml', 
        'Geometry/TrackerCommonData/data/tobrod0l.xml', 
        'Geometry/TrackerCommonData/data/tobrod0h.xml', 
        'Geometry/TrackerCommonData/data/tobrod0.xml', 
        'Geometry/TrackerCommonData/data/tobrod1l.xml', 
        'Geometry/TrackerCommonData/data/tobrod1h.xml', 
        'Geometry/TrackerCommonData/data/tobrod1.xml', 
        'Geometry/TrackerCommonData/data/tobrod2c.xml', 
        'Geometry/TrackerCommonData/data/tobrod2l.xml', 
        'Geometry/TrackerCommonData/data/tobrod2h.xml', 
        'Geometry/TrackerCommonData/data/tobrod2.xml', 
        'Geometry/TrackerCommonData/data/tobrod3l.xml', 
        'Geometry/TrackerCommonData/data/tobrod3h.xml', 
        'Geometry/TrackerCommonData/data/tobrod3.xml', 
        'Geometry/TrackerCommonData/data/tobrod4c.xml', 
        'Geometry/TrackerCommonData/data/tobrod4l.xml', 
        'Geometry/TrackerCommonData/data/tobrod4h.xml', 
        'Geometry/TrackerCommonData/data/tobrod4.xml', 
        'Geometry/TrackerCommonData/data/tobrod5l.xml', 
        'Geometry/TrackerCommonData/data/tobrod5h.xml', 
        'Geometry/TrackerCommonData/data/tobrod5.xml', 
        'Geometry/TrackerCommonData/data/tob.xml', 
        'Geometry/TrackerCommonData/data/tecmaterial.xml', 
        'Geometry/TrackerCommonData/data/tecmodpar.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule0s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule1s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule2.xml', 
        'Geometry/TrackerCommonData/data/tecmodule3.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4r.xml', 
        'Geometry/TrackerCommonData/data/tecmodule4s.xml', 
        'Geometry/TrackerCommonData/data/tecmodule5.xml', 
        'Geometry/TrackerCommonData/data/tecmodule6.xml', 
        'Geometry/TrackerCommonData/data/tecpetpar.xml', 
        'Geometry/TrackerCommonData/data/tecring0.xml', 
        'Geometry/TrackerCommonData/data/tecring1.xml', 
        'Geometry/TrackerCommonData/data/tecring2.xml', 
        'Geometry/TrackerCommonData/data/tecring3.xml', 
        'Geometry/TrackerCommonData/data/tecring4.xml', 
        'Geometry/TrackerCommonData/data/tecring5.xml', 
        'Geometry/TrackerCommonData/data/tecring6.xml', 
        'Geometry/TrackerCommonData/data/tecring0f.xml', 
        'Geometry/TrackerCommonData/data/tecring1f.xml', 
        'Geometry/TrackerCommonData/data/tecring2f.xml', 
        'Geometry/TrackerCommonData/data/tecring3f.xml', 
        'Geometry/TrackerCommonData/data/tecring4f.xml', 
        'Geometry/TrackerCommonData/data/tecring5f.xml', 
        'Geometry/TrackerCommonData/data/tecring6f.xml', 
        'Geometry/TrackerCommonData/data/tecring0b.xml', 
        'Geometry/TrackerCommonData/data/tecring1b.xml', 
        'Geometry/TrackerCommonData/data/tecring2b.xml', 
        'Geometry/TrackerCommonData/data/tecring3b.xml', 
        'Geometry/TrackerCommonData/data/tecring4b.xml', 
        'Geometry/TrackerCommonData/data/tecring5b.xml', 
        'Geometry/TrackerCommonData/data/tecring6b.xml', 
        'Geometry/TrackerCommonData/data/tecpetalf.xml', 
        'Geometry/TrackerCommonData/data/tecpetalb.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal0b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal3b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal6f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal6b.xml', 
        'Geometry/TrackerCommonData/data/tecpetal8f.xml', 
        'Geometry/TrackerCommonData/data/tecpetal8b.xml', 
        'Geometry/TrackerCommonData/data/tecwheel.xml', 
        'Geometry/TrackerCommonData/data/tecwheela.xml', 
        'Geometry/TrackerCommonData/data/tecwheelb.xml', 
        'Geometry/TrackerCommonData/data/tecwheelc.xml', 
        'Geometry/TrackerCommonData/data/tecwheeld.xml', 
        'Geometry/TrackerCommonData/data/tecwheel6.xml', 
        'Geometry/TrackerCommonData/data/tecservices.xml', 
        'Geometry/TrackerCommonData/data/tecbackplate.xml', 
        'Geometry/TrackerCommonData/data/tec.xml', 
        'Geometry/TrackerCommonData/data/trackermaterial.xml', 
        'Geometry/TrackerCommonData/data/tracker.xml', 
        'Geometry/TrackerCommonData/data/trackerpixbar.xml', 
        'Geometry/TrackerCommonData/data/trackerpixfwd.xml', 
        'Geometry/TrackerCommonData/data/trackertibtidservices.xml', 
        'Geometry/TrackerCommonData/data/trackertib.xml', 
        'Geometry/TrackerCommonData/data/trackertid.xml', 
        'Geometry/TrackerCommonData/data/trackertob.xml', 
        'Geometry/TrackerCommonData/data/trackertec.xml', 
        'Geometry/TrackerCommonData/data/trackerbulkhead.xml', 
        'Geometry/TrackerCommonData/data/trackerother.xml', 
        'Geometry/EcalCommonData/data/eregalgo.xml', 
        'Geometry/EcalCommonData/data/ebalgo.xml', 
        'Geometry/EcalCommonData/data/ebcon.xml', 
        'Geometry/EcalCommonData/data/ebrot.xml', 
        'Geometry/EcalCommonData/data/eecon.xml', 
        'Geometry/EcalCommonData/data/eefixed.xml', 
        'Geometry/EcalCommonData/data/eehier.xml', 
        'Geometry/EcalCommonData/data/eealgo.xml', 
        'Geometry/EcalCommonData/data/escon.xml', 
        'Geometry/EcalCommonData/data/esalgo.xml', 
        'Geometry/EcalCommonData/data/eeF.xml', 
        'Geometry/EcalCommonData/data/eeB.xml', 
        'Geometry/HcalCommonData/data/hcalrotations.xml', 
        'Geometry/HcalCommonData/data/hcalalgo.xml', 
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml', 
        'Geometry/HcalCommonData/data/hcalendcapalgo.xml', 
        'Geometry/HcalCommonData/data/hcalouteralgo.xml', 
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml', 
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml', 
        'Geometry/MuonCommonData/data/mbCommon.xml', 
        'Geometry/MuonCommonData/data/mb1.xml', 
        'Geometry/MuonCommonData/data/mb2.xml', 
        'Geometry/MuonCommonData/data/mb3.xml', 
        'Geometry/MuonCommonData/data/mb4.xml', 
        'Geometry/MuonCommonData/data/muonYoke.xml', 
        'Geometry/MuonCommonData/data/mf.xml', 
        'Geometry/ForwardCommonData/data/forward.xml', 
        'Geometry/ForwardCommonData/data/bundle/forwardshield.xml', 
        'Geometry/ForwardCommonData/data/brmrotations.xml', 
        'Geometry/ForwardCommonData/data/brm.xml', 
        'Geometry/ForwardCommonData/data/totemMaterials.xml', 
        'Geometry/ForwardCommonData/data/totemRotations.xml', 
        'Geometry/ForwardCommonData/data/totemt1.xml', 
        'Geometry/ForwardCommonData/data/totemt2.xml', 
        'Geometry/ForwardCommonData/data/ionpump.xml', 
        'Geometry/MuonCommonData/data/muonNumbering.xml', 
        'Geometry/TrackerCommonData/data/trackerStructureTopology.xml', 
        'Geometry/TrackerSimData/data/trackersens.xml', 
        'Geometry/TrackerRecoData/data/trackerRecoMaterial.xml', 
        'Geometry/EcalSimData/data/ecalsens.xml', 
        'Geometry/HcalCommonData/data/hcalsenspmf.xml', 
        'Geometry/HcalSimData/data/hf.xml', 
        'Geometry/HcalSimData/data/hfpmt.xml', 
        'Geometry/HcalSimData/data/hffibrebundle.xml', 
        'Geometry/HcalSimData/data/CaloUtil.xml', 
        'Geometry/MuonSimData/data/muonSens.xml', 
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml', 
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml', 
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml', 
        'Geometry/RPCGeometryBuilder/data/RPCSpecs.xml', 
        'Geometry/ForwardCommonData/data/brmsens.xml', 
        'Geometry/HcalSimData/data/HcalProdCuts.xml', 
        'Geometry/EcalSimData/data/EcalProdCuts.xml', 
        'Geometry/EcalSimData/data/ESProdCuts.xml', 
        'Geometry/TrackerSimData/data/trackerProdCuts.xml', 
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml', 
        'Geometry/MuonSimData/data/muonProdCuts.xml', 
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml', 
        'Geometry/CMSCommonData/data/FieldParameters.xml'),
    rootNodeName = cms.string('cms:OCMS')
)


process.eegeom = cms.ESSource("EmptyESSource",
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd'),
    firstValid = cms.vuint32(1)
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    toGet = cms.untracked.vstring('GainWidths')
)


process.magfield = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMagneticField.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml', 
        'MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml', 
        'Geometry/CMSCommonData/data/materials.xml'),
    rootNodeName = cms.string('cmsMagneticField:MAGF')
)


process.prefer("magfield")

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableConnectionSharing = cms.untracked.bool(True),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        connectionRetrialPeriod = cms.untracked.int32(10)
    )
)

process.JetIdParams = cms.PSet(
    Pt2030_Tight = cms.vdouble(0.3, 0.4, 0.7, 0.8),
    Pt2030_Loose = cms.vdouble(0.0, 0.0, 0.2, 0.6),
    Pt3050_Medium = cms.vdouble(0.3, 0.2, 0.7, 0.8),
    Pt1020_Tight = cms.vdouble(-0.2, 0.2, 0.2, 0.6),
    Pt2030_Medium = cms.vdouble(0.2, 0.2, 0.5, 0.7),
    Pt010_Tight = cms.vdouble(0.5, 0.6, 0.6, 0.9),
    Pt1020_Loose = cms.vdouble(-0.4, -0.4, -0.4, 0.4),
    Pt010_Medium = cms.vdouble(0.2, 0.4, 0.2, 0.6),
    Pt1020_Medium = cms.vdouble(-0.3, 0.0, 0.0, 0.5),
    Pt010_Loose = cms.vdouble(0.0, 0.0, 0.0, 0.2),
    Pt3050_Loose = cms.vdouble(0.0, 0.0, 0.6, 0.2),
    Pt3050_Tight = cms.vdouble(0.5, 0.4, 0.8, 0.9)
)

process.fieldScaling = cms.PSet(
    scalingVolumes = cms.vint32(14100, 14200, 17600, 17800, 17900, 
        18100, 18300, 18400, 18600, 23100, 
        23300, 23400, 23600, 23800, 23900, 
        24100, 28600, 28800, 28900, 29100, 
        29300, 29400, 29600, 28609, 28809, 
        28909, 29109, 29309, 29409, 29609, 
        28610, 28810, 28910, 29110, 29310, 
        29410, 29610, 28611, 28811, 28911, 
        29111, 29311, 29411, 29611),
    scalingFactors = cms.vdouble(1, 1, 0.994, 1.004, 1.004, 
        1.005, 1.004, 1.004, 0.994, 0.965, 
        0.958, 0.958, 0.953, 0.958, 0.958, 
        0.965, 0.918, 0.924, 0.924, 0.906, 
        0.924, 0.924, 0.918, 0.991, 0.998, 
        0.998, 0.978, 0.998, 0.998, 0.991, 
        0.991, 0.998, 0.998, 0.978, 0.998, 
        0.998, 0.991, 0.991, 0.998, 0.998, 
        0.978, 0.998, 0.998, 0.991)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.metCalibration = cms.PSet(
    responseMCU2 = cms.string('-0.00544907'),
    resolutionMCU2 = cms.string('10.5649+0.0225853*x-5.81371e-5*x*x'),
    resolutionMCU1 = cms.string('10.6449+0.0436475*x+3.07554e-5*x*x'),
    responseMCU1 = cms.string('1.26247-0.950094*x'),
    responseU1 = cms.string('1.33223-0.917782*x'),
    responseU2 = cms.string('-0.013'),
    applyCalibration = cms.bool(False),
    calibrationScheme = cms.string('BothLegs'),
    resolutionU1 = cms.string('11.1566+0.0654529*x+0.000124436*x*x'),
    resolutionU2 = cms.string('11.1235+0.0449872*x-6.39822e-5*x*x')
)

process.svFitLikelihoodEleMuKinematicsPhaseSpace = cms.PSet(
    leg1 = cms.PSet(
        pluginType = cms.string('SVfitElectronLikelihoodPhaseSpace')
    ),
    leg2 = cms.PSet(
        pluginType = cms.string('SVfitMuonLikelihoodPhaseSpace')
    ),
    pluginType = cms.string('SVfitLikelihoodElecMuPairKinematics'),
    firstFitIteration = cms.uint32(0),
    pluginName = cms.string('svFitLikelihoodDiTauKinematicsPhaseSpace')
)

process.svFitLikelihoodEleMuMEt = cms.PSet(
    pluginName = cms.string('svFitLikelihoodMEt'),
    pluginType = cms.string('SVfitLikelihoodMEtElecMu'),
    resolution = cms.PSet(
        parBias = cms.string('-0.96'),
        parSigma = cms.string('7.54*(1 - 0.00542*x)'),
        perpBias = cms.string('0.'),
        perpSigma = cms.string('6.85*(1 - 0.00547*x)')
    ),
    srcPFCandidates = cms.InputTag("particleFlow"),
    firstFitIteration = cms.uint32(0)
)

process.svFitLikelihoodEleMuPtBalance = cms.PSet(
    pluginName = cms.string('svFitLikelihoodDiTauPtBalance'),
    pluginType = cms.string('SVfitLikelihoodElecMuPairPtBalance'),
    firstFitIteration = cms.uint32(0)
)

process.svFitLikelihoodEleTauKinematicsPhaseSpace = cms.PSet(
    leg1 = cms.PSet(
        pluginType = cms.string('SVfitElectronLikelihoodPhaseSpace')
    ),
    leg2 = cms.PSet(
        pluginType = cms.string('SVfitTauLikelihoodPhaseSpace')
    ),
    pluginType = cms.string('SVfitLikelihoodElecTauPairKinematics'),
    firstFitIteration = cms.uint32(0),
    pluginName = cms.string('svFitLikelihoodDiTauKinematicsPhaseSpace')
)

process.svFitLikelihoodEleTauMEt = cms.PSet(
    pluginName = cms.string('svFitLikelihoodMEt'),
    pluginType = cms.string('SVfitLikelihoodMEtElecTau'),
    resolution = cms.PSet(
        parBias = cms.string('-0.96'),
        parSigma = cms.string('7.54*(1 - 0.00542*x)'),
        perpBias = cms.string('0.'),
        perpSigma = cms.string('6.85*(1 - 0.00547*x)')
    ),
    srcPFCandidates = cms.InputTag("particleFlow"),
    firstFitIteration = cms.uint32(0)
)

process.svFitLikelihoodEleTauPtBalance = cms.PSet(
    pluginName = cms.string('svFitLikelihoodDiTauPtBalance'),
    pluginType = cms.string('SVfitLikelihoodElecTauPairPtBalance'),
    firstFitIteration = cms.uint32(0)
)

process.svFitLikelihoodMuMuKinematicsPhaseSpace = cms.PSet(
    leg1 = cms.PSet(
        pluginType = cms.string('SVfitMuonLikelihoodPhaseSpace')
    ),
    leg2 = cms.PSet(
        pluginType = cms.string('SVfitMuonLikelihoodPhaseSpace')
    ),
    pluginType = cms.string('SVfitLikelihoodMuPairKinematics'),
    firstFitIteration = cms.uint32(0),
    pluginName = cms.string('svFitLikelihoodDiTauKinematicsPhaseSpace')
)

process.svFitLikelihoodMuMuMEt = cms.PSet(
    pluginName = cms.string('svFitLikelihoodMEt'),
    pluginType = cms.string('SVfitLikelihoodMEtMuMu'),
    resolution = cms.PSet(
        parBias = cms.string('-0.96'),
        parSigma = cms.string('7.54*(1 - 0.00542*x)'),
        perpBias = cms.string('0.'),
        perpSigma = cms.string('6.85*(1 - 0.00547*x)')
    ),
    srcPFCandidates = cms.InputTag("particleFlow"),
    firstFitIteration = cms.uint32(0)
)

process.svFitLikelihoodMuMuPtBalance = cms.PSet(
    pluginName = cms.string('svFitLikelihoodDiTauPtBalance'),
    pluginType = cms.string('SVfitLikelihoodMuPairPtBalance'),
    firstFitIteration = cms.uint32(0)
)

process.svFitLikelihoodMuTauKinematicsPhaseSpace = cms.PSet(
    leg1 = cms.PSet(
        pluginType = cms.string('SVfitMuonLikelihoodPhaseSpace')
    ),
    leg2 = cms.PSet(
        pluginType = cms.string('SVfitTauLikelihoodPhaseSpace')
    ),
    pluginType = cms.string('SVfitLikelihoodMuTauPairKinematics'),
    firstFitIteration = cms.uint32(0),
    pluginName = cms.string('svFitLikelihoodDiTauKinematicsPhaseSpace')
)

process.svFitLikelihoodMuTauMEt = cms.PSet(
    pluginName = cms.string('svFitLikelihoodMEt'),
    pluginType = cms.string('SVfitLikelihoodMEtMuTau'),
    resolution = cms.PSet(
        parBias = cms.string('-0.96'),
        parSigma = cms.string('7.54*(1 - 0.00542*x)'),
        perpBias = cms.string('0.'),
        perpSigma = cms.string('6.85*(1 - 0.00547*x)')
    ),
    srcPFCandidates = cms.InputTag("particleFlow"),
    firstFitIteration = cms.uint32(0)
)

process.svFitLikelihoodMuTauPtBalance = cms.PSet(
    pluginName = cms.string('svFitLikelihoodDiTauPtBalance'),
    pluginType = cms.string('SVfitLikelihoodMuTauPairPtBalance'),
    firstFitIteration = cms.uint32(0)
)

