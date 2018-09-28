def main():
    #grades=[86.6,86.6,86.6,86.6,86.6]
    grades=[float(input("What are you getting in first period?")), float(input("Second period?")), float(input("Third?")), float(input("Fourth period?")), float(input("Fifth?"))]
    total=AverageGrade(grades)
    print(total)
    response=Class(int(input("What year are you in? ")))
    print(response)

def AverageGrade(grades):
    average= float((grades[0]+grades[1]+grades[2]+grades[3]+grades[4])/len(grades))
    if average>=90:
        lettergrade=(". You're getting an A.")
        z=1
    elif average>=80:
        lettergrade=(". You're getting a B.")
        z=1
    elif average>=70:
        lettergrade=(". You're getting a C.")
        z=1
    elif average>=60:
        lettergrade=(". You're getting a D.")
        z=2
    elif average<60:
        lettergrade=(". You're getting an F.")
        z=2
    if z==1:
        passing=(" You're passing.")
    if z==2:
        passing(" You're failing.")
    total="Your average grade is "+str(average)+str(lettergrade)+str(passing)
    return total

def Class(schoolyear):
    if schoolyear == 9:
        response = "You're a freshman"
    if schoolyear == 10:
        response ="You're a sophomore"
    if schoolyear == 11:
        response="You're a Junior"
    if schoolyear == 12:
        response="You're a Senior"
    else:
        response="You're not in highschool"
    return response

main()
