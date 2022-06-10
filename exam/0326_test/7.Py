n=int(input())

for num in range(1,1+n):
    print(' '*(n-num)+'*'*(2*num-1))


for num in range(n):
    print(' '*(num+1) + '*' * (2*(n-num)-3) )
  


    