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
TagAndProbeMCEtaBins DYee /hdfs/store/user/stephane/TagAndProbe_dielectron_mc/ /hdfs/store/user/stephane/TagAndProbe_dielectron_data_v2-TP/ZEETPData.root tagAndProbeelectron2l2t17L/tagAndProbeTree ID "MVAIDPass==1" "MVAIDPass==0" DYeePtEtaConfig.txt > DYee_output.txt
#TagAndProbeMCEtaBins DYee /hdfs/store/user/stephane/TagAndProbe_dielectron_mc/ /hdfs/store/user/stephane/TagAndProbe_dielectron_data_v2-TP/ZEETPData.root tagAndProbeelectron2l2t17L/tagAndProbeTree ISO "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
#TagAndProbeMCEtaBins DYee /hdfs/store/user/stephane/TagAndProbe_dielectron_mc/ /hdfs/store/user/stephane/TagAndProbe_dielectron_data_v2-TP/ZEETPData.root tagAndProbeelectron2l2t17L/tagAndProbeTree Trigger17GeV "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
#TagAndProbeMCEtaBins DYee /hdfs/store/user/stephane/TagAndProbe_dielectron_mc/ /hdfs/store/user/stephane/TagAndProbe_dielectron_data_v2-TP/ZEETPData.root ttagAndProbeelectron2l2t8L/tagAndProbeTree Trigger8GeV "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
#TagAndProbeMCEtaBins DYee /hdfs/store/user/stephane/TagAndProbe_dielectron_mc/ /hdfs/store/user/stephane/TagAndProbe_dielectron_data_v2-TP/ZEETPData.root tagAndProbeelectron2l2t17L/tagAndProbeTree Combined "ISOPass==1" "MVAIDPass==0 || ISOPass==0" DYeePtEtaConfig.txt  >> DYee_output.txt



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
