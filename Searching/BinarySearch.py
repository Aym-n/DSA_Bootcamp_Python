def binarySearch(arr,target):
    start = 0;
    end = len(arr)-1
    while(start <= end):
        mid = int(start + (end - start)/2)
        if target < arr[mid]:
            end = mid - 1
        elif(target > arr[mid]):
            start = mid + 1
        else:
            return mid
    return -1
def OrderAgnosticBS(arr,target):
    
arr = [2, 3, 4, 16, 18, 21, 25, 40]
print(binarySearch(arr,40))
