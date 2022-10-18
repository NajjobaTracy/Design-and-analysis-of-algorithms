#implementation of a bubble sort 
def bubble_sort(array):
    n=len(array)
    
    for i in range(n-1):
        sort_status = True
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                sort_status= False
        if sort_status:
              break
        
    return array

input_array = [6,4,9,1,3]
bubble_sort(input_array)
