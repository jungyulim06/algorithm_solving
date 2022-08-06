# 4. 미로가 있어서 출발지점에서 도착지점으로 가려고 해 (시작점 -1, 장애물 1, 갈 수 있는 곳 0, 도착점 2)
## [-1, 0, 1]
## [ 1, 0, 0]
## [ 1, 1, 0]
## [ 1, 1, 2]
## MAZE = [[-1, 0, 1],[ 1, 0, 0],[ 1, 1, 0], [ 1, 1, 2]]
## 몇 번 거쳐서 갈 수 있는 지? 나타내기 4
## 어느 점을 거쳐서 갈 수 있는지? 나타내기 (0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2)
## (-1은 (0,0)이고, 2는 (2,2)이고, 맨 오른쪽 상단은 (0,2)라고 가정)
## (미로 밖으로 나갈 수는 없음, 최소 거리를 구해야 함)
MAZE = [[-1, 0, 1],[ 1, 0, 0],[ 1, 1, 0], [ 1, 1, 2]]
VISITED = [[False]*3 for x in range(4)]
print(MAZE)
print(VISITED)


# 1. 상 하 좌 우를 본다
# 2. 한 번 간 자리인지 확인한다.
# 3. 0 인 자리로 이동한다.
# 4. 0인 자리가 한 번 간 자리라고 바꾼다.

# (0,0)
# 상 -> (-1,0)
# 하 -> (1,0)
# 좌 -> (0,-1) 
# 우 -> (0,1)
# Direction : 방향
# Row : 행
# Column(Col) : 열
# Current(Cur) : 현재
# Visit : 방문하다
DIR = [[-1,0], [1,0], [0,-1], [0,1]]

# print("<<<<", DIR[0][0], DIR[1][0], DIR[2][0], DIR[3][0])
# print()
# for item in DIR:
#     print(item)
# print()
# for row, col in DIR:
#     print(row, col)
# print()
# for item in VISITED:
#     print(item)
# print()

cur = [0,0]
VISITED[cur[0]][cur[1]] = True
endFlag = False

for item in VISITED:
    print(item)
print()

print(MAZE)

while True:
    for row, col in DIR:
        newRow = cur[0]+row
        newCol = cur[1]+col
        if newRow<0 or newRow>3 or newCol<0 or newCol>2:
            print("index 초과 했습니다.", newRow, newCol)
            continue
        elif MAZE[newRow][newCol] == 1:
            print("장애물에 닿았습니다", newRow, newCol)
            continue
        elif VISITED[newRow][newCol] == True:
            print("이미 간 곳이에요", newRow, newCol)
            continue
        elif MAZE[newRow][newCol] == 2:
            print("도착했습니다", newRow, newCol)
            endFlag = True
            break
        elif MAZE[newRow][newCol] == 0:
            print("새로운 점에 들어왔습니다.", newRow, newCol)
            VISITED[newRow][newCol] = True
            cur[0] = newRow
            cur[1] = newCol
            print()
            for item in VISITED:
                print(item)
            print()
            break
    if endFlag:
        break
