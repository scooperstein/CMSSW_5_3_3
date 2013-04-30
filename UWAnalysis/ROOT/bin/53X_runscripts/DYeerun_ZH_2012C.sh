# remove previous output
rm DYee_output.txt
rm -r DYee
mkdir DYee/
mkdir DYee/IndividualFits/
mkdir DYee/SummaryPlots/
mkdir DYee/IndividualFits/ID/
mkdir DYee/IndividualFits/ISO-Loose/
mkdir DYee/IndividualFits/ISO-Tight/
mkdir DYee/IndividualFits/Combined-Loose/
mkdir DYee/IndividualFits/Combined-Tight/
mkdir DYee/IndividualFits/Trigger8GeV/
mkdir DYee/IndividualFits/Trigger17GeV/
mkdir DYee/SummaryPlots/ID/
mkdir DYee/SummaryPlots/ISO-Loose/
mkdir DYee/SummaryPlots/ISO-Tight/
mkdir DYee/SummaryPlots/Combined-Loose/
mkdir DYee/SummaryPlots/Combined-Tight/
mkdir DYee/SummaryPlots/Trigger8GeV/
mkdir DYee/SummaryPlots/Trigger17GeV/
mkdir DYee/SummaryPlots/Tables/

# run sequentially on filters
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_ZH-TP-MC-ZH/ /scratch/stephane/TP_dielectron_data_ZH_2012A-TP-ZH/ZEETPData.root tagAndProbeelectronZH17GeVTriggerLoose/tagAndProbeTree ID "MVAIDPass==1" "MVAIDPass==0" DYeePtEtaConfig.txt > DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_ZH-TP-MC-ZH/ /scratch/stephane/TP_dielectron_data_ZH_2012A-TP-ZH/ZEETPData.root tagAndProbeelectronZH17GeVTriggerLoose/tagAndProbeTree ISO-Loose "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_ZH-TP-MC-ZH/ /scratch/stephane/TP_dielectron_data_ZH_2012A-TP-ZH/ZEETPData.root tagAndProbeelectronZHtau17GeVTriggerTight/tagAndProbeTree ISO-Tight "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_ZH-TP-MC-ZH/ /scratch/stephane/TP_dielectron_data_ZH_2012A-TP-ZH/ZEETPData.root tagAndProbeelectronZH17GeVTriggerLoose/tagAndProbeTree Trigger17GeV "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_ZH-TP-MC-ZH/ /scratch/stephane/TP_dielectron_data_ZH_2012A-TP-ZH/ZEETPData.root tagAndProbeelectronZH8GeVTriggerLoose/tagAndProbeTree Trigger8GeV "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_ZH-TP-MC-ZH/ /scratch/stephane/TP_dielectron_data_ZH_2012A-TP-ZH/ZEETPData.root tagAndProbeelectronZH17GeVTriggerLoose/tagAndProbeTree Combined-Loose "ISOPass==1" "MVAIDPass==0 || ISOPass==0" DYeePtEtaConfig.txt  >> DYee_output.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_ZH-TP-MC-ZH/ /scratch/stephane/TP_dielectron_data_ZH_2012A-TP-ZH/ZEETPData.root tagAndProbeelectronZHtau17GeVTriggerTight/tagAndProbeTree Combined-Tight "ISOPass==1" "MVAIDPass==0 || ISOPass==0" DYeePtEtaConfig.txt  >> DYee_output.txt


# create efficiency LaTeX tables
cd DYee/SummaryPlots/Tables
latex efficienciesDYee-ID.tex >/dev/null
latex efficienciesDYee-ISO-Loose.tex >/dev/null
latex efficienciesDYee-ISO-Tight.tex >/dev/null
latex efficienciesDYee-Trigger17GeV.tex >/dev/null
latex efficienciesDYee-Trigger8GeV.tex >/dev/null
latex efficienciesDYee-Combined-Loose.tex >/dev/null
latex efficienciesDYee-Combined-Tight.tex >/dev/null
dvips -o efficienciesDYee-ID.ps efficienciesDYee-ID.dvi >/dev/null
dvips -o efficienciesDYee-ISO-Loose.ps efficienciesDYee-ISO-Loose.dvi >/dev/null
dvips -o efficienciesDYee-ISO-Tight.ps efficienciesDYee-ISO-Tight.dvi >/dev/null
dvips -o efficienciesDYee-Trigger17GeV.ps efficienciesDYee-Trigger17GeV.dvi >/dev/null
dvips -o efficienciesDYee-Trigger8GeV.ps efficienciesDYee-Trigger8GeV.dvi >/dev/null
dvips -o efficienciesDYee-Combined-Loose.ps efficienciesDYee-Combined-Loose.dvi >/dev/null
dvips -o efficienciesDYee-Combined-Tight.ps efficienciesDYee-Combined-Tight.dvi >/dev/null
rm *.log
rm *.aux
rm *.dvi
cd ../../..
cp DYee_output.txt DYee/
