#implementing a linear search

def linear_Search(list,target):

    for i in range (0,len(list)):
        if list[i]==target: #change list([i]) to list[i], otherwise the rest is okay 
            print([i])
       

            return i# why are you having both return and print separate?? in an editor like jupyter notebooks, a return would print, but in vs code you can have it as below
            
    return -1
def linearsearch2(z,value):
    z=[]
    for i in range (0,len(z)):
        if list[i]==value:
         z.append(list[i])
        return -1   
    return z        
               
                
list=[11,423,172,30,910,9,2,45,172]
#linear_Search(list,172)
linearsearch2(list,172)