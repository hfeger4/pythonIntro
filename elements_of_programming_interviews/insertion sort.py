

def insertion_sort(arr):
    for i in range(1,len(arr)):

        currentvalue = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > currentvalue:
            arr[pos] = arr[pos-1]
            pos = pos-1
        arr[pos] = currentvalue
    return arr


print(insertion_sort([1,3,2,5,4,3]))