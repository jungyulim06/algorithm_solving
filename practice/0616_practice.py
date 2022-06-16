##set 형 함수를 통해서 만드시오 
#1
a=set()
for i in range(1,6):
    a.add(i)
print(a)

#2
b=set([i for i in range(1,6)])
print(b)

#3
c =[1,2,3,4,5]
set(c)
print(c)


d=[1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,76,3,2,5,3,6,4,62,23,11,1]
d= set(d)
print(len(d))

s=[1,5,2,3,4,6,2,76,2,3,5,4]
d=set(s)
print(d)
f=[1,5,6,3,7,2,5,4,6,2,5,3,1,6,55,3,86,3,2,5,3,6,4,62,23,11,1]
v= set(f)
print(d)

#차집합
print(len(v-d))
# 합집합
print(len(v|d))
#교집합
print(len(v&d))


c={}
c['성현']=181
c['유림']=162
c['현희']=171
print(sorted(c.items(),key=lambda x:x[1]))
print(sorted(c.items(),reverse=True,key=lambda x:x[1]))
print(sorted(c.items(),key=lambda x:x[0]))
print(sorted(c.items(),reverse=True,key=lambda x:x[0]))
