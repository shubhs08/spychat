print("Hello world")
print ('what\'s up?')
print ('Let\'s get started...')

#####asking name#####
def entry():
    spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy_name) > 0:
        print ('Welcome ' + spy_name + '. Glad to have you back with us.')

   #####providing salutation######
        spy_salutation = input("What should we call you (Mr. or Ms.)?")
        spy_salutation + " " + spy_name
        spy_name = spy_salutation + " " + spy_name
        print(spy_name)
        print( "Alright " + " " + spy_name +". I'd like to know a little bit more about you before we proceed...")
    else:
        print ("A spy needs to have a valid name. Try again please.")

#####further details#####
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False
#####asking age#####
    spy_age = input("What is your age?")
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(input("What is your spy rating?"))
    else:
        print( 'Sorry you are not of the correct age to be a spy')
    if spy_rating > 4.5:
        print( 'Great ace!')
    elif spy_rating > 3.5 and spy_rating <= 4.5:
        print ('You are one of the good ones.')
    elif spy_rating >= 2.5 and spy_rating <= 3.5:
        print ('You can always do better')
    else:
        print ('We can always use somebody to help in the office.')
    spy_is_online = True
    print ('Authentication complete. Welcome ', spy_name)
    print( 'Your age =' , spy_age)
    print ('Your spy rating=',spy_rating)

#################################

def spy_chat(new):
    i=0
    while i<5:
        print ("What do you want to do?")
        menu_choices="1. Add a status update \n2. Exit the application \nInput:-"
        menu_choice=raw_input(menu_choices)
        if menu_choice=="1":
            if new==0:
                from spy_details import status
                print ("Your current status is: %s" % status)  ####Display your current status####
            elif new==2:
                print ("Your status is: %s" % status)  ####Display status of new user
            else:
                print ("Add your status:")  ####ask for a new status
                status=input()
                print ("Your status is- %s" % status)
                new =2
            i=i+1

        elif menu_choice=="2":
            print ("Quitting...")   ####quits the program
            exit()
        else:
            i=i+1
            pass
user=input("Do you want to continue with the default user ?(Y/N)")
new_user=0
if user=="Y":
    from spy_details import name
    from spy_details import spy_salutation
    from spy_details import spy_age
    from spy_details import spy_rating
    print ("Welcome, %s %s with %d years of age and %d rating. Welcome to spyChat..." % (spy_salutation, name, spy_age, spy_rating))
else:
    new_user=1
    entry()  ######taking details of new user
spy_chat(new_user)