def reverse_no(n):
    m=0
    while n>0:
        r=n%10
        m=m*10+r
        n=n//10
    return m
n=int(input("Enter a number: "))
print(f"The reverse of the number is: {reverse_no(n)}")