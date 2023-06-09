#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time

# API endpoints
#create_url = "https://api.boce.com/v3/task/create/curl"
#result_url = "https://task.boce.com/v3/task/hijack"

# Authorization key
api_key = "0638e2614857864c4b41c26899136c02"

# Node ID list
node_ids = "31,32,13,14,19,20,2"

# Domain list file
filename = "domain_list.txt"

# Read domain list from file
with open(filename, "r") as file:
    domains = file.readlines()

for domain in domains:
    domain = domain.strip()
    print("-------------------------------")
    print("-------------------------------")
    print("Domain:", domain)  # Print the domain

    # Create task
    results = []
#for domain in domains:
    create_task_url = f"https://api.boce.com/v3/task/create/curl?key={api_key}&node_ids={node_ids}&host={domain}"
    create_response = requests.get(create_task_url)
    task_data = create_response.json()
    

    # Parse create task response
    create_error_code = task_data.get("error_code")
    create_data_id = task_data.get("data", {}).get("id")
    create_error = task_data.get("error")

    #Print create task result
    #print("Create Task Result:"
    #print(task_data)
    #print("error_code:", create_error_code)
    print("data.id:", create_data_id)
    #print("error:", create_error)
    #print()

    # Get Result
    #done_status = False
    false_count = 0 
    while True:

        result_url = f"https://api.boce.com/v3/task/curl/{create_data_id}?key={api_key}"
        result_response = requests.get(result_url)
        result_data = result_response.json()


        done_status = result_data.get("done")

        #host = result_data.get("list", [{}])[0].get("hijack")
    #error_code = result_data.get(["list"][0]["hijack"])

        #print(result_data)
        print("是否检查成功 :", done_status)

        

        #print("是否被劫持 :", host) #	是否被劫持,true被劫持,false未被劫持
        if done_status == True :
            for item in result_data.get('list', []):
                node_name = item.get('node_name')
                error_code = item.get('error_code')
                ip_region = item.get('ip_region')


                if ip_region == "本机地址本机地址" :
                    
                    print("节点有问题 ：", node_name)
                    #print(ip_region)
                #print(error_code)

            #if hijack == True: #------------------

                #print("	是否被劫持,true被劫持,false未被劫持 :", hijack)
            #    print("	被劫持的地区名称 :", node_name)
            #else: false_count += 1
            #if not done_status :
            #    false_count +=1
            #    if false_count >4 :    
            #        break
            #elif hijack == False:
            #    print("域名正常") 
        #print("是否被劫持 :", host) #	是否被劫持,true被劫持,false未被劫持


        # Check if task is done
        if done_status:
            break


        false_count += 1            
        if false_count > 2:
            break

        # Wait for 5 seconds before requesting task result again
        time.sleep(20)
        # Check if task is done



