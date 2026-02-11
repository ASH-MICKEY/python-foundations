import random
ln=random.randint(1,10)
print(f"Your lucky number is {ln}")
rg=random.randint(1,999999)
print(f"The random guess number is {rg}")
def add(n):
    while n>9:
        s=0
        while n>0:
            s+=n%10
            n=n//10
        n=s
    return n
sum_add=add(rg)
print(f"The sum value for the random number is: {sum_add}")
if sum_add==ln:
    print(f"Is your lucky number {sum_add}? Yes, you are lucky!")
else:
    print(f"It is not your lucky number")