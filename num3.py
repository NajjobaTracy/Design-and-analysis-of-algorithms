def flatten_list(lst):
    if lst == []:
       return lst
 #if the first element of the list passed to the function 
 # is an empty list, then the function should return the list
    elif isinstance(lst[0],list):
#the above line checks whether the first element of the list
#passed in is also a list
       return flatten_list(lst[0]) + flatten_list(lst[1:])
#if so, the lists are passed back to the flatten_list function
# to check whether there are other nested lists in it
       return lst[:1] + flatten_list(lst[1:])

S = ['a',['b',['c',['d']],'e'],'f']
flat = flatten_list(S)
print(flatten_list(S))

