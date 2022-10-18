#declare your array
z=[5,2,4,6,1,3] 
print("array before using the insertion sort algorithm ")
print(z)

print("Array size")
x=1
print(len(z))

#x and y are in reference to the index positions
while x < len(z):
    c=z[x]

    y=x-1
    while y>=0 and z[y]>c:
        z[y+1]=z[y]
        y=y-1
    z[y+1]=c
   
    x=x+1

print("Array after using the insertion sort")  
print(z)


