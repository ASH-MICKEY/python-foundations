def armstrong(n):
    nd=len(str(n))
    m=n 
    s=0
    while n>0:
        r=n%10
        s=s+(r**nd)
        n=n//10
        if m==s:
            print(f"{m} is an armstrong number")
            break
    else:
        print(f"{m} is not an armstrong number")
n=int(input("Enter the number: "))
armstrong(n)