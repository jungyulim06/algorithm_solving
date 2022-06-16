print("연습입니다")

print("1.")
a=[1,2,3,4,5,6,7,8,9,10]
print(a)

print("2.")
b=[]
for i in range(1,101):
    b.append(i)
print(b)

print("3.")
c=[x for x in range(1,101)]
print(c)

print("4.")
d=[]
for i in range(1,101):
    if i%3==0:
        d.append(i)
print(d)


print("5.")

e=[]
i=1
while True:
     i+=1
     if i%4==0:
        e.append(i)
        if i>100:
            break
print(e)

print("5-2.")

f=[]
i=1
while i<100:
    i+=1
    if i%4==0:
        f.append(i)
print(f)

print("6.")
g=[0,0,0]
g[0]+=10
g[1]+=1
g[2]+=7
print(g)

print("7.")
g.pop()
g.pop(0)
print(g)

print("8.")
h=[2,5,3,7,1,2,5,8,2,9]

print("8-1.")
j=0
for i in h:
    if i==2:
        j+=1
print(j)

print("8-2.")
h.count(2)
print(h)
print("8-3.")
print(len(h))
print("8-4.")
print(sum(h))
print("8-5.")
print(min(h))
print("8-6.")
print(max(h))

print("9.")

h.sort()
print(h)

i=sorted(h)
print(i)

h.sort(reverse=True)
print(h)

i_reverse=sorted(h,reverse=True)
print(i_reverse)


