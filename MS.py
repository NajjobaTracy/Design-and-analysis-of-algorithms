# Merge Sort - works like binary search - split problem into sub problems 
# 1 start with unsorted list 
# 2 split the list into 2 sub lists
# 3 keep spliting evenly until 1 element lists are attained 
# 4 work backwards 
# 5 repeatedly merge single element lists and sort them 

# naively sorting - passing a 1 element list to a merge sort 


def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    Divide: find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublist created in the previous step
    Combine: Merge the sorted sublists created in the previous step
    Takes O(kn log n) time
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)



def split(list):
    """
    Divides the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes overall O(k log n) time
    """

    mid = len(list) // 2

    left = list[:mid] 
    right = list[mid:]

# Python3 code for the above approach
 
# function perform selection sorting on the array
def selectionSort(arr):
    n = len(arr)
 
    # One by one move boundary of
    # unsorted subarray
    for i in range(n - 1):
 
        # Find the minimum element
        # in unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if (isAlphabeticallySmaller(arr[j], arr[min_idx])):
                min_idx = j
 
        # Swap the found minimum
        # element with the first element
        temp = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = temp
    return arr
 
# Function to compare 2 words
 
 
def isAlphabeticallySmaller(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    if str1 < str2:
        return True
    return False
 
 
# Driver code
Arr = ["Solomon","Daphine", "Charles", "Tracu", "Jasper","Destiny","Nabil"]
N = len(Arr)
 
# function call
Arr = selectionSort(Arr)
for word in Arr:
    print(word)