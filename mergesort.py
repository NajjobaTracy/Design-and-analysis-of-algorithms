def merge(a,b):
    sorted_arr=[]
    x=0
    y=0

    len_a=len(a)
    len_b=len(b)

    while x< len_a and y < len_b:
        if a[x] <= b[y]:
            sorted_arr.append(a[x])
            x+=1
        else:
         sorted_arr.append(b[y])
         y+=1
    while x < len_a:
            sorted_arr.append(a[x])
            x=+1

    
    while x < len_a:
            sorted_arr.append(b[y])
            y=+1
    

    return sorted_arr
A=[2,100,1000]
B=[1,699,1000000,1000001]

print(merge(A,B))

