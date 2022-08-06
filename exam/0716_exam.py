
# 1. 현희랑 유림이가 가위바위보를 해! (가위:0, 바위:1, 보:2)
## 현희는 [0,1,1,2,2,2,0,0,0,1,1,2,3] 이렇게 냈고,
## 유림이는 [1,1,0,2,1,2,0,2,1,0,2,3,1] 이렇게 냈어
## 현희가 [이긴 횟수, 비긴 횟수, 진 횟수]를 리스트에 담아서 나타내주세요
## 유림이가 [이긴 횟수, 비긴 횟수, 진 횟수]를 리스트에 담아서 나타내주세요

print(">>>","1번")
a=[0,1,1,2,2,2,0,0,0,1,1,2,3] 
b=[1,1,0,2,1,2,0,2,1,0,2,3,1]

a_result=[0,0,0]
b_result=[0,0,0]

for A,B in zip(a,b):
    if(A==0 and B==2)or(A==1 and B==0) or (A==2 and B==1):
        a_result[0]+=1
        b_result[2]+=1
    elif A==B:
        a_result[1]+=1
        b_result[1]+=1
    else:
        a_result[2]+=1
        b_result[0]+=1
print(a_result,b_result)

#2. 선생님키 181 유림이키 170 현희키가 175일 때
## 이에 상응하는 Dictionary를 만들고,
## 2-1. 키 순으로 정렬 후, 첫번째 INDEX 항목 PRINT 하세요(오름차순)
## 2-2. 이름 순으로 정렬 후, 첫번째 INDEX 항목 PRINT 하세요(내림차순)
print(">>>","2번")
name_dict={'성현':181,'유림':170,'현희':175}
print(sorted(name_dict.items(),key=lambda x:x[1]))
print(sorted(name_dict.items(),reverse=True,key=lambda x:x[0]))


#3. 현재 KTX 자리를 예매 하려고해
## 전광판 현황 [1,0,3,4,5,0,7,8,9,10,11,12,0,14,15,16,17,18,0,20,21,22,23,0,0,26,0,0,29]
## 0이 아닌 숫자가 있는 자리는 예약 가능 자리, 0 이 있는 자리는 선 예약이 된 자리야
## 근데,,, 방금 B학교에서 2의 배수 자리를 다 예약 해버렸고,
## 그 다음 바로 C학교에서는 3의 배수 자리를 다 예약 해버렸고
## 그 다음 바로 A학교에서는 5의 배수 자리를 다 예약 해버렸어.
## 3-1. A학교가 예약한 자리의 갯수, B학교가 예약한 자리의 갯수, C학교가 예약한 자리의 갯수를 딕셔너리에 담아서 나타내기
## 3-2. 남은 자리는 몇자리가 있고, 어떤 자리가 남았는 지 나타내기

print(">>>","3번")
board=[1,0,3,4,5,0,7,8,9,10,11,12,0,14,15,16,17,18,0,20,21,22,23,0,0,26,0,0,29]
school_dict = {'A':0, 'B':0, 'C':0}
left_list = []

for idx,num in enumerate(board):
    if num==0:
        continue
    elif num%2==0:
        school_dict['B']+=1
    elif num%3==0:
         school_dict['C']+=1
    elif num%5==0:
         school_dict['A']+=1
    else:
        left_list.append(idx+1)
print(school_dict)
print(left_list, len(left_list))
   
# 4. 미로가 있어서 출발지점에서 도착지점으로 가려고 해 (시작점 -1, 장애물 1, 갈 수 있는 곳 0, 도착점 2)
## [ 0, 0, 0, 0]
## [ 0, 1, 1, 0]
## [ 0, -1, 1, 0]
## [ 1, 1, 1, 0]
## [ 2, 0, 0, 0]
## MAZE = [[ 0, 0, 0, 0], [ 0, 1, 1, 0], [ 0, -1, 1, 0], [ 1, 1, 1, 0],[ 2, 0, 0, 0] ]
## 몇 번 거쳐서 갈 수 있는 지? 나타내기
## 어느 점을 거쳐서 갈 수 있는지? 나타내기
## (-1은 (0,0)이고, 2는 (2,2)이고, 맨 오른쪽 상단은 (0,2)라고 가정)

print(">>>","4번")
MAZE = [[ 0, 0, 0, 0], [ 0, 1, 1, 0], [ 0, -1, 1, 0], [ 1, 1, 1, 0],[ 2, 0, 0, 0] ]
print(len(MAZE))
print(len(MAZE[0]))
VISITED=[[False]*len(MAZE[0]) for x in range(len(MAZE))]
for x in VISITED:
    print(x)
DIR=[[-1,0],[1,0],[0,-1],[0,1]]
CUR=[2,1]
endFlag=False
path=[]
path.append([CUR[0],CUR[1]])
while True:
    for row,col in DIR:
        newRow=CUR[0]+row
        newCol=CUR[1]+col
        if newRow<0 or newCol<0 or newRow>len(MAZE)-1 or newCol>len(MAZE[0])-1:
            # print(" 초과",[newRow,newCol])
            continue
        elif VISITED[newRow][newCol]==True:
            # print("이미 간곳 입니다",[newRow,newCol])
            continue
        elif MAZE[newRow][newCol]==1:
            # print("장애물입니다",[newRow,newCol])
            continue
        elif MAZE[newRow][newCol]==0:
            # print("새로운 곳에 도착",[newRow,newCol])
            VISITED[newRow][newCol]=True
            path.append([newRow,newCol])
            CUR[0]=newRow
            CUR[1]=newCol
            break
        elif MAZE[newRow][newCol]==2:
            # print("도착했습니다",[newRow,newCol])
            path.append([newRow,newCol])
            endFlag=True
            break
    if endFlag==True:
        break
            
print(path)
print(len(path))