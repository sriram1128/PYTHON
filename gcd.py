def gcd(a,b):
    while b!=0:
        
        t = a
        a = b
        b= t%b
        
    return a


print(gcd(9,12))


