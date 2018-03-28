print("Hello world")
print ('what\'s up?')
print ('Let\'s get started...')
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

def add_status(current_status_message):
    if current_status_message != None:
      print ("Your current status message is " + current_status_message + "\n")
    else:
      print( 'You don\'t have any status message currently \n')
    default = input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = input("What status message do you want to set?")
        if len(new_status_message) > 0:
           updated_status_message = new_status_message
           STATUS_MESSAGES.append(updated_status_message)
           print(STATUS_MESSAGES)
    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print(str((item_position)) + ". " + message)
            item_position = item_position + 1
        message_selection = int(input("\nChoose from the above messages "))
    if len(STATUS_MESSAGES) >= message_selection:
        updated_status_message = STATUS_MESSAGES[message_selection - 1]
    return updated_status_message

def start_chat(spy_name,spy_salutation, spy_age, spy_rating):
    current_status_message = None
    show_menu=True

    while show_menu:
            menu_choices = ("What do you want to do? \n1. Add a status update \n2. Add a friend \n3. Send a secret message \n4. Read secret messages \n 5. Read chats \n 6.Close Application  ")
            menu_choice = input(menu_choices)

            if menu_choice =="1" :
                print('You chose to update the status')
                current_status_message=add_status(current_status_message)

            elif menu_choice == "2":
                print("adding a friend")
            elif menu_choice == "3":
                print("sending a secret message")
            elif menu_choice == "4":
                print("reading message")
            elif menu_choice == "5":
                print("read chats")
            else:
                show_menu = False
spy_name = "shubhi"
spy_salutation = "miss"
spy_age = 18
spy_rating = 3.5
user =input("Do you want to continue with the default user"+spy_salutation+" "+spy_name+" ?(Y/N)")
if (user == "Y"):
    start_chat(spy_name, spy_salutation, spy_age, spy_rating)
else:
    spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy_name) > 0:
        spy_salutation = input("Should I call you Mr. or Ms.?: ")
        spy_age = int(input("What is your age?"))
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(input("What is your spy rating?"))
    else:
        print('Sorry you are not of the correct age to be a spy')
    if spy_rating > 4.5:
        print('Great ace!')
    elif spy_rating > 3.5 and spy_rating <= 4.5:
        print('You are one of the good ones.')
    elif spy_rating >= 2.5 and spy_rating <= 3.5:
        print('You can always do better')
    else:
        print('We can always use somebody to help in the office.')
    start_chat(spy_name,spy_salutation, spy_age, spy_rating)
