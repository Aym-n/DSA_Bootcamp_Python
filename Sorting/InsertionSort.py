def InsertionSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[i]>=arr[j]:
                swap(arr,i,j)
                print(arr)

def swap(arr,first,last):
    temp = arr[first]
    arr[first]=arr[last]
    arr[last]=temp


arr = [5, 3, 4, 1, 2]
InsertionSort(arr)
print(arr)
