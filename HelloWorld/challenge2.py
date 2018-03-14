

ip_address = "127.0.0.1"

count = 0
arr = []
for i in range(0,len(ip_address)):
    if ip_address[i] == ".":
        arr.append(count)
        count = 0
    if ip_address[i] in "0123456789":
        count += 1
    if i == (len(ip_address) - 1):
        arr.append(count)

print(arr)