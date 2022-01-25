#첫째줄에 n을 입력받음. n은 들어올 명령의 줄
n = int(input())

x,y = 0, 0
dx, dy = [1,0,-1,0], [0,1,0,-1]

for i in range(n):
    #이동할 방향과 이동할 거리를 입력받음
    command, distance = input().split()
    if command == 'N':
        move_dir = 1
    elif command == 'E':
        move_dir = 0
    elif command == 'S':
        move_dir = 3
    else:
        move_dir = 2

    x += dx[move_dir] * int(distance)
    y += dy[move_dir] * int(distance)

print(x, y)
