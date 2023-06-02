#!/bin/bash

# API接口地址
create_url="https://api.boce.com/v3/task/create/curl"
result_url=" https://api.boce.com/v3/task/curl"

# 授权的标识信息
key="97fa88c09ec4fe9ebdc614ecfa361461"

# 节点ID列表
node_ids="31,32"

# 待检测的链接
#domain list : add , remove domain here
#filename="/Users/steven/Desktop/ceshicunchu/api/domain_list.txt"
#while IFS= read -r domain
#do
host="kwzbo2.com"
# 域名白名单
except_domain="a.com"

# 创建任务
create_response=$(curl -s -X GET "$create_url?key=$key&node_ids=$node_ids&host=$domain&except_domain=$except_domain")

# 解析创建任务的JSON响应
create_error_code=$(echo "$create_response" | jq -r '.error_code')
create_data_id=$(echo "$create_response" | jq -r '.data.id')
create_error=$(echo "$create_response" | jq -r '.error')
done < "$filename"
# 打印创建任务的结果
echo "创建任务结果："
echo "error_code: $create_error_code"
echo "data.id: $create_data_id"
echo "error: $create_error"
echo

# 获取任务结果
while true
do
    # 获取结果
    result_response=$(curl -s -X GET "$result_url/$create_data_id?key=$key")

    # 解析结果的JSON响应
    done_status=$(echo "$result_response" | jq -r '.done')
    hijack_num=$(echo "$result_response" | jq -r '.hijack_num')
    max_node=$(echo "$result_response" | jq -r '.max_node')

    # 打印结果
    echo "任务结果："
    echo "done: $done_status"
    echo "被劫持的节点数: $hijack_num"
    echo "max_node: $max_node"
    echo

    # 判断任务是否完成
    if [ "$done_status" = "true" ]; then
        break
    fi

    # 每5秒请求一次任务结果
    #sleep 5
done