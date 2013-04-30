#!/bin/sh

mkdir sandbox
cd sandbox

mergeFiles --copy-timeout=90 ETEM_2012A.root /hdfs/store/user/swanson/ETEM_2012A-SUB-ET-EM
mergeFiles --copy-timeout=90 ETEM_2012B_1.root /hdfs/store/user/swanson/ETEM_2012B_1-SUB-ET-EM
mergeFiles --copy-timeout=90 MTEM_2012A.root /hdfs/store/user/swanson/MTEM_2012A-SUB-MT-EM
mergeFiles --copy-timeout=90 MTEM_2012B_1.root /hdfs/store/user/swanson/MTEM_2012B_1-SUB-MT-EM

hadd ETEM.root ETEM_2012A.root ETEM_2012B_1.root
hadd MTEM.root MTEM_2012A.root MTEM_2012B_1.root




 









