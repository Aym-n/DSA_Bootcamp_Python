def CyclicSort(arr):
    i = 0
    while i < len(arr)-1:
        #correct  arr[i]-1 if array starts form 0
        correct = arr[i] 
        if not arr[i] == arr[correct] and arr[i] < len(arr):
            swap(arr, i, correct)
        else:
            i += 1

def swap(arr,first,last):
    temp = arr[first]
    arr[first]=arr[last]
    arr[last]=temp

#Find The Missing Number
def MissingNumber(arr):
    CyclicSort(arr) 
    for i in range(len(arr)):
        if( arr[i] != i):
            return i
        return len(arr)



arr = [5, 3, 4, 1]
print(MissingNumber(arr))