<<<<<<< HEAD
def binary(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        b=""
        while n>0:
            b=str(n%2)+ b
            n=n//2
        return b
n=int(input("Enter a number: "))   
=======
def binary(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        b=""
        while n>0:
            b=str(n%2)+ b
            n=n//2
        return b
n=int(input("Enter a number: "))   
>>>>>>> c3c4bc532b86ef14ebaf740d3d6549be08bb4c39
print(f"The binary representation of {n} is: {binary(n)}")