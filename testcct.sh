#! /bin/bash

cd /Users/steven/Desktop/BIG-svn/JKsource/workspace/testcct


dbtime=$(date "+%Y%m%d")
echo $dbtime
mkdir $dbtime


cd /Users/steven/Desktop/BIG-svn/JKsource/workspace/testcct/$dbtime
wget https://93tv-gj.oss-accelerate.aliyuncs.com/app/93tv.mobileconfig  #93tv
wget https://f7tv-gj-1314123205.cos.accelerate.myqcloud.com/app/F7.mobileconfig  #f7tv
wget https://h8tv-gj.oss-accelerate.aliyuncs.com/app/h8zb.mobileconfig          #h8tv
wget https://tvlives.oss-accelerate.aliyuncs.com/app/lqtv.mobileconfig #lqtv
wget https://btv-gj-1314123205.cos.accelerate.myqcloud.com/app/btv.mobileconfig   #btv
wget https://wqtv-gj.oss-accelerate.aliyuncs.com/app/wqtv.mobileconfig    #wqtv
wget https://tqtv-gj.oss-accelerate.aliyuncs.com/app/tqtv.mobileconfig   #tqtv
wget https://kwtv-gj.oss-accelerate.aliyuncs.com/app/kwtv.mobileconfig    #kwtv
wget https://resaiba.oss-accelerate.aliyuncs.com/app/rs.mobileconfig    #resai8



files=(
	
	"93tv.mobileconfig"
	"F7.mobileconfig"
	"h8zb.mobileconfig"
	"lqtv.mobileconfig"
	"btv.mobileconfig"
	"wqtv.mobileconfig"
	"tqtv.mobileconfig"
	"kwtv.mobileconfig"
	"rs.mobileconfig"

)
 log_file="/Users/steven/Desktop/ceshicunchu/cctlog.txt"

for file_name in "${files[@]}";do
if [ -f "$file_name" ]; then

echo " from $dbtime File '$file_name' exists" 
else
	echo " from $dbtime File '$file_name' not ok =>>>>>>>>> check-cloud object storage(存储桶)" >> "$log_file"
	fi
done

cd /Users/steven/Desktop/BIG-svn/JKsource/workspace/testcct/
rm -rf $dbtime
