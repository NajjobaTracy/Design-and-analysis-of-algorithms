#binary searches 
#funtion that calls a binary search where the input array is a collection of the items and the search value indicates the value youre looking for
def binary_search(input_array,search_value):
#beginning is avariable that helps initiate the index of the first input value of your list.
    beginning = 0
#end indicates the index of the last value in the list-we subtract one to achieve that .
    end = len(input_array) - 1
#the while loop helps insert conditions that prompt the program to return the value one is searching for
    while beginning <= end:
#since the binary serach uses the divide and conquer mechanism we find the middle value using the formula below
        middle = int((beginning + end)/2)
#if the value we are looking is equal to the middle value of the input array return true if you decide to use bolean or for a different case you can return that middle value
        if search_value == input_array[middle]:
            return True
#however if the number is less than the middle value of the input array proceed and return true since the number exists in that array
        elif search_value < input_array[middle]:
            end=middle - 1
#else-if the number is greater than the middle value of the input array proceed and return true if the number exists in that array  
        else:
            beginning = middle + 1  
#if the search value does not exist in the array then return false 
    return False 

#testing the code
#input_array referred to as test_list
test_list=[1,2,3,4,5,6,9,11] 
#diffrent serach values listed
search_value1= 3
search_value2 = 9
search_value3 = 15 
#return bolean results.
print(binary_search(test_list,search_value1))
print(binary_search(test_list,search_value2))
print(binary_search(test_list,search_value3))
         