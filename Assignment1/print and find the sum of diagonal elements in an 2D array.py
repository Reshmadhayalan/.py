n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
diag_sum = sum(matrix[i][i] for i in range(n))
print("Diagonal elements:", *[matrix[i][i] for i in range(n)])
print("Sum:", diag_sum)
