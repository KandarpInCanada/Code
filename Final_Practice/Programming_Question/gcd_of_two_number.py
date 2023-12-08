def get_gcd(a,b):
    while b:
        a,b = b,a%b
    return a

list_number = [48, 18, 24, 36]
result = list_number[0]
for i in list_number[1:]:
    result = get_gcd(result,i)
print(result)
