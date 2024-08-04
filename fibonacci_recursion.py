'''
0 fib=0{Base Case}
1st fib=1
---------
2nd fib=1{Derived Case}
3rd fib=2
4th fib=3
5th fib=5
'''
#To Find nthh Fibonacci Number
#0,1,1,2,3,5,8,13...
def fibo(n):
    if(n==0):
        return(0)
    elif(n==1):
        return(1)
    else:
        return(fibo(n-1)+fibo(n-2))
n=int(input("Enter A Number="))

if n<0:
    print("Fibonacci Numbers Are Not Defined Number")
else:
    print(f"{n}th Fibonacci Number Is",fibo(n))
