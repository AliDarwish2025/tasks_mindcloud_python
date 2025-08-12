import re
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input().ljust(m))
result = ""
for col in range(m):
    for row in range(n):
        result += matrix[row][col]
result = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', result)
print(result)
