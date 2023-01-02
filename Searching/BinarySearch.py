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
    start = 0;
    end = len(arr)-1
    while(start <= end):
        mid = int(start + (end - start)/2)
        if arr[mid] == target:
            return mid

        if(arr[0]>arr[-1]):
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1


arr = [2, 3, 4, 16, 18, 21, 25, 40]
print(OrderAgnosticBS(arr[::-1],40))
