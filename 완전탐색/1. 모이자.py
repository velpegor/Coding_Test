import sys
INT_MAX = sys.maxsize
n = int(input())
arr = list(map(int,input().split()))

sum_dis = INT_MAX
for i in range(n):
    total_dis = 0
    for j in range(n):
        total_dis += arr[j] * abs(j-i)

    sum_dis = min(sum_dis, total_dis)

print(sum_dis)