#!/bin/bash
log_file="/Users/steven/Desktop/ceshicunchu/api/log/log_domain.txt"
normal_file="/Users/steven/Desktop/ceshicunchu/api/log/1.txt"
block_file="/Users/steven/Desktop/ceshicunchu/api/log/2.txt"
test_fail="/Users/steven/Desktop/ceshicunchu/api/log/3.txt"
non_file="/Users/steven/Desktop/ceshicunchu/api/log/4.txt"

# API接口地址
url="https://api.boce.com/v3/task/create/wechat"

# 授权的标识信息
key="97fa88c09ec4fe9ebdc614ecfa361461" #申请的key

#domain list : add , remove domain here
filename="/Users/steven/Desktop/ceshicunchu/api/domain_list.txt"

# Đọc domain từ tệp tin
while IFS= read -r domain
do
    response=$(curl -s "$url?key=$key&host=$domain")

    # Get "data" from JSON response
    data=$(echo "$response" | jq '.data')

    # Trích xuất domain và giá trị từ dữ liệu
    domain_value=$(echo "$data" | jq -r 'keys[]')
    value=$(echo "$data" | jq -r '.[]')

    # In ra kết quả
    #echo "Domain: $domain_value , Value: $value"

    echo "Domain: $domain_value , Value: $value" >> "$log_file"

done < "$filename"

    grep "Value: 1" $log_file | awk '{print $2}' > $normal_file
    awk 'BEGIN{print "----域名正常 :"} {print}' $normal_file
    echo -n > $normal_file

    grep "Value: 2" $log_file | awk '{print $2}' > $block_file
    awk 'BEGIN{print "----域名拦截(域名被封) :"} {print}' $block_file
    echo -n > $block_file

    grep "Value: 3" $log_file | awk '{print $2}' > $test_fail
    awk 'BEGIN{print "----检测失败 :"} {print}' $test_fail
    echo -n > $test_fail

    grep "Value: 4" $log_file | awk '{print $2}' > $non_file
    awk 'BEGIN{print "----拦截(非微信官方链接，需跳转访问):"} {print}' $non_file
    echo -n > $non_file

    echo -n > $log_file
    echo "total test domain : $(cat domain_list.txt | wc -l)"