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
        while arr[j] > pivot and j > left:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    if arr[i] > pivot:
        arr[i],arr[right] = arr[right],arr[i]
    return i

li = [1,45,24,67,36,68,5423,413,325]
quick_sort(li,0,len(li)-1)
print(li)
