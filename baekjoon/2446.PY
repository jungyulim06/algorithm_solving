n = int(input())

for num in range(1, n):
    print (" " * (num-1) + "*" * (2 * (n - num) + 1))
for num in range(1,n+1):
    print(' ' * (n-num) + '*'*(2*num-1))

