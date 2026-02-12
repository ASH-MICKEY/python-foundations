<<<<<<< HEAD
def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year=int(input("Enter a year: "))
if leapyear(year):
    print(f"{year} is a leap year.")
else:
=======
def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year=int(input("Enter a year: "))
if leapyear(year):
    print(f"{year} is a leap year.")
else:
>>>>>>> c3c4bc532b86ef14ebaf740d3d6549be08bb4c39
    print(f"{year} is not a leap year.")