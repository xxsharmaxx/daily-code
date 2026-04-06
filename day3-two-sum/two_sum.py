# Day 3: Two Sum (Optimized - O(n))

def two_sum(nums, target):
    num_map = {}  # stores number -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

    return []


# Example
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)

print("Input:", nums)
print("Target:", target)
print("Output:", result)
