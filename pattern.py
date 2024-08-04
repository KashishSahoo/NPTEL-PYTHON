import turtle
from random import randint

turtle.bgcolor("black")
seurat=turtle.Turtle()

width=5
height=7

dot_distance=25

seurat.penup()
list_color=["yellow","white","brown","green","red","orange","blue","pink","violet","grey","light green"]

seurat.setpos(-250,250)

def spiral(m,n):

    seurat.color("white")
    k=0
    l=0
    f=0

#m=No.Of Rows
#n=No.Of Columns
#k=Starting Index Of Row(0)
#l=Starting Index Of Column(0)
    
    col=randint(0,10)
    seurat.color(list_color[col])
    
    while(k<m and l<n):

        if f==1:
            seurat.right(90)
        #Printing The First Row From Remaining Rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[k][i],end=" ")
        
        k+=1
        f=1

        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        #Printing Last Column Values From Remaining Columns
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[i][n-1],end=" ")
        
        n-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
  
        if(k<m):
            #Printing The Last Row From Reamining Rows
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                # print(a[m-1][i],end=" ")

            m-=1
            seurat.right(90)
            col=randint(0,10)
            seurat.color(list_color[col])

            if(l<n):
                #Pring The First Column From Remaining Columns
                for i in range(m-1,k-1,-1):
                    seurat.dot()
                    # print(a[i][l],end=" ")
                    seurat.forward(dot_distance)
                l+=1

# a=[]
# c=1
# for i in range(4):
#     l=[]
#     for j in range(4):
#         l.append(c)
#         c+=1
#     a.append(l)

# print(a)
spiral(20,20)
turtle.done()