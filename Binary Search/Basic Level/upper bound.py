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
    return arr[left] #if target not found

print("Case 1: \nIndex position:",binary_serach([1,3,5,6,8,9,10], 10))
#print("Case 2: \nIndex position:",binary_serach([1,3,5,6,8,9,10], 11))
print("Case 2: \nIndex position:",binary_serach([1,3,5,6,8,9,10], 1))