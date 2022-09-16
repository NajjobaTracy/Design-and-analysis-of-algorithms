#QUESTION 1-Given the input sequence (31,41,59,26,41,58),using python write a sorting algorithm that searches for "55" and returns output true or false if the number appears.


#function that calls a binary search where the input array is a collection of the items and the search value indicates the value you are looking for.
def binary_search(input_array,search_value):
#beginning is a variable that helps initiate the index of the first input value of your list.
    beginning = 0
#end indicates the index of the last value in the list -we subtract one to achieve that .
    end = len(input_array) - 1
#the while loop helps insert conditions that prompts the program to return the value a user is searching for
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
test_list=[26,31,41,41,58,59] 
#diffrent serach values listed
search_value1= 55

#return bolean result.

#returns False to indicate that value does not exist in the input array
print(binary_search(test_list,search_value1))