# 미로가 있어서 출발지점에서 도착지점으로 가려고 해 (시작점 -1, 장애물 1, 갈 수 있는 곳 0, 도착점 2)
## [-1, 0, 1]
## [ 1, 0, 0]
## [ 1, 1, 0]
## [ 1, 0, 0]
## [ 2, 0, 1]

# 1. 최소 몇 번의 점으로 갈 수 있나요?
# 2. 어떤 점을 거쳐서 갈 수 있나요?

from sqlite3 import Row


MAZE = [[-1, 0, 1], [ 1, 0, 0], [ 1, 1, 0], [ 1, 0, 0], [ 2, 0, 1]]

VISITED=[[False]*3 for x in range(5)]
print(VISITED)
for x in VISITED:
    print(x)

DIR=[[-1,0],[1,0],[0,-1],[0,1]]
CUR=[0,0]
path=[]
endFlag=False
cnt=0
path.append([0,0])

while True:
    for row,col in DIR:
        newRow = CUR[0]+row
        newCol = CUR[1]+col
        if newRow<0 or newCol<0 or newRow>4 or newCol>2:
            print("index 초과",[newRow,newCol])
            continue
        elif MAZE[newRow][newCol]==1:
            print("장애물입니다",[newRow,newCol])
            continue
        elif VISITED[newRow][newCol]==True:
            print("이미 간곳 입니다",[newRow,newCol])
            continue
        elif MAZE[newRow][newCol]==2:
            print("도착했습니다",[newRow,newCol])
            cnt+=1
            path.append([newRow,newCol])
            endFlag=True
            break
        elif MAZE[newRow][newCol]==0:
            print("새로운 곳에 도착",[newRow,newCol])
            cnt+=1
            VISITED[newRow][newCol]=True
            path.append([newRow,newCol])
            CUR[0]=newRow
            CUR[1]=newCol
            break
    if endFlag==True:
        break
print("1번  최소 몇 번의 점으로 갈 수 있나요?",">>>",len(path))
print("2번  어떤 점을 거쳐서 갈 수 있나요?",">>>",path)





