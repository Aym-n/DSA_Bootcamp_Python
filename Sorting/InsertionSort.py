def InsertionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j-1]>arr[j]:
                swap(arr,j-1,j)
            else:
                break

def swap(arr,first,last):
    temp = arr[first]
    arr[first]=arr[last]
    arr[last]=temp


arr = [5, 3, 4, 1, 2]
InsertionSort(arr)
print(arr)
