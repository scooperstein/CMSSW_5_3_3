
rm -rf DYmumu/
mkdir DYmumu/
mkdir DYmumu/IndividualFits/
mkdir DYmumu/SummaryPlots/
mkdir DYmumu/IndividualFits/4l-ID/
mkdir DYmumu/IndividualFits/2l2tau-ID/
mkdir DYmumu/IndividualFits/ZH-ID/
mkdir DYmumu/IndividualFits/4l-SIP/
mkdir DYmumu/IndividualFits/4l-ISO/
mkdir DYmumu/IndividualFits/4l-ISO-dBetta/
mkdir DYmumu/IndividualFits/2l2tau-ISO-Tight/
mkdir DYmumu/IndividualFits/2l2tau-ISO-Loose/
mkdir DYmumu/IndividualFits/ZH-ISO-Tight/
mkdir DYmumu/IndividualFits/ZH-ISO-Loose/
mkdir DYmumu/IndividualFits/4l-T8/
mkdir DYmumu/IndividualFits/4l-T17/
mkdir DYmumu/IndividualFits/2l2tau-T8/
mkdir DYmumu/IndividualFits/2l2tau-T17/
mkdir DYmumu/IndividualFits/ZH-T8/
mkdir DYmumu/IndividualFits/ZH-T17/
mkdir DYmumu/IndividualFits/4l-Combined/
mkdir DYmumu/IndividualFits/4l-Combined-dBetta/
mkdir DYmumu/IndividualFits/2l2tau-Combined-Loose/
mkdir DYmumu/IndividualFits/2l2tau-Combined-Tight/
mkdir DYmumu/IndividualFits/ZH-Combined-Loose/
mkdir DYmumu/IndividualFits/ZH-Combined-Tight/
mkdir DYmumu/SummaryPlots/4l-ID/
mkdir DYmumu/SummaryPlots/2l2tau-ID/
mkdir DYmumu/SummaryPlots/ZH-ID/
mkdir DYmumu/SummaryPlots/4l-SIP/
mkdir DYmumu/SummaryPlots/4l-ISO/
mkdir DYmumu/SummaryPlots/4l-ISO-dBetta/
mkdir DYmumu/SummaryPlots/2l2tau-ISO-Tight/
mkdir DYmumu/SummaryPlots/2l2tau-ISO-Loose/
mkdir DYmumu/SummaryPlots/ZH-ISO-Tight/
mkdir DYmumu/SummaryPlots/ZH-ISO-Loose/
mkdir DYmumu/SummaryPlots/4l-T8/
mkdir DYmumu/SummaryPlots/4l-T17/
mkdir DYmumu/SummaryPlots/2l2tau-T8/
mkdir DYmumu/SummaryPlots/2l2tau-T17/
mkdir DYmumu/SummaryPlots/ZH-T8/
mkdir DYmumu/SummaryPlots/ZH-T17/
mkdir DYmumu/SummaryPlots/4l-Combined/
mkdir DYmumu/SummaryPlots/4l-Combined-dBetta/
mkdir DYmumu/SummaryPlots/2l2tau-Combined-Loose/
mkdir DYmumu/SummaryPlots/2l2tau-Combined-Tight/
mkdir DYmumu/SummaryPlots/ZH-Combined-Loose/
mkdir DYmumu/SummaryPlots/ZH-Combined-Tight/
mkdir DYmumu/SummaryPlots/Tables/

# 4l
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root tagAndProbeMu4lT17/tagAndProbeTree 4l-ID "IDPass==1" "IDPass==0" DYmumuPtEtaConfig.txt > DYmumu_output_4l.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root tagAndProbeMu4lT17/tagAndProbeTree 4l-SIP "SIPPass==1" "SIPPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_4l.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root tagAndProbeMu4lT17/tagAndProbeTree 4l-ISO "ISOPass==1" "ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_4l.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root tagAndProbeMu4lT8dBetta/tagAndProbeTree 4l-ISO-dBetta "ISOPass==1" "ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_4l.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root tagAndProbeMu4lT17/tagAndProbeTree 4l-T17 "hltPass" "hltPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_4l.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root tagAndProbeMu4lT8/tagAndProbeTree 4l-T8 "hltPass==1" "hltPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_4l.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root tagAndProbeMu4lT17/tagAndProbeTree 4l-Combined "IDPass==1&&SIPPass==1&&ISOPass==1" "IDPass==0||SIPPass==0||ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_4l.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root tagAndProbeMu4lT8dBetta/tagAndProbeTree 4l-Combined-dBetta "IDPass==1&&SIPPass==1&&ISOPass==1" "IDPass==0||SIPPass==0||ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_4l.txt


# 2l2tau
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMu2l2tauLooseT17/tagAndProbeTree 2l2tau-ID "IDPass==1" "IDPass==0" DYmumuPtEtaConfig.txt > DYmumu_output_2l2tau.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMu2l2tauLooseT17/tagAndProbeTree 2l2tau-ISO-Loose "ISOPass==1" "ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_2l2tau.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMu2l2tauTightT17/tagAndProbeTree 2l2tau-ISO-Tight "ISOPass==1" "ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_2l2tau.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMu2l2tauLooseT17/tagAndProbeTree 2l2tau-T17 "hltPass==1" "hltPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_2l2tau.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMu2l2tauLooseT8/tagAndProbeTree 2l2tau-T8 "hltPass==1" "hltPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_2l2tau.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMu2l2tauLooseT17/tagAndProbeTree 2l2tau-Combined-Loose "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_2l2tau.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMu2l2tauTightT17/tagAndProbeTree 2l2tau-Combined-Tight "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_2l2tau.txt

