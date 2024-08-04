def spiral(m,n,a):

    k=0
    l=0
    

#m=No.Of Rows
#n=No.Of Columns
#k=Starting Index Of Row(0)
#l=Starting Index Of Column(0)
    
    while(k<m and l<n):
        #Printing The First Row From Remaining Rows
        for i in range(l,n):
            print(a[k][i],end=" ")
        
        k+=1
        #Printing Last Column Values From Remaining Columns
        for i in range(k,m):
            print(a[i][n-1],end=" ")
        
        n-=1
  
        if(k<m):
            #Printing The Last Row From Reamining Rows
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end=" ")

            m-=1

            if(l<n):
                #Pring The First Column From Remaining Columns
                for i in range(m-1,k-1,-1):
                    print(a[i][l],end=" ")
                l+=1

a=[]
c=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(c)
        c+=1
    a.append(l)

print(a)
spiral(4,4,a)



        


