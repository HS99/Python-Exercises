a,b=0,1
n=int(input("Enter N "))
print(a,b,end=' ')
for i in range(1,n):
    c=a+b
    a,b=b,c
    print(c,end=' ')

a=[0,1]
n=int(input("Enter N "))
print(a[0],a[1],end=' ')
for i in range(1,n):
    c=a[i-1]+a[i]
    a.append(c)
    print(a[i],end=' ')