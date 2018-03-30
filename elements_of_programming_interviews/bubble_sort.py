def bubble_sort(arr):
    sorted = False

    while sorted != True:
        sorted = True
        i = 0
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
            i += 1
    return arr

print(bubble_sort([1,5,4,2,3]))

