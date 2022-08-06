# 1. 현희랑 유림이가 가위바위보를 해! (가위:0, 바위:1, 보:2)
## 현희는 [0,1,1,2,2,2,0,0,0,1] 이렇게 냈고,
## 유림이는 [1,1,0,2,1,2,0,2,1,0] 이렇게 냈어
## 현희가 [이긴 횟수, 비긴 횟수, 진 횟수]를 리스트에 담아서 나타내주세요
## 유림이가 [이긴 횟수, 비긴 횟수, 진 횟수]를 리스트에 담아서 나타내주세요
A = [0,1,1,2,2,2,0,0,0,1]
B = [1,1,0,2,1,2,0,2,1,0]
A_result = [0,0,0]
B_result = [0,0,0]
for a,b in zip(A,B):
    if (a==0 and b==2) or (a==1 and b==0) or (a==2 and b==1):
        A_result[0]+=1
        B_result[2]+=1
    elif a==b:
        A_result[1]+=1
        B_result[1]+=1
    else:
        A_result[2]+=1
        B_result[0]+=1
print('1번')
print(A_result, B_result)
print()

#2. 선생님키 181 유림이키 170 현희키가 175일 때
## 이에 상응하는 Dictionary를 만들고,
## 2-1. 키 순으로 정렬 후, 첫번째 INDEX 항목 PRINT 하세요(오름차순)
## 2-2. 이름 순으로 정렬 후, 첫번째 INDEX 항목 PRINT 하세요(내림차순)
print('2번')
name_to_height_dict = {'성현':181, '유림':170, '현희':175}
sorted_by_height_list = sorted(name_to_height_dict.items(), key=lambda x: x[1])
print(sorted_by_height_list[0])
sorted_by_name_list = sorted(name_to_height_dict.items(), key=lambda x:x[0], reverse=True)
print(sorted_by_name_list[0])
print()

#3. 현재 KTX 자리를 예매 하려고해
## 전광판 현황 [1,0,3,4,5,0,7,8,9,10,11,12,0,14,15,16,17,18,0,20]
## 0이 아닌 숫자가 있는 자리는 예약 가능 자리, 0 이 있는 자리는 선 예약이 된 자리야
## 근데,,, 방금 A학교에서 2의 배수 자리를 다 예약 해버렸고,
## 그 다음 바로 B학교에서는 3의 배수 자리를 다 예약 해버렸고
## 그 다음 바로 C학교에서는 5의 배수 자리를 다 예약 해버렸어.
## 3-1. A학교가 예약한 자리의 갯수, B학교가 예약한 자리의 갯수, C학교가 예약한 자리의 갯수를 딕셔너리에 담아서 나타내기
## 3-2. 남은 자리는 몇자리가 있고, 어떤 자리가 남았는 지 나타내기
board = [1,0,3,4,5,0,7,8,9,10,11,12,0,14,15,16,17,18,0,20]
school_count_dict = {'A':0, 'B':0, 'C':0}
left_list = []
for idx, num in enumerate(board):
    if num == 0:
        continue
    elif num%2 == 0:
        school_count_dict['A']+=1
    elif num%3 == 0:
        school_count_dict['B']+=1
    elif num%5 == 0:
        school_count_dict['C']+=1 
    else:
        left_list.append(idx+1)
print('3번')
print(school_count_dict)
print(left_list, len(left_list))
print()

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
# Count(cnt) : (숫자를)세다
# Path : 길

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

# cur = [0,0]
# VISITED[cur[0]][cur[1]] = True
# endFlag = False

# for item in VISITED:
#     print(item)
# print()

# print(MAZE)

## 어떤 변수가 필요한지?? 
MAZE = [[-1, 0, 1],[ 1, 0, 0],[ 1, 1, 0], [ 1, 1, 2]] #문제에서 주는 변수
VISITED = [[False]*3 for x in range(4)] #갔던 곳을 다시 가지 않기 위해서
cur = [0,0] #현재 자기 위치를 저장하기 위해서
endFlag = False #끝나는 부분을 찾기 위해서 (2일 때)
path = [] #자기가 갔었던 위치를 저장하기 위해서
DIR = [[-1,0], [1,0], [0,-1], [0,1]] #상하좌우를 알기 위해서
path.append((0,0))
VISITED[0][0] = True

## 어떤 조건문이 들어갈지?? 5개 (안되는거 3개 + 되는 점 1 + 도착점 1)
## 어떤 반복문이 들어갈지?? 2개
while True: #cur 점이 바뀌기 때문에
    for row, col in DIR: #한 점에 대해서 상하좌우
        newRow = cur[0]+row
        newCol = cur[1]+col
        if newRow<0 or newRow>3 or newCol<0 or newCol>2:
            print("첫번째 if문 : index 초과 했습니다.", newRow, newCol)
            continue
        elif MAZE[newRow][newCol] == 1:
            print("두번째 if문 : 장애물에 닿았습니다", newRow, newCol)
            continue
        elif VISITED[newRow][newCol] == True:
            print("세번째 if문 : 이미 간 곳이에요", newRow, newCol)
            continue
        elif MAZE[newRow][newCol] == 2:
            print("네번째 if문 : 도착했습니다", newRow, newCol)
            path.append((newRow, newCol))
            endFlag = True
            break
        elif MAZE[newRow][newCol] == 0:
            print("다섯번째 if문 : 새로운 점에 들어왔습니다.", newRow, newCol)
            VISITED[newRow][newCol] = True
            cur[0] = newRow
            cur[1] = newCol
            path.append((newRow, newCol))
            # print()
            # for item in VISITED:
            #     print(item)
            # print()
            break
    if endFlag:
        break
print('1번 답 : 거쳐간 점은 ?', len(path))
print('2번 답 : 거쳐간 점은 뭐야???', path)
# 거쳐 간 점이 몇개가 있는 지??