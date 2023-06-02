#!/bin/bash
log_file="/Users/steven/Desktop/ceshicunchu/api/log_domain.txt"
# API接口地址
url="https://api.boce.com/v3/task/create/wechat"

# 授权的标识信息
key="97fa88c09ec4fe9ebdc614ecfa361461" #申请的key

# 需要测试的域名，多个用逗号隔开
#host="www.wqzb.win,www.wqzbs.life" . -------------

filename="/Users/steven/Desktop/ceshicunchu/api/domain_list.txt"



#read domain of file
while IFS= read -r domain
do
response=$(curl -s "$url?key=$key&host=$domain")

# 解析JSON响应
    error_code=$(echo "$response" | jq -r '.error_code')
    error=$(echo "$response" | jq -r '.error')
    data=$(echo "$response" | jq '.data')
    

#Case
 #  if [[ "$data" -eq 1 ]]; then
  #      echo "域名正常 : $domain "
   # fi

#domain_ok=$($data | cut -d ' ' -f2)
#echo "$domain_ok"
    # 打印返回结果
    
    echo "error_code: $error_code"
    echo "error: $error"
    echo "data: $data" 
     echo "data: $data" >> $log_file
   
   
done < "$filename"