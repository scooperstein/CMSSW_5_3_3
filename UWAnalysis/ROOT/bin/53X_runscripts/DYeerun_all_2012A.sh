rm -rf DYee/
mkdir DYee/
mkdir DYee/IndividualFits/
mkdir DYee/SummaryPlots/
mkdir DYee/IndividualFits/4l-ID/
mkdir DYee/IndividualFits/2l2tau-ID/
mkdir DYee/IndividualFits/ZH-ID/
mkdir DYee/IndividualFits/4l-SIP/
mkdir DYee/IndividualFits/4l-ISO/
mkdir DYee/IndividualFits/4l-ISO-dBetta/
mkdir DYee/IndividualFits/2l2tau-ISO-Tight/
mkdir DYee/IndividualFits/2l2tau-ISO-Loose/
mkdir DYee/IndividualFits/ZH-ISO-Tight/
mkdir DYee/IndividualFits/ZH-ISO-Loose/
mkdir DYee/IndividualFits/4l-T8/
mkdir DYee/IndividualFits/4l-T17/
mkdir DYee/IndividualFits/2l2tau-T8/
mkdir DYee/IndividualFits/2l2tau-T17/
mkdir DYee/IndividualFits/ZH-T8/
mkdir DYee/IndividualFits/ZH-T17/
mkdir DYee/IndividualFits/4l-Combined/
mkdir DYee/IndividualFits/4l-Combined-dBetta/
mkdir DYee/IndividualFits/2l2tau-Combined-Loose/
mkdir DYee/IndividualFits/2l2tau-Combined-Tight/
mkdir DYee/IndividualFits/ZH-Combined-Loose/
mkdir DYee/IndividualFits/ZH-Combined-Tight/
mkdir DYee/SummaryPlots/4l-ID/
mkdir DYee/SummaryPlots/2l2tau-ID/
mkdir DYee/SummaryPlots/ZH-ID/
mkdir DYee/SummaryPlots/4l-SIP/
mkdir DYee/SummaryPlots/4l-ISO/
mkdir DYee/SummaryPlots/4l-ISO-dBetta/
mkdir DYee/SummaryPlots/2l2tau-ISO-Tight/
mkdir DYee/SummaryPlots/2l2tau-ISO-Loose/
mkdir DYee/SummaryPlots/ZH-ISO-Tight/
mkdir DYee/SummaryPlots/ZH-ISO-Loose/
mkdir DYee/SummaryPlots/4l-T8/
mkdir DYee/SummaryPlots/4l-T17/
mkdir DYee/SummaryPlots/2l2tau-T8/
mkdir DYee/SummaryPlots/2l2tau-T17/
mkdir DYee/SummaryPlots/ZH-T8/
mkdir DYee/SummaryPlots/ZH-T17/
mkdir DYee/SummaryPlots/4l-Combined/
mkdir DYee/SummaryPlots/4l-Combined-dBetta/
mkdir DYee/SummaryPlots/2l2tau-Combined-Loose/
mkdir DYee/SummaryPlots/2l2tau-Combined-Tight/
mkdir DYee/SummaryPlots/ZH-Combined-Loose/
mkdir DYee/SummaryPlots/ZH-Combined-Tight/
mkdir DYee/SummaryPlots/Tables/

# 4l
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root tagAndProbeEl4lT17/tagAndProbeTree 4l-ID "IDPass==1" "IDPass==0" DYeePtEtaConfig.txt > DYee_output_4l.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root tagAndProbeEl4lT17/tagAndProbeTree 4l-SIP "SIPPass==1" "SIPPass==0" DYeePtEtaConfig.txt >> DYee_output_4l.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root tagAndProbeEl4lT17/tagAndProbeTree 4l-ISO "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_4l.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root tagAndProbeEl4lT8dBetta/tagAndProbeTree 4l-ISO-dBetta "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_4l.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root tagAndProbeEl4lT17/tagAndProbeTree 4l-T17 "hltPass" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output_4l.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root tagAndProbeEl4lT8/tagAndProbeTree 4l-T8 "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output_4l.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root tagAndProbeEl4lT17/tagAndProbeTree 4l-Combined "IDPass==1&&SIPPass==1&&ISOPass==1" "IDPass==0||SIPPass==0||ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_4l.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/ /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root tagAndProbeEl4lT8dBetta/tagAndProbeTree 4l-Combined-dBetta "IDPass==1&&SIPPass==1&&ISOPass==1" "IDPass==0||SIPPass==0||ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_4l.txt


# 2l2tau
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeEl2l2tauLooseT17/tagAndProbeTree 2l2tau-ID "IDPass==1" "IDPass==0" DYeePtEtaConfig.txt > DYee_output_2l2tau.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeEl2l2tauLooseT17/tagAndProbeTree 2l2tau-ISO-Loose "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_2l2tau.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeEl2l2tauTightT17/tagAndProbeTree 2l2tau-ISO-Tight "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_2l2tau.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeEl2l2tauLooseT17/tagAndProbeTree 2l2tau-T17 "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output_2l2tau.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeEl2l2tauLooseT8/tagAndProbeTree 2l2tau-T8 "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output_2l2tau.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/ /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeEl2l2tauLooseT17/tagAndProbeTree 2l2tau-Combined-Loose "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_2l2tau.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeEl2l2tauTightT17/tagAndProbeTree 2l2tau-Combined-Tight "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_2l2tau.txt

