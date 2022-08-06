#3. 현재 KTX 자리를 예매 하려고해
## 전광판 현황 [1,0,3,4,5,0,7,8,9,10,11,12,0,14,15,16,17,18,0,20]
## 0이 아닌 숫자가 있는 자리는 예약 가능 자리, 0 이 있는 자리는 선 예약이 된 자리야
## 근데,,, 방금 A학교에서 2의 배수 자리를 다 예약 해버렸고,
## B학교에서는 3의 배수 자리를 다 예약 해버렸고
## C학교에서는 5의 배수 자리를 다 예약 해버렸어.
## 3-1. A학교가 예약한 자리의 갯수, B학교가 예약한 자리의 갯수, C학교가 예약한 자리의 갯수를 딕셔너리에 담아서 나타내기

dict_a={'a':0,'b':0,'c':0}

a=[1,0,3,4,5,0,7,8,9,10,11,12,0,14,15,16,17,18,0,20]
for idx, item in enumerate(a):  
    if item==0:
        continue
    elif item%2==0:
        a[idx]=0
        dict_a['a']+=1
    elif item%3==0:
        a[idx]=0
        dict_a['b']+=1
    elif item%5==0:
        a[idx]=0
        dict_a['c']+=1
print(a)
print(dict_a)

## 3-2. 남은 자리는 몇자리가 있고, 어떤 자리가 남았는 지 나타내기
list_a=[]
for i in a:
    if i==0:
        continue
    else:
        list_a.append(i)
print(list_a)
print(len(list_a))


#left_list = []
#for item in a:
#    if item != 0:
#        left_list.append(item)
#print(len(left_list), left_list)
