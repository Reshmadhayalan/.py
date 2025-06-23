import math

n = int(input("Enter the number of terms: "))

total_sum = 0
for i in range(1, n + 1):
    s = i * (i + 1) // 2
    total_sum += math.factorial(s)

print("Sum of the series:", total_sum)
