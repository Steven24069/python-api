filename = "jiedian.txt"  # Đường dẫn đến file chứa dữ liệu

# Đọc dữ liệu từ file
with open(filename, 'r') as file:
    data = file.read()

# Tách các số riêng biệt từ dữ liệu
numbers = data.split('\n')
formatted_numbers = ','.join(numbers)

print(formatted_numbers)