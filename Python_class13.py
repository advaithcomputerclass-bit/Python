def has_negative(nums):
    return any(num < 0 for num in nums)
print(has_negative([1, -2, 3, -4, 5]))  # Output: True