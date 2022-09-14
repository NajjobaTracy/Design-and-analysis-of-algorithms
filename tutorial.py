#binary searches 
def binary_search(input_array,search_value):
    beginning = 0
    end = len(input_array) - 1
    while beginning <= end:
        middle = int((beginning + end)/2)
        if search_value == input_array[middle]:
            return True
        elif search_value < input_array[middle]:
            end=middle - 1
        else:
            beginning = middle + 1  
    return False 

test_list=[1,2,3,4,5,6,9,11] 
search_value1= 3
search_value2 = 9
search_value3 = 15 

print(binary_search(test_list,search_value1))
print(binary_search(test_list,search_value2))
print(binary_search(test_list,search_value3))
         