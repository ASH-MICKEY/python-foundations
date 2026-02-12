def prime_in_givenrange(n):
    p = []
    for i in range(2, n + 1):
        for j in range(2, (i//2) + 1):
            if i % j == 0:
                break
        else:
            p.append(i)
    return p
n = int(input("Enter a number: "))
print(f"Prime numbers from 1 to {n} are: {prime_in_givenrange(n)}")