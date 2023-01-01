#Find The Missing Number
def MissingNumber(arr):
    CyclicSort(arr) 
    for i in range(len(arr)):
        if( arr[i] != i):
            return i
    return len(arr)

#Numbers Dissappeared in an array
def DissappearedNumbers(arr):
    CyclicSort(arr)
    ans = []
    for i in range(len(arr)):
        if(arr[i] != i):
            ans.append(i)
    return ans

def CyclicSort(arr):
    i = 0
    while i < len(arr):
        #correct  arr[i]-1 if array starts form 0
        correct = arr[i] 
        if arr[i] < len(arr) and not arr[i] == arr[correct]:
            swap(arr, i, correct)
        else:
            i += 1
        return arr

def swap(arr,first,last):
    temp = arr[first]
    arr[first]=arr[last]
    arr[last]=temp


arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(CyclicSort(arr))
print(MissingNumber(arr))
print(DissappearedNumbers(arr))