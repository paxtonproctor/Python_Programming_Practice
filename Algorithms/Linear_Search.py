# Paxton Proctor
# 10/28/2021
# This program takes in a input of numbers and uses linear search
# to find a secific value that the user is looking for

# Definition function
# takes in arr, sizeof arr, number to find
def search(arr, n, x):

    # for iterates till end of array
    for i in range(0, n):
      # if array index is equal to number
      # return Index
      # else return -1
      if (arr[i] == x):
        return i
    return -1

# number of elements
n = int(input("Enter number of elements : "))
# Below line read inputs from user using map() function
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
# number to find
x = int(input("Enter the number you want to find: "))
# Function call
result = search(arr, n, x)
# if ele is not in array. else print index
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

# The time complexity of the above algorithm is O(n). 

# Linear search is rarely used practically because other
# search algorithms #such as the binary search algorithm 
# and hash tables allow significantly #faster-searching comparison to Linear search.

# Improve Linear Search Worst-Case Complexity

# if element Found at last  O(n) to O(1)
# It is the same as previous method because here we are performing 2
# ‘if’ #operations in one iteration of the loop and in previous method
# we #performed only 1 ‘if’ operation. This makes both the time complexities #same.
