# remove previous output
rm DYee_output.txt
rm -r DYee
mkdir DYee/
mkdir DYee/IndividualFits/
mkdir DYee/SummaryPlots/
mkdir DYee/IndividualFits/ID/
mkdir DYee/IndividualFits/ISO/
mkdir DYee/IndividualFits/Combined/
mkdir DYee/IndividualFits/Trigger8GeV/
mkdir DYee/IndividualFits/Trigger17GeV/
mkdir DYee/SummaryPlots/ID/
mkdir DYee/SummaryPlots/ISO/
mkdir DYee/SummaryPlots/Combined/
mkdir DYee/SummaryPlots/Trigger8GeV/
mkdir DYee/SummaryPlots/Trigger17GeV/
mkdir DYee/SummaryPlots/Tables/

# run sequentially on filters
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_4l-TP-MC-4l/ /scratch/stephane/TP_dielectron_data_4l_2012A-TP-4l/ZEETPData.root tagAndProbeelectron4l17GeVTrigger/tagAndProbeTree ID "MVAIDPass==1" "MVAIDPass==0" DYeePtEtaConfig.txt > DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_4l-TP-MC-4l/ /scratch/stephane/TP_dielectron_data_4l_2012A-TP-4l/ZEETPData.root tagAndProbeelectron4l17GeVTrigger/tagAndProbeTree ISO "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_4l-TP-MC-4l/ /scratch/stephane/TP_dielectron_data_4l_2012A-TP-4l/ZEETPData.root tagAndProbeelectron4l17GeVTrigger/tagAndProbeTree Trigger17GeV "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_4l-TP-MC-4l/ /scratch/stephane/TP_dielectron_data_4l_2012A-TP-4l/ZEETPData.root tagAndProbeelectron4l8GeVTrigger/tagAndProbeTree Trigger8GeV "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_4l-TP-MC-4l/ /scratch/stephane/TP_dielectron_data_4l_2012A-TP-4l/ZEETPData.root tagAndProbeelectron4l17GeVTrigger/tagAndProbeTree Combined "ISOPass==1" "MVAIDPass==0 || ISOPass==0" DYeePtEtaConfig.txt  >> DYee_output.txt



# create efficiency LaTeX tables
cd DYee/SummaryPlots/Tables
latex efficienciesDYee-ID.tex >/dev/null
latex efficienciesDYee-ISO.tex >/dev/null
latex efficienciesDYee-Trigger17GeV.tex >/dev/null
latex efficienciesDYee-Trigger8GeV.tex >/dev/null
latex efficienciesDYee-Combined.tex >/dev/null
dvips -o efficienciesDYee-ID.ps efficienciesDYee-ID.dvi >/dev/null
dvips -o efficienciesDYee-ISO.ps efficienciesDYee-ISO.dvi >/dev/null
dvips -o efficienciesDYee-Trigger17GeV.ps efficienciesDYee-Trigger17GeV.dvi >/dev/null
dvips -o efficienciesDYee-Trigger8GeV.ps efficienciesDYee-Trigger8GeV.dvi >/dev/null
dvips -o efficienciesDYee-Combined.ps efficienciesDYee-Combined.dvi >/dev/null
rm *.log
rm *.aux
rm *.dvi
cd ../../..
