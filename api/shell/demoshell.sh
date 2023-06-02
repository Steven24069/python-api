#!/bin/bash

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
    
    # 打印返回结果
    echo "域名: $domain"
    echo "error_code: $error_code"
    echo "error: $error"
    echo "data: $data"
    #echo
done < "$filename"








:<<'END'
# 发送GET请求
response=$(curl -s "$url?key=$key&host=$host")

# 解析JSON响应
error_code=$(echo "$response" | jq -r '.error_code')
error=$(echo "$response" | jq -r '.error')
data=$(echo "$response" | jq '.data')

# 打印返回结果
echo "error_code: $error_code"
echo "error: $error"
echo "data: $data"
END