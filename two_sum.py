# Day 3: Two Sum Problem

def two_sum(nums, target):
    num_map = {}  # Dictionary to store number and index

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in num_map:
            return [num_map[complement], i]

        num_map[nums[i]] = i

    return []


# Example usage
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)

print("Input:", nums)
print("Target:", target)
print("Output (indices):", result)
