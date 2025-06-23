m= [[1,2,3],[4,5,6],[7,8,9]]
print("Row:", [sum(r) for r in m])
print("Col:", [sum(m[i][j] for in range (3)) for j in range(3)])
print("Main Diag:", sum(m[i][i] for i in range(3)))
print ("Anti Diag:", sum(m[i][2-i] for i in range(3)))
