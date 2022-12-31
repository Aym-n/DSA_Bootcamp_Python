import math

#Simple Linear Search Algorithm
def linear_search(num,target):
    index = 0
    if not len(num) == 0:
        for item in num:
            if item == target:
                return index;
            index += 1
        return -1
    else:
        return -1

#Find Character in a string
def CharInStr(text,char):
    if not len(text) == 0:
        for a in text:
            if a == char:
                return True
        return False
    else:
        return False

#Search In Range
def SearchInRange(num,target,start,end):
    #Checking for invalid values of start end and nums list
    if not start == end and not len(num) == 0 and not start < 0 and not end < 0 and end > start:
        for a in range(start,end+1):
            if num[a] == target:
                return a
        return -1
    return -1

#Minimum Number
def minimum_number(num):
    minimun = num[0]
    for a in num:
        if a < minimun:
            minimun = a
    return minimun

#Maximum Number
def maximum_number(num):
    maximum = num[0]
    for a in num:
        if a > maximum:
            maximum = a
    return maximum
#Search In 2D Arrays
def SearchIn2DArray(num,target):
    for i in range(len(num)):
        for j in range(len(num[i])):
            if num[i][j] == target:
                return [i,j]
    return [-1 , -1]

#Leetcode Problem
#Find Number of elements in array containing even no of digits
#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

def digits(num):
    count = 0;
    while num > 0:
        num = int(num/10)
        count += 1
    return count

def OptimisedDigits(num):
    return int(math.log10(num)+1)

def NumbersWithEvenDigits(arr):
    count = 0
    for a in arr:
        if OptimisedDigits(int(a))%2 == 0:
            count+= 1
    return count

#Leetcode problem 2 
#Max Wealth
# https://leetcode.com/problems/richest-customer-wealth/

def maximumWealth(self, accounts: List[List[int]]) -> int:
    wealth = 0
    maxWealth  = 0
    for person in accounts:
        for money in person:
            wealth += money 
        if maxWealth < wealth:
            maxWealth = wealth
    return maxWealth

#index  0   1   2   3   4   5
nums = [1 , 2 , 3 , 4, 5 , 6]
targets =  2
twodArray  = [
    [2 , 3],
    [4 , 5]
]

text = "STRING"
char = "F"

#print(SearchIn2DArray(twodArray,targets))

#print(linear_search(nums,targets))

#print(SearchInRange(nums,targets,1,4))

#print(maximum_number(nums))
#print(minimum_number(nums))

#print(CharInStr(text,char))

#print(NumbersWithEvenDigits(nums))


