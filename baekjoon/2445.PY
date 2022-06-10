n = int(input())

for num in range(1,n+1):
    print("*"*num+" " *(n-num)*2+"*"*num)
for k in range(1,n):
    print("*"*(n-k)+" "*(2*k)+"*"*(n-k))
