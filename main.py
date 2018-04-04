#importing the packages
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import *

print ('Let\'s start the spychat application.')

#############function to start chat##########

def start_chat(spy_name,spy_salutation, spy_age, spy_rating):
    current_status_message = None
    show_menu=True
    while show_menu==True:
        #the app displays the menu with the folowing choices
            menu_choices = ("What do you want to do? \n1. Add a status update \n2. Add a friend \n3. Select a friend \n4. Send message \n5. Read message \n6.Close Application  ")
            menu_choice = raw_input(menu_choices)
            if menu_choice =="1" :
                print('You chose to update the status')
                current_status_message=add_status(current_status_message)
            elif menu_choice == "2":
                print("adding a friend")
                number = add_friends()
                print("You total have : %d friends" %(number))
            elif menu_choice == "3":
                print("selecting friends")
                select_a_friend()
            elif menu_choice == "4":
                print("sending message")
                send_message()
            elif menu_choice == "5":
                print("reading message")
                read_message()
            else:
                show_menu = False

###########a function to add status###########

def add_status(current_status_message):
    if current_status_message != None:
      print ("Your current status message is " + current_status_message + "\n")
    else:
      print( 'You don\'t have any status message currently \n')
    default =raw_input("Do you want to select from the older status (y/n)? ")
    #this upper function converts the string to upper case
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")
        if len(new_status_message) > 0:
           updated_status_message = new_status_message
           STATUS_MESSAGES.append(updated_status_message)
           print(STATUS_MESSAGES)
    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print(str((item_position)) + ". " + message)
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose from the above messages "))
        if(len(STATUS_MESSAGES)>=message_selection):
            updated_status_message=STATUS_MESSAGES[message_selection-1]
    return updated_status_message
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

friends=[]#an empty list

#########function to add a friend############


def add_friends():
    #new_friend = {"Name": "", "Salutation": "", "age": 0, "Rating": 0.0, "Chats": [] }
    name=raw_input("Whats your friend spy name?")
    salutation=raw_input("what would be the salutation, Mr. or Mrs??")
    #Name= new_friend["Salutation"] + " " + new_friend["Name"]
    age = int(input("what is friends age?"))
    rating= float(input("what's your friend spy rating??"))
    if len(name) > 0 and 12 < age < 50:  # add friend
        friend_no=Spy(name,salutation,age,rating)
        friends.append(friend_no)
    else:      #####invalid details
        print("Sorry we can't add your friend's details please try again.")
    return len(friends)

##########a function to select friends#########

def select_a_friend():
    item_no = 0
    if len(friends)!=0:
        for friend in friends:
            print("%d . %s" % (item_no+1, friend["name"]))
            item_no = item_no + 1
        friend_no = int(input("Select your Friend : "))
        if friend_no<=len(friends) and friend_no!=0:
            print("You selected %d no Friend" % friend_no)
            return friend_no-1
        else:
            print("Wrong input, please try again...")
    else:
        print("Sorry no Friend added till now, plz add a friend first...")
        friend_no=add_friends()
        print("No. of Friends: %d" % friend_no)
        select_a_friend()
# function to send secret message

def send_message():
    selection = select_a_friend()
    original_image = raw_input("What is the name of the image?")
    output_image = 'output_new.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_image, text)
    #new_chat = {
       # "message": text,
       # "time": datetime.now(),
        #"sent_by_me": True,

    #}
    chat = ChatMessage(text, True)
    friends[selection]["Chats"].append(chat)

    #friends[selection]['chats']=(new_chat)
    print "Your secret message is ready! to be delivered"


#####a function to read  secret message#########

def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file to be decoded?")
    secret_text = Steganography.decode(output_path)
    print("your secret message is:"+secret_text)
    chat = ChatMessage(secret_text, True)
    friends[sender]["Chats"].append(chat)
    print(secret_text)
    #new_chat = {
    #"message": secret_text,
    #"time": datetime.now(),
    #"sent_by_me": False
    #}
    #friends[sender]['chats']=(new_chat)
    print(secret_text)
    print "Your secret message has been saved! spy"


################storing the default user details########

#spy_name = "shubhi"
#spy_salutation = "miss"
#spy_age = 18
#spy_rating = 3.5
#asking to continue with default or create a new one

user =raw_input("Do you want to continue with  "+Spy.salutation+" "+Spy.name+" ?(Y/N)")
if (user == "Y"or user=='y' ):
    from spy_details import spy

    print('Welcome,%s  %s with %d years of age and %.1f rating. Welcome to SpyChat.... ' % (
    spy.salutation, spy.name, spy.age, spy.rating))
    from spy_details import friend_one, friend_three, friend_two

    Friends = [friend_one, friend_two, friend_three]
    start_chat(spy_name, spy_salutation, spy_age, spy_rating)
else:
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy_name) > 0:
        spy_salutation = raw_input("Should I call you Mr. or Ms.?: ")
        spy_age = int(raw_input("What is your age?"))
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(raw_input("What is your spy rating?"))
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
    print ("Authentication complete. Welcome " + spy_name + " age: " \
               + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard")
    start_chat(spy_name,spy_salutation, spy_age, spy_rating)
