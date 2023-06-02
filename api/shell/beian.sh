#!/bin/bash

# API接口地址
api_url="https://api.1314.cool/icp/api.php"

# 待查询的域名
domain="njhycx.com"

# 发送请求并获取结果
response=$(curl -s -X GET "$api_url?dm=$domain")

# 解析JSON响应
code=$(echo "$response" | jq -r '.code')
host=$(echo "$response" | jq -r '.主办单位名称')
nature=$(echo "$response" | jq -r '.主办单位性质')
license=$(echo "$response" | jq -r '.网站备案/许可证号')
name=$(echo "$response" | jq -r '.网站名称')
url=$(echo "$response" | jq -r '.网站首页网址')
review_time=$(echo "$response" | jq -r '.审核时间')

# 打印结果
echo "域名：$domain"
echo "查询结果："

if [ "$code" = "200" ]; then
  echo "主办单位名称: $host"
  echo "主办单位性质: $nature"
  echo "网站备案/许可证号: $license"
  echo "网站名称: $name"
  echo "网站首页网址: $url"
  echo "审核时间: $review_time"
else
  echo "查询失败，错误码：$code"
fi