# 오늘은 set, dict을 집중적으로 다뤄볼예정입니다
## 1. dict, set을 만들어 봅시다. (빈 dict, 빈 set)

## 1-1. dict 어떻게 만들지??

a={}
print(a)

b=dict()
print(b)



## 1-2. set 어떻게 만들지??
a=set()
print(a)

a={}
print(a)



## 1-3. list 어떻게 만들지??
a=list()
print(a)

b=[]
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
c =[1,2,3,4,5]
set(c)
print(c)


### 세 번째 방법
b=set([i for i in range(1,6)])
print(b)


## 4-2. 가지고 있는 숫자카드는 
## 1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,76,3,2,5,3,6,4,62,23,11,1
## 이 있다. 총 몇가지의 숫자 카드를 가지고 있나요?

a= [ 1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,76,3,2,5,3,6,4,62,23,11,1]
a=set(a)
print(len(a))

## 4-3. 새롭게 다른 카드 팩을 구했어 1,5,2,3,4,6,2,88,2,3,5,4 카드가 있대
## 4-2가지고 있던 숫자 카드종류에서 4-3. 카드 종류를 뺀 숫자 카드의 종류 총 몇개?
a=[1,5,2,3,4,6,2,76,2,3,5,4]
b=set(a)
print(b)
c=[1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,86,3,2,5,3,6,4,62,23,11,1]
d= set(c)
print(d)

print(len(d-b))


## 4-4. 4-2의 카드팩, 4-3의 카드팩의 모든 숫자 카드의 종류의 갯수는?

print(len(d|b))

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


