def max_min(arr):
    max = arr[0]
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return min,max

print(max_min([1,3,5,6,8,9,10]))