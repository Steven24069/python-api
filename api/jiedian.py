import requests

api_key = "40d3791ba08273e1571446ede39bc9a1"

create_task_url = f"https://task.boce.com/v3/node/list?key={api_key}"
create_response = requests.get(create_task_url)
task_data = create_response.json()

#print(task_data)
create_data_id = task_data.get("data", {}).get("id")

print(create_data_id)
for item in task_data.get('data', {}).get('list', []):
    id_value = item.get('id')

    print(id_value)