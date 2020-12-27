import sys


student = {"name":"Emre","surname":"Uslu"}
courses = ["1)Python","2)Embedded","3)AI","4)ML","5)DL"]

selected_courses = []
selected_courses_new = []
grades = {"midterm" : 0 ,"final" : 0, "project": 0}
error = 3
right = 0
login = False
chck = 0



while error > 0:
    name = input("Your name:")
    surname = input("Your surname:")
    if name == student["name"] and surname == student["surname"]:
        login = True
        break
    else:
        print("Login Failed!" ,error-1, "attemp remained.")
        error -= 1
    if error == 0:
        print("Try again later!")   


def calculate_grade(selected_4grade):

    grades["midterm"] = int(input("Your midterm: "))
    grades["final"] = int(input("Your final: "))
    grades["project"] = int(input("Your project: "))

    print(f"Your {selected_4grade} course grades list : ",grades)

    your_grade = grades["midterm"] * 0.30 + grades["final"]*0.50 + grades["project"]*0.20

    if your_grade >= 90:
        print("Your final grade: AA")
    elif your_grade >= 70 and your_grade < 90:
        print("Your final grade: BB")
    elif your_grade >= 50 and your_grade < 70:
        print("Your final grade: CC")
    elif your_grade >= 30 and your_grade < 50:
        print("Your final grade: DD")
    else:
        print("Your grade: FF\n**** YOU FAILED! ****") 


if login:
    print(f"Welcome {name} {surname}!")
    for i in courses:
        print(i)
    while right < 5:
        selected_course = input("Please choose at least 3 of them!\nPress q for exit!\n")
        if selected_course == "q":
            break
        elif int(selected_course) >= 1 and int(selected_course) <=5:
            if courses[int(selected_course) - 1] not in selected_courses:
                selected_courses.append(courses[int(selected_course) - 1])
                right += 1
            else:
                print("You can't choose a course 2 times. Choose another course")
        else:
            print("Selection Failed! Choose number of course!")
    if right < 3:
        print("*** YOU FAILED CLASS! ***")
        sys.exit()
    
    
    print("Chosen courses:")
    for i in range(len(selected_courses)):
        print(selected_courses[i][2:])
        selected_courses_new.append(selected_courses[i][2:])
 
    

    while chck < 10:
        selected_4grade = input("Please enter your course name that you want to calculate your grade:\n")
        if selected_4grade in selected_courses_new:            
            calculate_grade(selected_4grade)
            
        else:
            print("Please choose course from your chosen courses")
            chck += 1
    
        
    

    

