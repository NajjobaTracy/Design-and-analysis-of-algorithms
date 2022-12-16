#BINARY SORT optimization looking for the number 4 in an unsorted array
aux_arr = []
 
# Function to make auxiliary array
def make_aux_array(arr, n):
    global aux_arr
 
    # For every element in array write
    # elements and their indices in
    # auxiliary array of pairs
    for i in range(n):
        aux_arr.append([arr[i], i])
         
    # sort auxiliary array
        aux_arr.sort()
 
# Function to perform binary search
def binarySearch(arr, n, x):
    global aux_arr
     
    # For given value x perform Binary Search on sorted auxiliary
    # array, let position be the index where element x  or the element
    # just greater than x is in auxiliary array
    position = n
    for i in range(n):
        if aux_arr[i][0] == x:
            position = i
             
            # return index of element in
            # original array arr
            # aux_array[position][1]
            return aux_arr[position][1]
    return -1
 
# print function
def printFunc(arr, n, x):
    global aux_arr
    make_aux_array(arr, n)
    result = binarySearch(arr, n, x)
 
    if result == -1:
        print(-1)
    else:
        print(result)
 
# Driver Code
arr = [4,1,2,3,5,0]
N = len(arr)
X = 4
 
# Function call
printFunc(arr, N, X)


#MERGE SORT optimization for when the array is already sorted so it doesnt divide
array = [15,1,67,2,80,90]

def mergeSort(arr):

    j = 0
    i = 1

    if len(arr)<= 1:
        return arr
    
    while i < len(arr):
        if(arr[i] < arr[i - 1]):
            j = 1
        i += 1

    if (not j) :
        return arr
    else :
        mid = len(arr)//2
    
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)

    print(len (arr))
    print(left)
    print(right)
    
    return merge(left,right)

def merge(a,b):
    sortedArray = []

    x=0
    y=0

    len_a = len(a)
    len_b = len(b)

    while x < len_a and y< len_b:
        if a[x] <= b[y]:
            sortedArray.append(a[x])
            x += 1
        else:
            sortedArray.append(b[y])
            y += 1
    while x < len_a:
        sortedArray.append(a[x])
        x += 1
    while y < len_b:
        sortedArray.append(b[y])
        y += 1

    return sortedArray
print(mergeSort(array))


#BUBBLE SORT optimization for when the array is alraedy sorted so that it doesnt divide
def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        current = array[j]
        array[j] = array[j+1]
        array[j+1] = current

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break

list = [4,5,3,2,8,0]

bubbleSort(list)

print('Sorted Array in Ascending Order:')
print(list)