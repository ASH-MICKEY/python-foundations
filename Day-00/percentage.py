def calculatepercentage(sum,tot):
    percentage=(sum/tot)*100
    return percentage
def grade(percentage):
    if percentage>=90:
        return "A"
    elif percentage>=80:
        return "B"
    elif percentage>=70:
        return "C"
    elif percentage>=60:
        return "D"
    elif percentage>=50:
        return "E"
    else:
        return "F"
outof=int(input("Enter the outoff marks of each subject: "))
tot=outof*5
s1=int(input("Enter the 1st subject marks: "))
s2=int(input("Enter the 2nd subject marks: "))
s3=int(input("Enter the 3rd subject marks: "))
s4=int(input("Enter the 4th subject marks: "))
s5=int(input("Enter the 5th subject marks: "))
sum=s1+s2+s3+s4+s5
percentage=calculatepercentage(sum,tot)
print(f"Your total percentage is: {percentage}%")
print(f"Your grade is: {grade(percentage)}")
print("1st subject grade is: ",grade(calculatepercentage(s1,outof)))
print("2nd subject grade is: ",grade(calculatepercentage(s2,outof)))
print("3rd subject grade is: ",grade(calculatepercentage(s3,outof)))
print("4th subject grade is: ",grade(calculatepercentage(s4,outof)))
print("5th subject grade is: ",grade(calculatepercentage(s5,outof)))