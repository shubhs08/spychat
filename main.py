#importing the packages
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import Spy,spy,ChatMessage
import csv

print ('Let\'s start the spychat application.')

def load_friends():
    with open('friends.csv', 'rb') as friends_data:
       read = csv.reader(friends_data)
    for row in read:
            spy = Spy(name=row[0], salutation=row[1],rating=float(row[2]), age=int(row[3]) )
            friends.append(spy)
def start_chat(spy):
    show_menu = True
    current_status_message = None
    spy.name1=spy.salutation+" "+spy.name
    if spy.age > 12 and spy.age < 50:
        print ("Authentication complete. Welcome " + spy.name1 + " age: "
               + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard")
        #load_friends()

    while show_menu==True:
            menu_choices = ("What do you want to do? \n1. Add a status update \n2. Add a friend \n3. Select a friend \n4. Send message \n5. Read message \n6.Read the contents of friends list \n7.Close Application  ")
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
            elif menu_choice == "6":
                for entry in friends:
                    print("Name is " + str(entry.name) + " age is " + str(entry.age) + " rating is " + str(entry.rating))
            else:
                show_menu = False

###########a function to add status###########

def add_status(current_status_message):
    updated_status_message=None
    if current_status_message != None:
      print ("Your current status message is " + current_status_message + "\n")
    else:
      print( 'You don\'t have any status message currently \n')
    default =raw_input("Do you want to select from the older status (y/n)? ")
    #this upper function converts the string to upper case
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")
        if len(new_status_message) > 0:

           STATUS_MESSAGES.append(new_status_message)
           updated_status_message = new_status_message
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
    name=raw_input("Whats your friend spy name?")
    salutation=raw_input("what would be the salutation, Mr. or Ms??")
    age = int(input("what is friends age?"))
    rating= float(input("what's your friend spy rating??"))
    if len(name) > 0 and 12 < age < 50:  # add friend
        new_friend=Spy(name=name,salutation=salutation,age=age,rating=rating)
        friends.append(new_friend)
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name,new_friend.salutation,new_friend.age,new_friend.rating])
            print("a new friend has been added")
    else:
        print("Sorry we can't add your friend's details please try again.")
    return len(friends)

##########a function to select friends#########

def select_a_friend():
    item_no = 0
    if len(friends)!=0:
        for friend in friends:
            print("%d . %s aged %d with rating %f is online" % (item_no+1, friend.name,friend.age,friend.rating))
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
    print "Your secret message is ready! to be delivered"
    new_chat = ChatMessage(message=text, sent_by_me=True)
    friends[selection].chats.append(new_chat)
    with open('chats.csv', 'a') as chat_data:
        writer = csv.writer(chat_data)
        writer.writerow([friends[selection].name, text, new_chat.time, new_chat.sent_by_me])


#####a function to read  secret message#########

def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file to be decoded?")
    secret_text = Steganography.decode(output_path)
    print("your secret message is:"+secret_text)
    print(secret_text)
    new_chat = ChatMessage(message=secret_text, sent_by_me=False)
    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"
    with open("chats.csv", 'ab') as chats_data:
        write = csv.writer(chats_data)
        write.writerow([friends[sender].name, secret_text, new_chat.time, new_chat.sent_by_me])
    print "Your secret message has been saved!"


################storing the default user details########



user =raw_input("Do you want to continue with  "+spy.salutation+" "+spy.name+" ?(Y/N)")
if (user == "Y"or user=='y' ):
     start_chat(spy)
else:
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")
        spy.age = int(raw_input("What is your age?"))
    if spy.age > 12 and spy.age < 50:
        spy.rating = float(raw_input("What is your spy rating?"))
    else:
        print('Sorry you are not of the correct age to be a spy')
    if spy.rating > 4.5:
        print('Great ace!')
    elif spy.rating > 3.5 and spy.rating <= 4.5:
        print('You are one of the good ones.')
    elif spy.rating >= 2.5 and spy.rating <= 3.5:
        print('You can always do better')
    else:
        pass

    start_chat(spy)
