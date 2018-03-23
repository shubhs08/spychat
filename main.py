##################FIRST PART:###########################
print("SPYCHAT")
print("Welcome to SPYCHAT")
spy_name=input('What/s your name')
print(spy_name)
print("Welcome " + spy_name + " How are you?")
type(spy_name)
spy_salutation=input("What should we call you(Mr./Miss.)")
print(spy_salutation)
print(spy_salutation +" " + spy_name)
print("Alright "+ spy_salutation +" " + spy_name + " I would like to know a little bit more about you")
spy_account=input("Tell which account would you prefer to choose(default/new)")
if(spy_account=="new"):
    spy_name = input("Whats your name")
    print(spy_name)
    print("Welcome " + spy_name + " How are you?")
    type(spy_name)
    spy_salutation = input("What should we call you(Mr./Miss.)")
    print(spy_salutation)
    print(spy_salutation + " " + spy_name)
    print("Alright " + spy_salutation + " " + spy_name + " I would like to know a little bit more about you")
else:
    exit(0)
##########################SECOND PART:##############################
#######fetching the name of a spy#######
spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")

if len(spy_name) > 0: ####checking the legth of name entered by spy####
    print('Welcome ' + spy_name + '. Glad to have you back with us.')
    spy_salutation = input("Should I call you Mister or Miss?: ")#asking for salutation#
    spy_name = spy_salutation + " " + spy_name
    print(spy_name)
    print("Alright " + spy_salutation + " " + spy_name + ". I'd like to know a little bit more about you before we proceed...")
else:
 print("A spy needs to have a valid name. Try again please.")#if if condition gets false else works#
 #####initialising variables#####
spy_age = 0
spy_rating = 0.0
spy_is_online = False
spy_age = int(input("What is your age?"))#asking the spy age#
if spy_age > 16 and spy_age < 55:
    spy_rating = float(input("What is your spy rating?"))
else:
    print('Sorry you are not of the correct age to be a spy')
if spy_rating > 4.5:#checking the rating values
        print('Great ace!')
elif spy_rating > 3.5 and spy_rating <= 4.5:
        print('You are one of the good ones.')
elif spy_rating >= 2.5 and spy_rating <= 3.5:
        print('You can always do better')
else:
        print('We can always use somebody to help in the office.')
spy_is_online = True
print("Authentication complete. Welcome " , spy_name) #priniting the final details
print(" age: " , spy_age)
print("rating of: " , spy_rating )
print(" Proud to have you onboard")











