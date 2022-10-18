#INSERTION SORTING ASCENDING ORDER

z=[20,35,45,10,40,60] 

x=1 #AS THE STANDARD STARTING INDEX
print(z)

while x < len(z):#WHILE INDEX X IS LESS THAN 6 WHICH IS THE LENGTH OF THE ARRAY
    c=z[x] #C IS THE TEMPORARILY STORED STARTING INDEX AND c,x,y are all about indexes
    y=x-1 #INDEX Y IS THE INDEX ON THE DIRECT LEFT USED FOR COMPARISON
    while y >= 0 and z[y] > c: #WHILE INDEX Y IS >= INDEX 0 AND NUMBER AT INDEX Y IS LESS THAN INDEX C
        z[y+1] = z[y]

        y = y-1
    z[y+1] = c
    x = x + 1

print(z) 

#INSERTION SORT in descending order 
z=[20,35,45,10,40,60] #AS THE GIVEN ARRAY

x=1 # AS THE STARTING INDEX
print(z)

while x < len(z):#WHILE INDEX X IS LESS THAN 6 WHICH IS THE LENGTH OF THE ARRAY
    c=z[x] #C IS THE TEMPORARILY STORED STARTING INDEX 
#c,x,y are all about indexes
    y=x-1 #INDEX Y IS THE INDEX ON THE DIRECT LEFT USED FOR COMPARISON
    while y >= 0 and z[y] < c: #WHILE INDEX Y IS >= INDEX 0 AND NUMBER AT INDEX Y IS GREATER THAN INDEX C
        z[y+1] = z[y]

        y = y-1
    z[y+1] = c
    x = x + 1

print(z) 