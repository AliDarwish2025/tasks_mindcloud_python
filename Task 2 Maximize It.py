K, M = map(int, input().split())
lists = []

for _ in range(K):
    data = list(map(int, input().split()))
    nums = data[1:]  
    lists.append(nums)

total = 0
for lst in lists:
    max_num = max(lst)   
    total += max_num ** 2

print(total % M)
