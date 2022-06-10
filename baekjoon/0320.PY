n=int(input())

for num in range(1,n+1):
    print('*'*num+ ' ' * (-2*num+2*n)+'*'*num)
for num in range(1,n):
    print('*'*(n-num)+' '*(2*num)+'*'*(n-num))