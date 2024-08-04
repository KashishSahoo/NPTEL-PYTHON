def fact(n):
    if(n==1):
        return(1)
    else:
        return(n*fact(n-1))
n=int(input("Enter A Number="))
r=fact(n)
print("The Factorial Of Number Is",r)

# f=5*f(4)
# f=5*4*f(3)
# f=5*4*3*f(2)
# f=5*4*3*2*f(1)
# f=5*4*3*2*1=120
        