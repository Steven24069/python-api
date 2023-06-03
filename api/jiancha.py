import requests
import time

# API endpoints
create_url = "https://api.boce.com/v3/task/create/curl"
result_url = "https://task.boce.com/v3/task/hijack"

# Authorization key
api_key = "19808f48ca8c5cf827f6cff8f87625ef"

# Node ID list
node_ids = "31,32"

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
    create_task_url = f"https://api.boce.com/v3/task/create/curl?key={api_key}&node_ids=31,32&host={domain}"
    create_response = requests.get(create_task_url)
    task_data = create_response.json()
    

    # Parse create task response
    create_error_code = task_data.get("error_code")
    create_data_id = task_data.get("data", {}).get("id")
    create_error = task_data.get("error")

    #Print create task result
    #print("Create Task Result:"
    print(task_data)
    print("error_code:", create_error_code)
    print("data.id:", create_data_id)
    print("error:", create_error)
    print()

    # Get Result
    #done_status = False
    while True:

        result_url = f"https://api.boce.com/v3/task/curl/{create_data_id}?key={api_key}"
        result_response = requests.get(result_url)
        result_data = result_response.json()


        done_status = result_data.get("done")

        #host = result_data.get("list", [{}])[0].get("hijack")
    #error_code = result_data.get(["list"][0]["hijack"])

        print(result_data)
        print("是否检查成功 :", done_status)

        #print("是否被劫持 :", host) #	是否被劫持,true被劫持,false未被劫持


        # Check if task is done
        if done_status:
            break

        # Wait for 5 seconds before requesting task result again
        time.sleep(5)


