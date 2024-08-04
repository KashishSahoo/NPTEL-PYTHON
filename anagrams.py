# x=[4,3,6,22,1]
# print(sorted(x))
# print(sorted(x,reverse=True))

# x=['h','k','l','a','j','m','u']
# print(sorted(x))

# a='python'
# print(sorted(a))

# b={'q':1,'w':2,'e':4,'t':0}
# print(sorted(b))

# l=['cccc','dd','a','hhhhhh']
# print(sorted(l,key=len))

s1=input("Enter 1st String=")
s2=input("Enter 2nd String=")
print(sorted(s1))
print(sorted(s2))

if(sorted(s1)==sorted(s2)):
    print("The Two String Are Annagrams")
else:
    print("The Two String Are  Not Annagrams")
