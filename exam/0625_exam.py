# 1. 1~100 중에서 2,3,5의 배수의 숫자들만 모여있는 a라는 변수의 list를 구해보세요 

## 1-1. list comprehension을 꼭 사용해 주세요


from msilib.schema import BBControl


a = [x for x in range(1, 101) if x%2==0 or x%3==0 or x%5==0]

print("1-1 :  ",a)

## 1-2. list comprehension을 사용하지 않아도 괜찮아요
a=[]
for i in range(1,101):
    if i%2==0 or i%3==0 or i%5==0:
        a.append(i)
print("1-2 :  ",a)

# 2. 1에서 만든 a라는 변수에서 5의 배수일 경우에는 a의 제일 적은 idx에서 값을 빼고, 그 외의 경우에는 제일 큰 idx에서 값을 빼서 item을 가지고 b라는 변수의 list를 만들어주세요

# a에서 뺀 item은 무조건 b에 넣어야 하고, 차례대로 넣어야 합니다.

b = []
a_copy = [x for x in a]
for i in a:
    if i%5 == 0:
        b.append(a_copy.pop(0))
    else:
        b.append(a_copy.pop())
print('2: ', b,end='\n\n')



# 3. 1~100 중에서 2의 배수만 모아둔 c라는 변수의 set을 만들어주세요. 그리고 3의 배수만 모아둔 d라는 변수의 set을 만들어 주세요

c=set()
for  i in range(1,101):
    if i%2==0:
        c.add(i)
print("3(2의 배수):  ",c)

d=set()
for i in range(1,101):
    if i%3==0:
        d.add(i)
print("3(3의 배수):  ",d)

# 4. c와 d변수를 이용해서
## 4-1. 서로 같은 item을 뽑아주세요
g=c&d
print("4-1:  ",g)

## 4-2. 각 각 포함하고 있는 모든 item을 뽑아주세요
print("4-2:  ",c|d)

## 4-3. c는 있지만 d에는 있지 않은 item을 뽑아주세요
print("4-3:  ",c-d)

# 5. e=[1,6,2,7,5,8,3,6,1,5,8,3,9,74,36,2]
## 5-1. e에서 중복되는 값을 제거하고, f라는 변수에 넣으세요
e=[1,6,2,7,5,8,3,6,1,5,8,3,9,74,36,2]
f = list(set(e))
print("5-1:  ",f)
## 5-2. f라는 변수를 정렬해주세요 (오름차순으로)
f.sort()
print("5-2:  ",f)
## 5-3. f라는 변수를 정렬해주세요 (내림차순으로)
f.sort(reverse=True)
print("5-3:  ",f)
## 5-4. f라는 변수로 g라는 변수를 정렬해주세요 (오름차순으로)
g=sorted(f)
print("5-4:  ",g)
## 5-4. f라는 변수로 g라는 변수를 정렬해주세요 (내림차순으로)
g_reverse=sorted(f,reverse=True)
print("5-5:  ",g_reverse)