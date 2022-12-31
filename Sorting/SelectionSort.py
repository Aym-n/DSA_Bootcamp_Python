def SelectionSort(nums):
    for i in range(len(nums)):
        last = len(nums)-i-1
        swap(nums,int(getMaxIndex(nums,0,last)),last)

#swapping position of elements
def swap(arr,first,last):
    temp = arr[first]
    arr[first]=arr[last]
    arr[last]=temp

#get index of maximum number in the remaining array
def getMaxIndex(arr,first,last):
    max = arr[0]
    maxIndex = 0
    for i in range(first,last+1):
        if max < arr[i]:
            max = arr[i]
            maxIndex = i
    return maxIndex
        


arr=[3,1,5,2,4]
SelectionSort(arr)
print(arr)