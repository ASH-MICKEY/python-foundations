def sum(n):
    s=0
    while n>0:
        s+=n%10
        n=n//10
    return s
def product(n):
    p=1
    while n>0:
        p*=n%10
        n=n//10
    return p
n=int(input("Enter the number: "))
s=sum(n)  
p=product(n)
if s==p:
    print("Given number is a spy number")
else:    
    print("Given number is not a spy number")  