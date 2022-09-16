# Python program to implement insertion sort 
# QUESTION-GIVEN THE INPUT SEQUENCE (31,41,59,26,41,58),USING PYTHON WRITE A SORTING ALGORITHM THAT RETURNS AN OUTPUT (26,31,41,41,58,59)

# function to do an insertion sort 

def insertion_sort(list):
    #Transverse through 1 to len(arr)
    for index in range (1,len(list)):
        value = list[index]
        i = index - 1
#Move elements of arr[0...i-1],that are greater than key,to one position ahead of their current position        
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i] 
                list[i] = value
                i -=1
            else:
                break

#testing code
list=[31,41,59,26,41,58]
insertion_sort(list)
#Print new sorted list 
print(list)