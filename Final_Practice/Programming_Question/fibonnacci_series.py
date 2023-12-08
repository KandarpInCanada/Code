def fibonacci(num):
    series_list = [0,1]
    for i in range(2,num+1):
        series_list.append(series_list[i-1] + series_list[i-2])
    print(series_list)
num = input("enter the number --> ")
fibonacci(int(num))