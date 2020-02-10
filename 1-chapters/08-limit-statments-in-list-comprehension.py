matrix = [[1,2,3],[4,5,6],[7,8,9]]

flat = [x for row in matrix for x in row]
print(matrix)
print(flat)

print([[x+1 for x in row] for row in matrix])


print([[x for x in row if x%2==0] for row in matrix])
print([[x for x in row] for row in matrix if row.index])