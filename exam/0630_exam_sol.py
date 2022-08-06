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