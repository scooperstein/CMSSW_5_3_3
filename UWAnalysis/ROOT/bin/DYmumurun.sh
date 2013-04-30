rm DYmumutest.txt
rm *.dvi
rm -rf DYmumu/
mkdir DYmumu/
mkdir DYmumu/IndividualFits/
mkdir DYmumu/SummaryPlots/
mkdir DYmumu/IndividualFits/ID/
mkdir DYmumu/IndividualFits/SIP/
mkdir DYmumu/IndividualFits/ISO/
mkdir DYmumu/IndividualFits/Combined/
mkdir DYmumu/IndividualFits/Trigger8GeV/
mkdir DYmumu/IndividualFits/Trigger17GeV/
mkdir DYmumu/SummaryPlots/ID/
mkdir DYmumu/SummaryPlots/SIP/
mkdir DYmumu/SummaryPlots/ISO/
mkdir DYmumu/SummaryPlots/Combined/
mkdir DYmumu/SummaryPlots/Trigger8GeV/
mkdir DYmumu/SummaryPlots/Trigger17GeV/
mkdir DYmumu/SummaryPlots/Tables/

TagAndProbeMCEtaBins DYmumu /scratch/aglevine/ZMuMuMC/  /scratch/aglevine/ZMuMuData/ZMuMuTP-Aug-22-2012.root tagAndProbeMuonHttMu12/tagAndProbeTree ID "IDPass==1" "IDPass==0" DYmumuPtEtaConfig.txt >> DYmumutest.txt
TagAndProbeMCEtaBins DYmumu /scratch/aglevine/ZMuMuMC/  /scratch/aglevine/ZMuMuData/ZMuMuTP-Aug-22-2012.root tagAndProbeMuonHttMu12/tagAndProbeTree SIP "SIPPass==1" "SIPPass==0" DYmumuPtEtaConfig.txt >> DYmumutest.txt
TagAndProbeMCEtaBins DYmumu /scratch/aglevine/ZMuMuMC/  /scratch/aglevine/ZMuMuData/ZMuMuTP-Aug-22-2012.root tagAndProbeMuonHttMu12/tagAndProbeTree ISO "ISOPass==1" "ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumutest.txt
TagAndProbeMCEtaBins DYmumu /scratch/aglevine/ZMuMuMC/  /scratch/aglevine/ZMuMuData/ZMuMuTP-Aug-22-2012.root tagAndProbeMuonHttMu12/tagAndProbeTree Combined "IDPass==1&&SIPPass==1&&ISOPass==1" "IDPass==0||SIPPass==0||ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumutest.txt
TagAndProbeMCEtaBins DYmumu /scratch/aglevine/ZMuMuMC/  /scratch/aglevine/ZMuMuData/ZMuMuTP-Aug-22-2012.root tagAndProbeMuonHttMu12GeV8/tagAndProbeTree Trigger8GeV "hltPass==1" "hltPass==0" DYmumuPtEtaConfig.txt >> DYmumutest.txt
TagAndProbeMCEtaBins DYmumu /scratch/aglevine/ZMuMuMC/  /scratch/aglevine/ZMuMuData/ZMuMuTP-Aug-22-2012.root tagAndProbeMuonHttMu12GeV17/tagAndProbeTree Trigger17GeV "hltPass==1" "hltPass==0" DYmumuPtEtaConfig.txt >> DYmumutest.txt

cd DYmumu/SummaryPlots/Tables
latex efficienciesDYmumu-ID.tex
dvips -o efficienciesDYmumu-ID.ps efficienciesDYmumu-ID.dvi
latex efficienciesDYmumu-SIP.tex
dvips -o efficienciesDYmumu-SIP.ps efficienciesDYmumu-SIP.dvi
latex efficienciesDYmumu-ISO.tex
dvips -o efficienciesDYmumu-ISO.ps efficienciesDYmumu-ISO.dvi
latex efficienciesDYmumu-Combined.tex
dvips -o efficienciesDYmumu-Combined.ps efficienciesDYmumu-Combined.dvi
latex efficienciesDYmumu-Trigger8GeV.tex
dvips -o efficienciesDYmumu-Trigger8GeV.ps efficienciesDYmumu-Trigger8GeV.dvi
latex efficienciesDYmumu-Trigger17GeV.tex
dvips -o efficienciesDYmumu-Trigger17GeV.ps efficienciesDYmumu-Trigger17GeV.dvi

rm *.dvi
rm *.aux
rm *.log
cd ../../..

