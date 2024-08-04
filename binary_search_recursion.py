def binary(l,x,start,end):
    #Base Case Only Element In Array
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
        
    else:
        #Divide The Array Into Halves
        mid=int((start+end)/2)
        if l[mid]==x:
            return mid
        elif(l[mid]>x):
            #Left Half
            return binary(l,x,start,mid-1)
        else:
            #Right Half
            return binary(l,x,mid+1,end)
#Code Execution
l=[20,45,60,70,90]
print("[20,45,60,70,90]")
x=int(input("Enter Search Key="))
index=binary(l,x,0,len(l)-1)

if index==-1:
    print(x,"Not Found!!!")
else:
    print(x,"Is Found At Position",index+1)

