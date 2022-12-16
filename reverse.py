#  a Recursive python program to reverse an array
 
# Function  used to reverse list[] from start to end
def reverseList(list, start, end):
    if start >= end:
        return
    list[start], list[end] = list[end], list[start]
    reverseList(list, start+1, end-1)
 

list = [2,6,9,10]
print(list)
reverseList(list, 0, 3)
print("Reversed list is")
print(list)