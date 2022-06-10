n = int(input())

for num in range(1, n+1):
    print("*" * num +" " * (num*-2+2*n) +"*" * num )

for a in range(n):
    print("*" *(n-a-1)+ " " * (a*2+2) +"*" *(n-a-1))
