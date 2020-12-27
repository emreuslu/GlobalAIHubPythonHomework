""" ***User Identify Program***
The user will be defined. Get the data of this user by input method. Obtain information from user as follow:
    * First name
    * Last name
    * Age
    * Date of birth (just year)
Pass the user's information to the list and displays the screen using the for loop. Print all user information on the screen.
If he is under 18, print "You can't go out because it's too dangerous" on the screen.
If he is over 18, print "You can go out to the street." on the screen.
"""
information = []
first_name = input("What is your first name?\n")
information.append(first_name)
last_name = input("What is your last name?\n")
information.append(last_name)
age = int(input("What is your age?\n"))
information.append(age)
date_of_birth = int(input("What is your birth year?\n"))
information.append(date_of_birth)

for i in information:
    print(i)
    
if 0 < age < 18:
    print("You can't go out because it's too dangerous")
elif age > 18:
    print("You can go out to the street.")
else:
    print("Invalid input! Please enter your age correctly")