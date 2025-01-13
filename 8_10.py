def show_messasges(list):
    for item in list:
        print(item)

def send_messages(list, sent_messages):
    while list:
        to_send = list.pop()
        print(to_send)
        sent_messages.append(to_send)


list = ['short msg 1', 'short msg 2', 'short msg 3']
sent_messages = []

send_messages(list, sent_messages)

print(sent_messages)
print(list)