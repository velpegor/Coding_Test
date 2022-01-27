a, b = map(int,input().split())
arr = [
    list(input().split()) for i in range(a)
]

cnt = 0

for i in range(1, a):
    for j in range(1, b):
        for k in range(i+1, a-1):
            for l in range(j+1,b-1):
                if arr[0][0] != arr[i][j] and \
                        arr[i][j] != arr[k][l] and arr[k][l] != arr[a-1][b-1]:
                    cnt +=1

print(cnt)

#다시 풀어볼 것