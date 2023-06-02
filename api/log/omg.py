log_file = "path/to/log_file.txt"
normal_file = "path/to/1.txt"
block_file = "path/to/2.txt"

normal_domains = []
block_domains = []

with open(log_file, "r") as log:
    lines = log.readlines()
    for line in lines:
        domain, value = line.split(", ")[0].split(": ")[1], line.split(", ")[1].split(": ")[1]
        if value == "0":
            normal_domains.append(domain)
        elif value == "1":
            block_domains.append(domain)

with open(normal_file, "w") as normal:
    normal.write("----域名正常:\n")
    normal.write("\n".join(normal_domains))

with open(block_file, "w") as block:
    block.write("----域名污染:\n")
    block.write("\n".join(block_domains))

print("----域名正常:")
with open(normal_file, "r") as normal:
    print(normal.read())

print("----域名污染:")
with open(block_file, "r") as block:
    print(block.read())