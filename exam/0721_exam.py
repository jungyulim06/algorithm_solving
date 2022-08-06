### 1번 문제

## 문제설명
#단체 유니폼을 주문하려고 합니다. 사람들의 덩치를 수치로 표현할 때 주문해야 하는 유니폼의 사이즈는 다음과 같습니다.
#덩치               사이즈
#95 미만               S
#95 이상 100 미만       M
#100 이상 105 미만       L
#105 이상               XL
#사람들의 덩치를 담은 배열 people, people의 길이 people_len이 매개변수로 주어질 때, 주문해야 하는 유니폼 사이즈의 수를 [S, M, L, XL] 순으로 배열에 담아 return 하도록 solution 함수를 작성해주세요.


## 매개변수 설명
#사람들의 덩치를 담은 배열 people, people_len이 solution 함수의 매개변수로 주어집니다.
#people_len은 1 이상 100 이하인 자연수입니다.
#사람들의 덩치는 80 이상 120 이하인 자연수입니다.

## return 값 설명
#주문해야 하는 유니폼 사이즈의 수를 [S, M, L, XL] 순으로 배열에 담아 return 합니다.

## 예시
#people   =[97, 102, 93, 100, 107]
#return =[1, 1, 2, 1]

## 예시설명
#3번째 사람은 S 사이즈를 입어야합니다.
#1번째 사람은 M 사이즈를 입어야합니다.
#2, 4번째 사람은 L 사이즈를 입어야합니다.
#5번째 사람은 XL 사이즈를 입어야합니다.

# 실행 화면 예시
#solution함수의반환값은[1,1,2,1]입니다.



def solution(people):
    answer=[0,0,0,0]
    for i in people:
        if i<95:
            answer[0]+=1   
        elif i<100:
            answer[1]+=1
        elif i<105:
            answer[2]+=1
        elif i>=105:
            answer[3]+=1


    return answer

people=[97, 102, 93, 100, 107]
ret = solution(people)
print("solution 함수의 반환 값은", ret, "입니다.")







## 문제설명
#카드를 3장 뽑아 점수를 내는 게임을 하려고 합니다. 각 카드는 색이 칠해져 있고, 숫자가 적혀 있습니다.
# 획득한 점수를 계산하는 규칙은 다음과 같습니다.
#1. 카드 3장의 색이 모두 같다면 획득한 점수는 적힌 숫자의 총합에 3을 곱한 값입니다.
#2. 카드 2장의 색이 같고, 1장의 색이 다르다면 획득한 점수는 적힌 숫자의 총합에 2를 곱한 값입니다.
#3. 카드 3장의 색이 모두 다르다면 획득한 점수는 적힌 숫자의 총합입니다.
#뽑은 카드의 색과 숫자를 문자열로 담은 2차원 배열 cards, cards의 길이 cards_len이 매개변수로 주어질 때, 획득한 총 점수를 return 하도록 solution 함수를 작성해주세요.

## 매개변수 설명
#뽑은 카드의 색과 숫자를 문자열로 담은 2차원 배열 cards, cards의 길이 cards_len이 solution 함수의 매개변수로 주어집니다.
#cards는 3x2 크기인 2차원 배열입니다.
#cards_len은 항상 3입니다.
#cards의 각 원소는 [색, 숫자] 입니다.
#카드의 색은 ["red", "black", "blue"] 중 하나입니다.
#카드에 적힌 숫자는 1 이상 9 이하인 자연수입니다.

## return 값 설명
#획득한 총 점수를 return 합니다.

## 예시1
#cards = [["blue", "2"], ["red", "5"], ["black", "3"]]
## 예시2
#cards = [["blue", "2"], ["blue", "5"], ["black", "3"]]

## 예시설명
#예제 #1
#모든 카드 색이 모두 다르기 때문에 획득한 점수는 적힌 숫자의 총합인 10 입니다.
#예제 #2
#두 카드 색이 같고, 1장의 색이 다릅니다. 따라서’ 획득한 점수는 적힌 숫자의 총합에 2를 곱한 20 입니다.

#실행 화면 예시
#solution함수의반환값은10입니다.
#solution함수의반환값은20입니다.

def solution(card):
    answer=0
    total=0
    cnt=[0,0,0]
    for col,sor in card:
        print(col,sor)
        total+=int(sor)

        if col=="blue":
            cnt[0]+=1
        elif col[0]=="red":
            cnt[1]+=1
        elif col[0]=="black":
            cnt[2]+=1
            print(cnt,total)
    if max(cnt)==1:
        answer=total
    elif max(cnt)==2:
        answer=total*2
    elif max(cnt)==3:
        answer=total*3 



    return answer

cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

print("solution 함수의 반환 값은", ret2, "입니다.")