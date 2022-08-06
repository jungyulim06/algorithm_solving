#1


print("1번")
VISITED=[[False]*3 for x in range(5)]
print(VISITED)
## *3은 col 의 갯수, range(5)는 row 의 갯수

#2
print("2번")
CUR=[3,4]
DIR=[[-1,0],[1,0],[0,-1],[0,1]]
for row,col in DIR:
    newRow=CUR[0]+row
    newCol=CUR[1]+col
    print(newRow,newCol)
##한점의 상,하,좌,우를 구하기

#3
PNTS = [[0,0], [0,1], [0,2], [0,3], [0,4], [1,4], [2,1], [2,2], [2,3], [2,4], [3,4], [4,4]]

print("3번")
VISITED=[[False]*6 for x in range(5)]
for x in VISITED:
    print(x)
print() 

for row, col in PNTS:
    VISITED[row][col] = True

for x in VISITED:
    for y in x:
        print(y, end="\t")
    print()
print() 

for x in VISITED:
    print(x)
print() 

print("4번")
VISITED=[[False]*6 for x in range(4)]
print(VISITED)
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
    for y in x:
        print(y, end="\t")
    print()
print() 









