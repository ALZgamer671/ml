def binsearch(nums, target):
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
    return -1


print(binsearch([1, 2, 3, 4, 5, 6], 4))
print(binsearch([], 1))
print(binsearch([1, 2, 3, 4, 5], 6))
