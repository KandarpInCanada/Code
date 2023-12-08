def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

num = input("enter the number for finding factorial of it --> ")
print("factorial of {} is {}".format(num,factorial(int(num))))
    