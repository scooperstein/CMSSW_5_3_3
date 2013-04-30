#!/bin/sh

mkdir sandbox
cd sandbox

mergeFiles --copy-timeout=90 Data2012A.root /hdfs/store/user/swanson/2012A-SUB
mergeFiles --copy-timeout=90 Data2012B_1.root /hdfs/store/user/swanson/2012B_1-SUB
mergeFiles --copy-timeout=90 Data2012B_2.root /hdfs/store/user/swanson/2012B_2-SUB
mergeFiles --copy-timeout=90 Data2012B_3.root /hdfs/store/user/swanson/2012B_3-SUB
mergeFiles --copy-timeout=90 Data2012B_4.root /hdfs/store/user/swanson/2012B_4-SUB
mergeFiles --copy-timeout=90 Data2012B_5.root /hdfs/store/user/swanson/data_2012B_5-SUB

hadd DATA.root Data2012A.root Data2012B_1.root Data2012B_2.root Data2012B_3.root Data2012B_4.root Data2012B_5.root


 









