def Fibo(n):
    return n if n < 2 else Fibo(n-1) + Fibo(n-2)

def BSrecursion(arr,target,start,end):
    middle = int(start + (end-start)/2)

    if start > end : return -1

    if arr[middle] == target: return middle

    if target < arr[middle]: return BSrecursion(arr, target, start, middle-1)

    else: BSrecursion(arr, target, middle+1, end)
     
#for i in range(10):
#    print(Fibo(i))

arr = [1, 2, 3, 4, 55, 66, 78]
target = 1
print(BSrecursion(arr,target,0,len(arr)))

