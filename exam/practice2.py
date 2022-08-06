# 1. 현희랑 유림이가 가위바위보를 해! (가위:0, 바위:1, 보:2)
## 현희는 [0,1,1,2,2,2,0,0,0,1] 이렇게 냈고,
## 유림이는 [1,1,0,2,1,2,0,2,1,0] 이렇게 냈어
## 현희가 [이긴 횟수, 비긴 횟수, 진 횟수]를 리스트에 담아서 나타내주세요
## 유림이가 [이긴 횟수, 비긴 횟수, 진 횟수]를 리스트에 담아서 나타내주세요

A=[0,1,1,2,2,2,0,0,0,1]
B=[1,1,0,2,1,2,0,2,1,0]

a_result=[0,0,0]
b_result=[0,0,0]

for a,b in zip(A,B):
    if(a==0 and b==2)or(a==1 and b==0)or(a==2 and b==1):
        a_result[0]+=1
        b_result[2]+=1
    elif a==b:
        a_result[1]+=1
        b_result[1]+=1
    else:
        a_result[2]+=1
        b_result[0]+=1
print(a_result, b_result)
print()
#2. 선생님키 181 유림이키 170 현희키가 175일 때
## 이에 상응하는 Dictionary를 만들고,
## 2-1. 키 순으로 정렬 후, 첫번째 INDEX 항목 PRINT 하세요(오름차순)
## 2-2. 이름 순으로 정렬 후, 첫번째 INDEX 항목 PRINT 하세요(내림차순)





c = {}
c['성현'] = 181
c['유림'] = 162
c['현희'] = 171

## 5-1. dict sorting, 키순으로 dictionary 정렬하기(오름차순)
print(sorted(c.items(),key=lambda x:x[1]))
## 5-2. dict sorting, 키순으로 dictionary 정렬하기(내림차순)
print(sorted(c.items(),reverse=True,key=lambda x:x[1]))
## 5-3. dict sorting, 이름순으로 dictionary 정렬하기(오름차순)
print(sorted(c.items(),key=lambda x:x[0]))
## 5-4. dict sorting, 이름순으로 dictionary 정렬하기(내림차순
print(sorted(c.items(),reverse=True,key=lambda x:x[0]))
print()

name_to_height_dict = {'성현':181, '유림':170, '현희':175}
sorted_by_height_list = sorted(name_to_height_dict.items(), key=lambda x: x[1])
print(sorted_by_height_list[0])
sorted_by_name_list = sorted(name_to_height_dict.items(), key=lambda x:x[0], reverse=True)
print(sorted_by_name_list[0])
print()


#2번 다시 외우기

#3. 현재 KTX 자리를 예매 하려고해
## 전광판 현황 [1,0,3,4,5,0,7,8,9,10,11,12,0,14,15,16,17,18,0,20]
## 0이 아닌 숫자가 있는 자리는 예약 가능 자리, 0 이 있는 자리는 선 예약이 된 자리야
## 근데,,, 방금 A학교에서 2의 배수 자리를 다 예약 해버렸고,
## 그 다음 바로 B학교에서는 3의 배수 자리를 다 예약 해버렸고
## 그 다음 바로 C학교에서는 5의 배수 자리를 다 예약 해버렸어.
## 3-1. A학교가 예약한 자리의 갯수, B학교가 예약한 자리의 갯수, C학교가 예약한 자리의 갯수를 딕셔너리에 담아서 나타내기
## 3-2. 남은 자리는 몇자리가 있고, 어떤 자리가 남았는 지 나타내기

