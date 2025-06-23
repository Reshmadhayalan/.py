import math

n = int(input("Enter n: "))
print(sum(math.factorial(i)/i for i in range(1, n+1)))
