print("1번")
VISITED=[[False]*3 for x in range(4)]
print(VISITED)
for x in VISITED:
    print(x)

print("2번")
CUR=[3,4]
DIR=[[-1,0],[1,0],[0,-1],[0,1]]
for row,col in DIR:
    newRow=CUR[0]+row
    newCol=CUR[1]+col
print(row,col)

print("3번")
PNTS = [[0,0], [0,1], [0,2], [0,3], [0,4], [1,4], [2,1], [2,2], [2,3], [2,4], [3,4], [4,4]]

VISITED=[[False]*6 for x in range(5)]
for a in VISITED:
    print(x)
print()

for row,col in PNTS:
    VISITED[row][col]=True
for x in VISITED:
    print(x)

print("4번")

VISITED=[[False]*6 for x in range(4)]
for x in VISITED:
    print(x)

CUR=(2,3)
VISITED[CUR[0]][CUR[1]]=True
DIR=[[-1,0],[1,0],[0,-1],[0,1]]
for row,col in DIR:
    newRow=CUR[0]+row
    newCol=CUR[1]+col
    print(newRow,newCol)

    VISITED[newRow][newCol]=True
for x in VISITED:
    print(x)



print("5번_시험")


MAZE = [[-1, 0, 1],[ 1, 0, 0],[ 1, 1, 0], [ 1, 1, 2]]
VISITED=[[False]*3 for x in range(4)]
for x in VISITED:
    print(x)
DIR=[[-1,0],[1,0],[0,-1],[0,1]]
for row,col in DIR:
    newRow=[]


MAZE = [[-1, 0, 1],[ 1, 0, 0],[ 1, 1, 0], [ 1, 1, 2]]
VISITED = [[False]*3 for x in range(4)]
print(MAZE)
print(VISITED)
DIR = [[-1,0], [1,0], [0,-1], [0,1]]
cur = [0,0]
VISITED[cur[0]][cur[1]] = True
endFlag = False

for item in VISITED:
    print(item)
print()


print(MAZE)
print(len(MAZE))

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

