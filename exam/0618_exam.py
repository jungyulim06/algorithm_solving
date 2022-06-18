# 오늘은 set, dict을 집중적으로 다뤄볼예정입니다
## 1. dict, set을 만들어 봅시다. (빈 dict, 빈 set)

## 1-1. dict 어떻게 만들지??

from multiprocessing.sharedctypes import Value
from webbrowser import get


a={}
print(a)

b=dict()
print(b)



## 1-2. set 어떻게 만들지??
a={1,2,3}
print(a)
print()

b=set()
print(b)


## 1-3. list 어떻게 만들지??
a=[]
print(a)

b=list()
print(b)



## 2. set형 함수 (2가지)
a=set()
a.add(1)
a.remove(1)
print(a)


## 3. dict형 함수?? (4가지)
c={"a":1,"b":2}

print(c.get("a"))
print(list(c.values()))
print(list(c.items()))
print(list(c.keys()))




## 4. set 심화

## 4-1. set() 내장함수랑, set형 함수를 통해서 만들어보시오
### 첫 번째 방법

a=set()
for i in range(1,6):
    a.add(i)
print(a)



### 두 번째 방법
b=set(i for i in range(1,6))
print(b)

### 세 번째 방법
c=[1,2,3,4,5]
c=set(c)
print(c)






## 4-2. 카드팩 A는 
## 1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,76,3,2,5,3,6,4,62,23,11,1 숫자카드가 존재
## 이 있다. 총 몇가지의 숫자 카드를 가지고 있나요?
a=[1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,76,3,2,5,3,6,4,62,23,11,1]
a= set(a)
print(len(a))
## 4-3. 카드팩 B는
## 1,5,2,3,4,6,2,88,2,3,5,4 숫자 카드가 존재
## A 카드팩 종류에서 B 카드팩 종류를 빼면 총 몇가지 종류가 남아 있어?
a=[1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,76,3,2,5,3,6,4,62,23,11,1]
a= set(a)
print(len(a))
b=[1,5,2,3,4,6,2,88,2,3,5,4]
b= set(a)
print(len(a))

print(len(b-a))
## 4-4. 카드팩 A, 카드팩 B의 모든 숫자 카드의 종류의 갯수는?
a=[1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,76,3,2,5,3,6,4,62,23,11,1]
a= set(a)
print(len(a))
b=[1,5,2,3,4,6,2,88,2,3,5,4]
b= set(a)
print(len(a))
## 4-5. 카드팩 A, 카드팩 B에서 같은 숫자 카드는 총 몇가지가 있어?
print(len(b&a))



## 5. dict 심화
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






##1.변수 이름이 a이고 [1,2,3,4,5,6,7,10]인 리스트를 print 하세요

a=[1,2,3,4,5,6,7,8,9,10]
print(a)

## 2.변수 이름이 b이고 [1,2,3,4,…100] 인 리스트를 print 하세요

b=[]
for i in range(1,101):
    b.append(i)
print(b)

##3.변수 이름이 c이고 [1,2,3,4,…100] 인 리스트를 list comprehension을 사용해서 print 하세요
c=[x for x in range(1,101)] 
print(c)
## 4.변수 이름이 d이고 [1~100 사이의 3의 배수] 인 리스트를 for문 사용해서 print하세요 
d=[]
for i in range(1,101):
    if(i%3==0):
       d.append(i)
print(d)


## 5-1.변수 이름이 e이고 [1~100 사이의 4의 배수] 인 리트스를 while문(while True 사용 o) 사용해서 print 하세요
e=[]
i=1
while True:
    i+=1
    if i%4==0:
        
        e.append(i)
    if i>100:
        break

##5-2.변수 이름이 e이고 [1~100 사이의 4의 배수] 인 리트스를 while문(while True 사용 x) 사용해서 print 하세요

f=[]
i=1
while i<100:
    i+=1
    if i%4==0:
        f.append(i)
print(f)

##6.g=[0,0,0] 일 때, index 접근을 통해서 g=[10,1,7]로 바꾸고 print 하세요
g=[0,0,0]
g[0]+=10
g[1]+=1
g[2]+=7
print(g)


## 7.list형 함수를 통해서 g=[1]로 바꾸고 print 하세요
g.pop(-1)
g.pop(0)
print(g)

## 8.h=[2,5,3,7,1,2,5,8,2,9] 에서 1) 2의 갯수 2) h의 길이 3) h의 최댓값 4) h의 최솟값 5) h의 합을 print 하세요
h=[2,5,3,7,1,2,5,8,2,9] 


print(len(h))
print(h.count(2))
print(min(h))
print(max(h))
print(sum(h))
## 9-1. h를 가지고 i변수를 새로 만들어서 sorting 하고 print 하세요(오름차순)
h.sort()
print(h)

## 9-2. h를 가지고 sorting 하고 print 하세요(오름차순)
h.sort(reverse=True)
print(h)
##9-3. h를 가지고 i변수를 새로 만들어서 sorting 하고 print 하세요(내림차순)
i=sorted(h)
print(i)
##9-4. h를 가지고 sorting 하고 print 하세요(내림차순)
i_reverse=sorted(h,reverse=True)
print(i_reverse)

