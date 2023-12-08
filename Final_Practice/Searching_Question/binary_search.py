def binary_search(arr,search_value):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid_point = (left+right)//2
        mid_value = arr[mid_point]
        if search_value == mid_value:
            print("found a position {}".format(mid_point))
            return
        else:
            if search_value < mid_value:
                right = mid_point - 1
            else:
                left = mid_point + 1
    print("not found")

li = ['kandarp','patel','sureshbhai','kakaka','kdfhfdf','fdfdf']
li.sort()
binary_search(li,'kandarp')