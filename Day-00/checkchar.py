def check_char(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        return "Vowel"
    elif char not in vowels and char.isalpha():
        return "Consonant"
    elif char.isdigit():
        return "Digit"
    else:
        return "special character"
char = input("Enter a character: ")
result = check_char(char)
print(f"The character '{char}' is a {result}.")
