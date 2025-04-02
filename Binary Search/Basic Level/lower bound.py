#binary serach

def binary_serach(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        #check mid element is equal to target
        if arr[mid] == target:
            return arr[mid]
        #if mid element is less than target
        elif arr[mid] < target:
            left = mid + 1
        #if mid element is greater than target
        else:
            right = mid - 1
    return arr[right] #if target not found it return the next lower element to target


print("Case 1: \n",binary_serach([1,3,5,6,8,9,10], 10))
print("Case 2: \n",binary_serach([1,3,4,7,8,9,10], 6))