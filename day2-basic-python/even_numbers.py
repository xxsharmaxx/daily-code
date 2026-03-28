# Day 2: Even Numbers Program

def find_even_numbers(numbers):
    even_list = []

    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)

    return even_list


# Sample input
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Function call
result = find_even_numbers(nums)

# Output
print("Original List:", nums)
print("Even Numbers:", result)
