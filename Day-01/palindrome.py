def palindrome(s):
    s=s.lower()
    if s==s[::-1]:
        return True
    else:
        return False
s=input("Enter a string: ")
if palindrome(s):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")