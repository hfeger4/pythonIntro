

ip_address = input("Please enter an IP address")

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


for i in range(0,len(arr)):
    print("In position {} there are {} numbers".format(i,arr[i]))