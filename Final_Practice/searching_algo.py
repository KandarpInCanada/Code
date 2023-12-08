def binary_search(arr,search_value):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid_point = (left+right)//2
        mid_value = arr[mid_point]
        if search_value == mid_value:
            print("found at position")
            return
        else:
            if search_value < mid_value:
                right = mid_point - 1
            else:
                left = mid_point + 1
    print("not found")

lis = [12,4,357,587,3125,66,7568,65]
lis.sort()
binary_search(lis,58744)