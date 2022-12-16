#THIS IS CODE ON HOW TO CALCULATE THE MAXIMUM AND MINIMUM SUM AFTER SORTING THE ARRAY
#IT USES A TIME COMPLEXITY OF O(NLOG N)
def minMax(arr):
     
    # Initialize the min_value
    # and max_value to 0
    min_value = 0
    max_value = 0
    n=len(arr)
     
    # Sort array before calculating
    # min and max value
    arr.sort()
    j=n-1
    for i in range(n-1):
         
        # All elements except
        # rightmost will be added
        min_value += arr[i]
         
        # All elements except
        # leftmost will be added
        max_value += arr[j]
        j-=1
     
    # Output: min_value and max_value
    print(min_value,max_value)
 
#  Driver Code
arr=[4,3,1,6,7]
minMax(arr)


#THIS METHOD CALCULATES THE MAXIMUM AND MINIMUM SUM BY ADDING THEN SUBTRACTING THE LARGEST AND THE SMALLEST NUMBER
# IT USES A TIME COMPLEXITY OF O(N)
# Function to calculate minimum and maximum sum
def miniMaxSum(arr, n):

    # Initialize the minElement, maxElement
    # and sum by 0.
    minElement = 0
    maxElement = 0
    sum = 0

    # Assigning maxElement, minElement
    # and sum as the first list element
    minElement = arr[0]
    maxElement = minElement
    sum = minElement

    # Traverse the entire list
    for i in range(1, n):

        # Calculate the sum of list elements
        sum += arr[i]

        # Keep updating the minimum element
        if (arr[i] < minElement):
            minElement = arr[i]

        # Keep updating the maximum element
        if (arr[i] > maxElement):
            maxElement = arr[i]

    # Print the minimum and maximum sum
    print(sum - maxElement,
        sum - minElement)

# Driver Code

# Test Case 1:
a1 = [ 4,3,1,6,7 ]
n = len(a1)

# Call miniMaxSum()
miniMaxSum(a1, n)


#FINDS THE MAXIMUM AND MINIMUM SUM OF THE ELEMENTS IN THE ARRAY BY POPPING THE LARGEST AND SMALLEST VALUES AFTER SORTING
#IT USES A TIME COMPLEXITY OF O(N LOG N)
def merge_sort(array):
    if len(array)>1:
        mid=len(array)//2
        L=array[:mid]
        R=array[mid:]
        merge_sort(L)
        merge_sort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            array[k]=R[j]
            j+=1
            k+=1
def printlist(array):
    for i in range(len(array)):
        print(array[i],end="  ")
    print()
#SORTS THE ARRAY    
if __name__=='__main__':
    array=[4,3,1,6,7]
    merge_sort(array)
#FINDS THE SUM OF THE ARRAY FROM INDEX 0 TO THE INDEX RIGHT BEFORE THE END OF THE LIST
sum1=0
array1=array[:4]
for i in array1:
    sum1=sum1+i
#FINDS THE SUM OF THE ARRAY FROM THE SECOND ELEMENT TO THE END    
array2=array[1:]
sum2=0
for i in array2:
    sum2=sum2+i
print(sum1,sum2)