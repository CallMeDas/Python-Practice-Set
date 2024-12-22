
def leapYear(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return 'Leap Year'
    else :
        return 'Not Leap Year'
    

print(leapYear(2000))