# ZH
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeElZHLooseT17/tagAndProbeTree ZH-ID "IDPass==1" "IDPass==0" DYeePtEtaConfig.txt > DYee_output_ZH.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/ /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeElZHLooseT17/tagAndProbeTree ZH-ISO-Loose "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_ZH.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeElZHTightT17/tagAndProbeTree ZH-ISO-Tight "ISOPass==1" "ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_ZH.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeElZHLooseT17/tagAndProbeTree ZH-T17 "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output_ZH.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeElZHLooseT8/tagAndProbeTree ZH-T8 "hltPass==1" "hltPass==0" DYeePtEtaConfig.txt >> DYee_output_ZH.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/  /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeElZHLooseT17/tagAndProbeTree ZH-Combined-Loose "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_ZH.txt
TagAndProbeMCEtaBins DYee /scratch/stephane/TP_dielectron_mc_all_53X-TP-MC-all-ee/ /scratch/stephane/TP_dielectron_data_all_2012A_53X_fixed-TP-all-ee/ZEETPData.root /tagAndProbeElZHTightT17/tagAndProbeTree ZH-Combined-Tight "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" DYeePtEtaConfig.txt >> DYee_output_ZH.txt


cd DYee/SummaryPlots/Tables
latex efficienciesDYee-4l-ID.tex
dvips -o efficienciesDYee-4l-ID.ps efficienciesDYee-4l-ID.dvi
latex efficienciesDYee-2l2tau-ID.tex
dvips -o efficienciesDYee-2l2tau-ID.ps efficienciesDYee-2l2tau-ID.dvi
latex efficienciesDYee-ZH-ID.tex
dvips -o efficienciesDYee-ZH-ID.ps efficienciesDYee-ZH-ID.dvi
latex efficienciesDYee-4l-SIP.tex
dvips -o efficienciesDYee-4l-SIP.ps efficienciesDYee-4l-SIP.dvi
latex efficienciesDYee-4l-ISO.tex
dvips -o efficienciesDYee-4l-ISO.ps efficienciesDYee-4l-ISO.dvi
latex efficienciesDYee-4l-ISO-dBetta.tex
dvips -o efficienciesDYee-4l-ISO-dBetta.ps efficienciesDYee-4l-ISO-dBetta.dvi
latex efficienciesDYee-2l2tau-ISO-Tight.tex
dvips -o efficienciesDYee-2l2tau-ISO-Tight.ps efficienciesDYee-2l2tau-ISO-Tight.dvi
latex efficienciesDYee-2l2tau-ISO-Loose.tex
dvips -o efficienciesDYee-2l2tau-ISO-Loose.ps efficienciesDYee-2l2tau-ISO-Loose.dvi
latex efficienciesDYee-ZH-ISO-Tight.tex
dvips -o efficienciesDYee-ZH-ISO-Tight.ps efficienciesDYee-ZH-ISO-Tight.dvi
latex efficienciesDYee-ZH-ISO-Loose.tex
dvips -o efficienciesDYeeZH-ISO-Loose.ps efficienciesDYee-ZH-ISO-Loose.dvi
latex efficienciesDYee-4l-T8.tex
dvips -o efficienciesDYee4l-T8.ps efficienciesDYee-4l-T8.dvi
latex efficienciesDYee-4l-T17.tex
dvips -o efficienciesDYee-4l-T17.ps efficienciesDYee-4l-T17.dvi
latex efficienciesDYee-2l2tau-T8.tex
dvips -o efficienciesDYee-2l2tau-T8.ps efficienciesDYee-2l2tau-T8.dvi
latex efficienciesDYee-2l2tau-T17.tex
dvips -o efficienciesDYee2l2tau-T17.ps efficienciesDYee-2l2tau-T17.dvi
latex efficienciesDYee-ZH-T8.tex
dvips -o efficienciesDYee-ZH-T8.ps efficienciesDYee-ZH-T8.dvi
latex efficienciesDYee-ZH-T17.tex
dvips -o efficienciesDYee-ZH-T17.ps efficienciesDYee-ZH-T17.dvi
latex efficienciesDYee-4l-Combined.tex
dvips -o efficienciesDYee-4l-Combined.ps efficienciesDYee-4l-Combined.dvi
latex efficienciesDYee-4l-Combined-dBetta.tex
dvips -o efficienciesDYee-4l-Combined-dBetta.ps efficienciesDYee4l-Combined-dBetta.dvi
latex efficienciesDYee-2l2tau-Combined-Loose.tex
dvips -o efficienciesDYee-2l2tau-Combined-Loose.ps efficienciesDYee-2l2tau-Combined-Loose.dvi
latex efficienciesDYee-2l2tau-Combined-Tight.tex
dvips -o efficienciesDYee-2l2tau-Combined-Tight.ps efficienciesDYee-2l2tau-Combined-Tight.dvi
latex efficienciesDYee-ZH-Combined-Loose.tex
dvips -o efficienciesDYee-ZH-Combined-Loose.ps efficienciesDYee-ZH-Combined-Loose.dvi
latex efficienciesDYee-ZH-Combined-Tight.tex
dvips -o efficienciesDYee-ZH-Combined-Tight.ps efficienciesDYee-ZH-Combined-Tight.dvi


rm *.dvi
rm *.aux
rm *.log
cd ../../..
cp DYee_output* DYee/
