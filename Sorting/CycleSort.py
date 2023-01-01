def CyclicSort(arr):
    i = 0;
    while i < len(arr):
        correct = arr[i] - 1
        if not arr[i] == arr[correct]:
            swap(arr, i, correct)
        else:
            i += 1

def swap(arr,first,last):
    temp = arr[first]
    arr[first]=arr[last]
    arr[last]=temp
#Find The Missing Number

arr = [5, 3, 4, 1, 2]
CyclicSort(arr)
print(arr)