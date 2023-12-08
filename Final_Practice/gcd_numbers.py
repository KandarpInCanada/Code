def get_gcd(a,b):
    while b:
        a,b = b,a%b
    return a

num = [18,16,14]
g = get_gcd(num[0],num[1])
for i in range(2,len(num)):
    g = get_gcd(g,i)
print(get_gcd(18,16))