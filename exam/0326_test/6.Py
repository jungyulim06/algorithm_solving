n=int(input())

for num in range(n):
    print(' '*num + '*' * (-2*(num)+(2*n-1)))

n=int(input())

for num in range(n):
    print(' '*num + '*' * (2*(n-num)-1) )