import requests
import time

# API endpoints
create_url = "https://api.boce.com/v3/task/create/hijack"
result_url = "https://task.boce.com/v3/task/hijack"

# Authorization key
key = "97fa88c09ec4fe9ebdc614ecfa361461"

# Node ID list
node_ids = "31,32"

# Domain list
filename = "/Users/steven/Desktop/ceshicunchu/api/domain_list.txt"

# Domain whitelist
except_domain = "a.com"

# Read domain list from file
with open(filename, "r") as file:
    domains = file.readlines()

for domain in domains:
    domain = domain.strip()
    print("Domain:", domain)  # Print the domain

    # Create task
    create_params = {
        "key": key,
        "node_ids": node_ids,
        "host": domain,
        "except_domain": except_domain
    }

    create_response = requests.get(create_url, params=create_params).json()

    # Parse create task response
    create_error_code = create_response.get("error_code")
    create_data_id = create_response.get("data", {}).get("id")
    create_error = create_response.get("error")

    # Print create task result
    print("Create Task Result:")
    print("error_code:", create_error_code)
    print("data.id:", create_data_id)
    print("error:", create_error)
    print()

    # Get task result
    while True:
        # Get result
        result_params = {
            "key": key
        }

        result_response = requests.get(f"{result_url}/{create_data_id}", params=result_params).json()

        # Parse result response
        done_status = result_response.get("done")
        hijack_num = result_response.get("hijack_num")
        max_node = result_response.get("max_node")

        # Print result
        print("Task Result:")
        print("done:", done_status)
        print("Hijacked Nodes:", hijack_num)
        print("max_node:", max_node)
        print()

        # Check if task is done
        if done_status:
            break

        # Wait for 5 seconds before requesting task result again
        time.sleep(5)