# ZH
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMuZHLooseT17/tagAndProbeTree ZH-ID "IDPass==1" "IDPass==0" DYmumuPtEtaConfig.txt > DYmumu_output_ZH.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/ /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMuZHLooseT17/tagAndProbeTree ZH-ISO-Loose "ISOPass==1" "ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_ZH.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMuZHTightT17/tagAndProbeTree ZH-ISO-Tight "ISOPass==1" "ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_ZH.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMuZHLooseT17/tagAndProbeTree ZH-T17 "hltPass==1" "hltPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_ZH.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMuZHLooseT8/tagAndProbeTree ZH-T8 "hltPass==1" "hltPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_ZH.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMuZHLooseT17/tagAndProbeTree ZH-Combined-Loose "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_ZH.txt
TagAndProbeMCEtaBins DYmumu /scratch/stephane/TP_dimuon_mc_all_53X-TP-MC-all/  /scratch/stephane/TP_dimuon_data_all_2012C_53X-TP-all/ZMuMuData.root /tagAndProbeMuZHTightT17/tagAndProbeTree ZH-Combined-Tight "IDPass==1&&ISOPass==1" "IDPass==0||ISOPass==0" DYmumuPtEtaConfig.txt >> DYmumu_output_ZH.txt


cd DYmumu/SummaryPlots/Tables
latex efficienciesDYmumu-4l-ID.tex
dvips -o efficienciesDYmumu-4l-ID.ps efficienciesDYmumu-4l-ID.dvi
latex efficienciesDYmumu-2l2tau-ID.tex
dvips -o efficienciesDYmumu-2l2tau-ID.ps efficienciesDYmumu-2l2tau-ID.dvi
latex efficienciesDYmumu-ZH-ID.tex
dvips -o efficienciesDYmumu-ZH-ID.ps efficienciesDYmumu-ZH-ID.dvi
latex efficienciesDYmumu-4l-SIP.tex
dvips -o efficienciesDYmumu-4l-SIP.ps efficienciesDYmumu-4l-SIP.dvi
latex efficienciesDYmumu-4l-ISO.tex
dvips -o efficienciesDYmumu-4l-ISO.ps efficienciesDYmumu-4l-ISO.dvi
latex efficienciesDYmumu-4l-ISO-dBetta.tex
dvips -o efficienciesDYmumu-4l-ISO-dBetta.ps efficienciesDYmumu-4l-ISO-dBetta.dvi
latex efficienciesDYmumu-2l2tau-ISO-Tight.tex
dvips -o efficienciesDYmumu-2l2tau-ISO-Tight.ps efficienciesDYmumu-2l2tau-ISO-Tight.dvi
latex efficienciesDYmumu-2l2tau-ISO-Loose.tex
dvips -o efficienciesDYmumu-2l2tau-ISO-Loose.ps efficienciesDYmumu-2l2tau-ISO-Loose.dvi
latex efficienciesDYmumu-ZH-ISO-Tight.tex
dvips -o efficienciesDYmumu-ZH-ISO-Tight.ps efficienciesDYmumu-ZH-ISO-Tight.dvi
latex efficienciesDYmumu-ZH-ISO-Loose.tex
dvips -o efficienciesDYmumu-ZH-ISO-Loose.ps efficienciesDYmumu-ZH-ISO-Loose.dvi
latex efficienciesDYmumu-4l-T8.tex
dvips -o efficienciesDYmumu-4l-T8.ps efficienciesDYmumu-4l-T8.dvi
latex efficienciesDYmumu-4l-T17.tex
dvips -o efficienciesDYmumu-4l-T17.ps efficienciesDYmumu-4l-T17.dvi
latex efficienciesDYmumu-2l2tau-T8.tex
dvips -o efficienciesDYmumu-2l2tau-T8.ps efficienciesDYmumu-2l2tau-T8.dvi
latex efficienciesDYmumu-2l2tau-T17.tex
dvips -o efficienciesDYmumu-2l2tau-T17.ps efficienciesDYmumu-2l2tau-T17.dvi
latex efficienciesDYmumu-ZH-T8.tex
dvips -o efficienciesDYmumu-ZH-T8.ps efficienciesDYmumu-ZH-T8.dvi
latex efficienciesDYmumu-ZH-T17.tex
dvips -o efficienciesDYmumu-ZH-T17.ps efficienciesDYmumu-ZH-T17.dvi
latex efficienciesDYmumu-4l-Combined.tex
dvips -o efficienciesDYmumu-4l-Combined.ps efficienciesDYmumu-4l-Combined.dvi
latex efficienciesDYmumu-4l-Combined-dBetta.tex
dvips -o efficienciesDYmumu-4l-Combined-dBetta.ps efficienciesDYmumu-4l-Combined-dBetta.dvi
latex efficienciesDYmumu-2l2tau-Combined-Loose.tex
dvips -o efficienciesDYmumu-2l2tau-Combined-Loose.ps efficienciesDYmumu-2l2tau-Combined-Loose.dvi
latex efficienciesDYmumu-2l2tau-Combined-Tight.tex
dvips -o efficienciesDYmumu-2l2tau-Combined-Tight.ps efficienciesDYmumu-2l2tau-Combined-Tight.dvi
latex efficienciesDYmumu-ZH-Combined-Loose.tex
dvips -o efficienciesDYmumu-ZH-Combined-Loose.ps efficienciesDYmumu-ZH-Combined-Loose.dvi
latex efficienciesDYmumu-ZH-Combined-Tight.tex
dvips -o efficienciesDYmumu-ZH-Combined-Tight.ps efficienciesDYmumu-ZH-Combined-Tight.dvi


rm *.dvi
rm *.aux
rm *.log
cd ../../..
cp DYmumu_output* DYmumu/
