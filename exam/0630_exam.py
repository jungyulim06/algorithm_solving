# 1. 현희랑 유림이가 가위바위보를 해! (가위:0, 바위:1, 보:2)
## 현희는 [0,1,1,2,2,2,0,0,0,1] 이렇게 냈고,
## 유림이는 [1,1,0,2,1,2,0,2,1,0] 이렇게 냈어
## 현희가 [이긴 횟수, 비긴 횟수, 진 횟수]를 리스트에 담아서 나타내주세요
## 유림이가 [이긴 횟수, 비긴 횟수, 진 횟수]를 리스트에 담아서 나타내주세요
a=[0,1,1,2,2,2,0,0,0,1]#현희
b=[1,1,0,2,1,2,0,2,1,0]#유림
a_result=[0,0,0]
b_result=[0,0,0]
for c,d in zip(a,b):
    if (c==0 and d==2) or (c==1 and d==0) or (c==2 and d==1):
        a_result[0]+=1
        b_result[2]+=1
    elif c==d:
        a_result[1]+=1
        b_result[1]+=1
    else:
        a_result[2]+=1
        b_result[0]+=1

print("1.", a_result,b_result)
print()





#2. 선생님키 181 유림이키 170 현희키가 175일 때
## 이에 상응하는 Dictionary를 만들고,
## 2-1. 키 순으로 정렬 후, 첫번째 INDEX 항목 PRINT 하세요(오름차순)
## 2-2. 이름 순으로 정렬 후, 첫번째 INDEX 항목 PRINT 하세요(내림차순)

dict_c={'성현':181,'유림':170,'현희':171}

a = sorted(dict_c.items(),key=lambda x:x[1])
print(a)
b= sorted(dict_c.items(),reverse=True,key=lambda x:x[0])
print(b)
print(a[0])
print(b[0])

