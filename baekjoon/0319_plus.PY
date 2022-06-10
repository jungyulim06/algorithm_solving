n=int(input())

for num in range(n):
    print(' ' * (n-num)+'*'*(2*num-1))
for num in range(n):
    print(' ' * (num)+ '*'* (-2*num+(2*n-1)))


for num in range(n+1):
    print(' ' * (n-num)+'*'*(2*num-1))
for num in range(1,n):
    print(' ' * (num)+ '*'* (-2*num+(2*n-1)))



    7번
