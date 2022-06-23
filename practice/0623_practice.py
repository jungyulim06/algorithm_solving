# 1. 구구단 만들기!!

for i in range(1,10):
   print("2","*",i,"=",i*2)
print()
for i in range(1,10):
   print("4","*",i,"=",i*4)
print()
for i in range(1,10):
   print("6","*",i,"=",i*6)



## 2단, 4단 6단만 나오도록! 짜보세요
#유림
for i in range(2,7,2):
    for x in range(1,10):
        print(i,"*",x,"=",i*x)
    print()

#쌤
for a in [2,4,6]:
    for b in range(1,10):
        print(a,"*",b,"=",a*b)
    print()

#현희
for j in range(1,7):
    if j%2==0:
        for i in range(1, 10):
            b = j*i
            print(j, "*", i, "=", b)
        print()


for i in range(2,7,2):
    for x in range(1,10):
        print(str(i)+"*"+str(x)+"="+str(i*x))
    print()


for i in range(2,7,2):
    for x in range(1,10):
        print( i,"*",x,"=",i*x, end="\n")
    print()

for x in range(1,10):
    for i in range(2,7,2):
        print( i,"*",x,"=",i*x, end="\t")
    print()
print()

for x in range(2,9,2):
    for i in range(2,7,2):
        print( i,"*",x,"=",i*x, end="\t")
    print()
print()

#가로로 만들기
for x in range(1,9):
    if x%2==0:
        for i in range(2,7,2):
            print( i,"*",x,"=",i*x, end="\t")
        print()
print()


#방법1 - 짝수 찾고, 8 걸러내서 찾기

for x in range(1,9):
    if (x%2==0) & (x!=8):
        for i in range(2,7,2):
            print( i,"*",x,"=",i*x, end="\t")
        print()
print()

for x in range(1,9):
    if x%2==0 and x!=8:
        for i in range(2,7,2):
            print( i,"*",x,"=",i*x, end="\t")
        print()
print()
    
#방법2 - 2,4,6쌩으로 찾기
for x in range(1,9):
    if x in [2,4,6]:
        for i in range(2,7,2):
            print( i,"*",x,"=",i*x, end="\t")
        print()







