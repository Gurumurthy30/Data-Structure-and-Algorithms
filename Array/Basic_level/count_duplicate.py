def count_duplicate(nums: list,target: int):
    ans= 0
    for num in nums:
        if num == target:
            ans+=1
    return ans

print(count_duplicate([1,2,3,1,2,3],1))