def find_two_largest(nums):
    first, second = float('-inf'), float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return first, second

numbers = [12, 35, 1, 10, 34, 1]
largest, second_largest = find_two_largest(numbers)
print(f"First largest: {largest}")
print(f"Second largest: {second_largest}")
