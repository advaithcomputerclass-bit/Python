def is_even(nums):
    return any(num % 2 == 0 for num in nums)
print(is_even([1,3,5,7,9]))  # Output: True