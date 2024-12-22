

def armstrongNo(n):

    t = n
    c = 0
    s = 0
    while t != 0:
        t = t // 10
        c += 1
    
    temp = n
    while temp != 0:
        r = temp % 10
        s = s + pow(r,c)
        temp = temp // 10
    if s == n:
        return 'Armstong '
    else:
        return 'Not Armstrong'



print(armstrongNo(370))

    
