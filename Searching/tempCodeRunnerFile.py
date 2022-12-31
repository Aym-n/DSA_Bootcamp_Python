def linear_search(num,target):
    index = 0
    for item in num:
        if item == target:
            return index;
        index += 1


nums = [1, 34, 88, 74, 3, 90, 22]
target =  90
print(linear_search(nums,target))



