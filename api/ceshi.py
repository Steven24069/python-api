import requests
import time

# API endpoints
create_url = "https://api.boce.com/v3/task/create/curl"
result_url = "https://task.boce.com/v3/task/hijack"

# Authorization key
api_key = "28c9e877c22d749ddda14398e7b95e6f"

# Node ID list
#node_ids = "jiedian.txt"
node_ids = "6,7,12"
#node_ids = "6,7,8,12,13,14,19,20,24,25,26,30,31,32,36,37,38,42,43,48,49,54,55,60,61,62,66,67,72,73,74,79,80,84,85,86,90,91,92,96,97,98,102,103,104,108,110,114,115,116,120,121,122,126,127,128,132,133,134,138,139,144,145,146,150,151,152,156,157,162,163,164,168,169,174,180,181,80044,80046,80053,80062,80066,80070,80090,80097,80164,80168,80169,80174,80176,80912,80913,80914,80915"
#create_task_url = f"https://task.boce.com/v3/node/list?key={api_key}"
#create_response = requests.get(create_task_url)
#task_data = create_response.json()

#print(task_data)
#create_data_id = task_data.get("data", {}).get("id")

#print(create_data_id)
#for item in task_data.get('data', {}).get('list', []):
    #id_value = item.get('id')

    #print(id_value)

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
    create_task_url = f"https://api.boce.com/v3/task/create/hijack?key={api_key}&node_ids={node_ids}&host={domain}&except_domain=a.com"
    create_response = requests.get(create_task_url)
    task_data = create_response.json()
    

    # Parse create task response
    create_error_code = task_data.get("error_code")
    create_data_id = task_data.get("data", {}).get("id")
    create_error = task_data.get("error")

    #Print create task result
    #print("Create Task Result:"
    #print(task_data)  #------------------test the create_task_url its okay yet?
    #print("error_code:", create_error_code)
    print("data.id:", create_data_id)
    #print("error:", create_error)
    #print()

    # Get Result
    #done_status = False
    while True:

        result_url = f"https://task.boce.com/v3/task/hijack/{create_data_id}?key={api_key}"
        result_response = requests.get(result_url)
        result_data = result_response.json()


        done_status = result_data.get("done")

        #host = result_data.get("list", [{}])[0].get("hijack")
    #error_code = result_data.get(["list"][0]["hijack"])

        #print(result_data) -------------result_url test its okay
        print("是否检查成功 :", done_status)
        false_count = 0
        for item in result_data.get('list', []):
            hijack = item.get('hijack')
            node_name = item.get('node_name')

            if hijack == True:

                #print("	是否被劫持,true被劫持,false未被劫持 :", hijack)
                print("	被劫持的地区名称 :", node_name)
            #else: false_count += 1
            #if false_count > 4:
            #        break
            #elif hijack == False:
            #    print("域名正常") 
        #print("是否被劫持 :", host) #	是否被劫持,true被劫持,false未被劫持


        # Check if task is done
        if done_status:
            break

        # Wait for 5 seconds before requesting task result again
        time.sleep(20)

