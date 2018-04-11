from datetime import datetime
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.friends = []
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


# for a default user
spy = Spy("Shubhi", "Ms.", 21, 4.6)

#existing friends
friend_one = Spy("Sakshi", "Mr.", 21, 4.1)
friend_two = Spy("Neeti", "Mr.", 21, 4.4)
friend_three = Spy("Tanya", "Ms.", 23, 4.5)

friends = [friend_one, friend_two, friend_three]

#chat class
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

