

def fibo (n):
    a =0
    b =1
    for i in range (1, n+1):
        print(a)
        c= a + b
        a = b
        b = c

print(fibo(10))
