def quick_sort(arr,left,right):
    if left < right:
        position = partition(arr,left,right)
        quick_sort(arr,left,position-1)
        quick_sort(arr,position+1,right)

def partition(arr,left,right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while arr[i] < pivot and i < right:
            i += 1
        while arr[j] >= pivot and j > left:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    if arr[i] > pivot:
        arr[i],arr[right] = arr[right],arr[i]
    return i

num_list = [2,435,654,124,34246,566,5562]
quick_sort(num_list,0,len(num_list)-1)
print(num_list)