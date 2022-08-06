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