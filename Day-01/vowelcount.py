def vowelcount(s):
    count=0
    v='aeiouAEIOU'
    for i in s:
        if i in v:
            count+=1
    return count
s=input("Enter a string: ")
print(f"The number of vowels in the string is: {vowelcount(s)}")