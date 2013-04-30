
#rm -rf DYmumu/
#mkdir DYmumu/
#mkdir DYmumu/IndividualFits/
#mkdir DYmumu/SummaryPlots/
#mkdir DYmumu/IndividualFits/IsoMu-ID/
#mkdir DYmumu/IndividualFits/NonIsoMu-ID/
#mkdir DYmumu/IndividualFits/NonIsoMuPS-ID/
#mkdir DYmumu/IndividualFits/IsoMu-ISO/
#mkdir DYmumu/IndividualFits/NonIsoMuPS-ISO/
#mkdir DYmumu/IndividualFits/NonIsoMu-ISO/
#mkdir DYmumu/IndividualFits/IsoMu-Trigger/
#mkdir DYmumu/IndividualFits/NonIsoMuPS-Trigger/
#mkdir DYmumu/IndividualFits/NonIsoMu-Trigger/
#mkdir DYmumu/IndividualFits/IsoMu-Combined/
#mkdir DYmumu/IndividualFits/NonIsoMuPS-Combined/
#mkdir DYmumu/IndividualFits/NonIsoMu-Combined/
#mkdir DYmumu/SummaryPlots/IsoMu-ID/
#mkdir DYmumu/SummaryPlots/NonIsoMu-ID/
#mkdir DYmumu/SummaryPlots/NonIsoMuPS-ID/
#mkdir DYmumu/SummaryPlots/IsoMu-ISO/
#mkdir DYmumu/SummaryPlots/NonIsoMuPS-ISO/
#mkdir DYmumu/SummaryPlots/NonIsoMu-ISO/
#mkdir DYmumu/SummaryPlots/IsoMu-Trigger/
#mkdir DYmumu/SummaryPlots/NonIsoMuPS-Trigger/
#mkdir DYmumu/SummaryPlots/NonIsoMu-Trigger/
#mkdir DYmumu/SummaryPlots/IsoMu-Combined/
#mkdir DYmumu/SummaryPlots/NonIsoMuPS-Combined/
#mkdir DYmumu/SummaryPlots/NonIsoMu-Combined/
#mkdir DYmumu/SummaryPlots/Tables/

# IsoMu
echo "processing IsoMu"
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeIsoMu/tagAndProbeTree IsoMu-ID "IDPass==1" "IDPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeIsoMu/tagAndProbeTree IsoMu-ISO "ISOPass==1" "ISOPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeIsoMu/tagAndProbeTree IsoMu-Trigger "hltPass==1" "hltPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeIsoMu/tagAndProbeTree IsoMu-Combined "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt

echo "processing NonIsoMuPS"
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeNonIsoMuPS/tagAndProbeTree NonIsoMuPS-ID "IDPass==1" "IDPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeNonIsoMuPS/tagAndProbeTree NonIsoMuPS-ISO "ISOPass==1" "ISOPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeNonIsoMuPS/tagAndProbeTree NonIsoMuPS-Trigger "hltPass==1" "hltPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeNonIsoMuPS/tagAndProbeTree NonIsoMuPS-Combined "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt

echo "processing NonIsoMu"
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeNonIsoMu/tagAndProbeTree NonIsoMu-ID "IDPass==1" "IDPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeNonIsoMu/tagAndProbeTree NonIsoMu-ISO "ISOPass==1" "ISOPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeNonIsoMu/tagAndProbeTree NonIsoMu-Trigger "hltPass==1" "hltPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_isomu_mc-TP-ISO_MU/  /scratch/stephane/TP_dimuon_isomu_data_combined/ZMuMuData.root tagAndProbeNonIsoMu/tagAndProbeTree NonIsoMu-Combined "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" TPIsoMuPtEtaConfig.txt > IsoMu_outupt.txt

cd DYmumu/SummaryPlots/Tables
latex efficienciesDYmumu-IsoMu-ID.tex
dvips -o efficienciesDYmumu-IsoMu-ID.ps efficienciesDYmumu-IsoMu-ID.dvi
latex efficienciesDYmumu-NonIsoMuPS-ID.tex
dvips -o efficienciesDYmumu-NonIsoMuPS-ID.ps efficienciesDYmumu-NonIsoMuPS-ID.dvi
latex efficienciesDYmumu-NonIsoMu-ID.tex
dvips -o efficienciesDYmumu-NonIsoMu-ID.ps efficienciesDYmumu-NonIsoMu-ID.dvi
latex efficienciesDYmumu-IsoMu-ISO.tex
dvips -o efficienciesDYmumu-IsoMu-ISO.ps efficienciesDYmumu-IsoMu-ISO.dvi
latex efficienciesDYmumu-NonIsoMuPS-ISO.tex
dvips -o efficienciesDYmumu-NonIsoMuPS-ISO.ps efficienciesDYmumu-NonIsoMuPS-ISO.dvi
latex efficienciesDYmumu-NonIsoMu-ISO.tex
dvips -o efficienciesDYmumu-NonIsoMu-ISO.ps efficienciesDYmumu-NonIsoMu-ISO.dvi
latex efficienciesDYmumu-IsoMu-Trigger.tex
dvips -o efficienciesDYmumu-IsoMu-Trigger.ps efficienciesDYmumu-IsoMu-Trigger.dvi
latex efficienciesDYmumu-NonIsoMuPS-Trigger.tex
dvips -o efficienciesDYmumu-NonIsoMuPS-Trigger.ps efficienciesDYmumu-NonIsoMuPS-Trigger.dvi
latex efficienciesDYmumu-NonIsoMu-Trigger.tex
dvips -o efficienciesDYmumu-NonIsoMu-Trigger.ps efficienciesDYmumu-NonIsoMu-Trigger.dvi
latex efficienciesDYmumu-IsoMu-Combined.tex
dvips -o efficienciesDYmumu-IsoMu-Combined.ps efficienciesDYmumu-IsoMu-Combined.dvi
latex efficienciesDYmumu-NonIsoMuPS-Combined.tex
dvips -o efficienciesDYmumu-NonIsoMuPS-Combined.ps efficienciesDYmumu-NonIsoMuPS-Combined.dvi
latex efficienciesDYmumu-NonIsoMu-Combined.tex
dvips -o efficienciesDYmumu-NonIsoMu-Combined.ps efficienciesDYmumu-NonIsoMu-Combined.dvi


#rm *.tex
rm *.dvi
rm *.aux
rm *.log
cd ../../..