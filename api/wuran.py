import requests


log_file = "/Users/steven/Desktop/ceshicunchu/api/log/log_domain.txt"
normal_file = "/Users/steven/Desktop/ceshicunchu/api/log/1.txt"
block_file = "/Users/steven/Desktop/ceshicunchu/api/log/2.txt"
test_fail = "/Users/steven/Desktop/ceshicunchu/api/log/3.txt"
non_file = "/Users/steven/Desktop/ceshicunchu/api/log/4.txt"

url = "https://api.boce.com/v3/task/create/pollute"
key = "97fa88c09ec4fe9ebdc614ecfa361461"  # 申请的key

filename = "/Users/steven/Desktop/ceshicunchu/api/domain_list.txt"

# 读取域名列表
with open(filename, "r") as file:
    for domain in file:
        domain = domain.strip()
        response = requests.get(f"{url}?key={key}&host={domain}")

        # 解析JSON响应
        data = response.json().get("data")

        # 提取域名和值
        domain_value = list(data.keys())[0]
        value = data[domain_value]

        # 输出结果
        #print(f"Domain: {domain_value} , Value: {value}")

        with open(log_file, "a") as log:
            log.write(f"Domain: {domain_value} , Value: {value}\n")

def check_domains(log_file, normal_file, block_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    with open(normal_file, 'w') as file_1, open(block_file, 'w') as file_2:
        for line in lines:
            line = line.strip()
            domain_start_index = line.find('Domain: ') + len('Domain: ')
            value_start_index = line.find('Value: ') + len('Value: ')
            domain = line[domain_start_index:line.find(' , Value:')]
            value = line[value_start_index:]
            if value.strip() == '0':
                file_1.write(f"{domain}\n")
            elif value.strip() == '1':
                file_2.write(f"{domain}\n")

check_domains(log_file, normal_file, block_file)

with open(normal_file, 'r') as file_1:
    print("-----域名正常:")
    print(file_1.read())

with open(block_file, 'r') as file_2:
    print("-----域名被污染:")
    print(file_2.read())




line_count = 0
with open(log_file, 'r') as file:
    for line in file:
        line_count +=1
print(f"总共检查 ： {line_count} 个域名 ")


with open(normal_file, 'w') as file_1:
    pass
with open(block_file, 'w') as file_2:
    pass
with open(log_file, 'w') as file:
    pass