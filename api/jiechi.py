import requests

log_file = "/Users/steven/Desktop/ceshicunchu/api/domain_list.txt" # Đường dẫn tới tệp log_domain.txt
output_file = "/Users/steven/Desktop/ceshicunchu/api/result.txt"  # Đường dẫn tới tệp lưu kết quả

api_key = "97fa88c09ec4fe9ebdc614ecfa361461"  # Thay thế bằng API key của bạn

# Đọc các tên miền từ tệp log_domain.txt
with open(log_file, 'r') as file:
    domains = file.readlines()

# Loại bỏ khoảng trắng và ký tự xuống dòng
domains = [domain.strip() for domain in domains]

# Kiểm tra từng tên miền
results = []
for domain in domains:
    create_task_url = f"https://api.boce.com/v3/task/create/hijack?key={api_key}&host={domain}"
    response = requests.get(create_task_url)
    task_data = response.json()

    if response.status_code == 200 and task_data.get('error_code') == 0:
        task_id = task_data['data']['id']
        result_url = f"https://task.boce.com/v3/task/hijack/{task_id}?key={api_key}"
        result_response = requests.get(result_url)
        result_data = result_response.json()

        hijack_num = result_data.get('hijack_num', 0)
        results.append(f"Domain: {domain}, Hijack Num: {hijack_num}")
    else:
        results.append(f"Failed to check domain: {domain}")

# Lưu kết quả vào tệp output_file
with open(output_file, 'w') as file:
    file.write('\n'.join(results))

print("Kết quả đã được lưu vào tệp result.txt")